"""
Complete Pattern Discovery & Mapping Assessment Page
Streamlit implementation - neutral presentation without pattern categorization
"""
import streamlit as st
from datetime import datetime
import json

class PatternAssessment:
    """Complete pattern assessment with neutral question presentation"""
    
    def __init__(self):
        # Initialize session state for assessment
        if 'assessment_data' not in st.session_state:
            st.session_state.assessment_data = {}
        if 'assessment_completed' not in st.session_state:
            st.session_state.assessment_completed = False
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 1
        if 'assessment_scores' not in st.session_state:
            st.session_state.assessment_scores = {}
        
        # Pattern definitions for backend scoring only
        self.patterns = {
            1: "Unhappiness Culture",
            2: "Power Struggles", 
            3: "Systematic Mistrust",
            4: "Separation/Division",
            5: "Doing vs Being",
            6: "Compartmentalized Authenticity",
            7: "Self-Sacrifice/Care Avoidance",
            8: "Inherited Missions",
            9: "Context-Dependent Weakness"
        }
        
        # All questions in neutral sequence without categorization
        self.questions = self._get_all_questions()
        self.total_questions = len(self.questions)
        
        # Backend mapping for scoring (not visible to user)
        self.question_patterns = self._get_question_pattern_mapping()
    
    def _get_all_questions(self):
        """Return all questions in mixed order without pattern grouping"""
        return [
            {
                'id': 'q1',
                'text': 'When something genuinely wonderful happens to you, within 60 seconds you typically:',
                'options': [
                    "Feel genuine joy and want to celebrate",
                    'Think "this won\'t last" or "what\'s the catch?"',
                    "Feel guilty, like you don't deserve it",
                    "Immediately worry about what bad thing will happen to balance it",
                    "Try to downplay it so others don't feel bad"
                ],
                'type': 'radio'
            },
            {
                'id': 'q2',
                'text': 'When someone disagrees with you or challenges your position, your body:',
                'options': [
                    "Stays relatively calm and curious",
                    "Tenses up immediately, ready to fight",
                    "Gets hot, heart races, adrenaline surges",
                    "Shuts down, goes numb, wants to flee",
                    "Feels attacked, even if they're being respectful"
                ],
                'type': 'radio'
            },
            {
                'id': 'q3',
                'text': 'Your default assumption about new people\'s intentions toward you:',
                'options': [
                    "Most people are generally well-meaning",
                    "They're probably judging me negatively",
                    "They want to use or manipulate me somehow",
                    "They'll reject me when they see my flaws",
                    "They have hidden agendas I need to figure out"
                ],
                'type': 'radio'
            },
            {
                'id': 'q4',
                'text': 'When facing important life choices, you typically:',
                'options': [
                    "Look for creative solutions that honor multiple values",
                    "Feel trapped between impossible either/or options",
                    "See only two extreme alternatives",
                    "Get paralyzed by black-and-white thinking",
                    "Feel like you can't have what you really want"
                ],
                'type': 'radio'
            },
            {
                'id': 'q5',
                'text': 'Complete this honestly: "I am valuable when I..."',
                'options': [
                    "Simply exist as I am",
                    "Accomplish something important",
                    "Help or please other people",
                    "Prove my worth through performance",
                    "Stay busy and productive"
                ],
                'type': 'radio'
            },
            {
                'id': 'q6',
                'text': 'Your personality or behavior significantly changes based on:',
                'options': [
                    "It stays pretty consistent across all contexts",
                    "Which group of people you're with",
                    "Professional versus personal settings",
                    "Whether you're in control or following others",
                    "If you're the expert or the newcomer"
                ],
                'type': 'radio'
            },
            {
                'id': 'q7',
                'text': 'When it comes to your own health, fitness, or wellbeing:',
                'options': [
                    "I naturally prioritize my wellbeing alongside others'",
                    "I know what to do but can't make myself do it",
                    "I care for everyone else first, then there's no energy left",
                    "I feel selfish focusing on my own needs",
                    "I'm great at advising others but terrible at following my own advice"
                ],
                'type': 'radio'
            },
            {
                'id': 'q8',
                'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
                'options': [
                    "Genuinely what you desire for your own life",
                    "What your family expected or dreamed for you",
                    "Honoring someone who died or sacrificed for you",
                    "Proving you're worthy of someone's love or sacrifice",
                    "What you think you 'should' want based on your background"
                ],
                'type': 'radio'
            },
            {
                'id': 'q9',
                'text': 'With your closest friends or certain social groups, you:',
                'options': [
                    "Stay true to your values and boundaries",
                    "Become someone you don't respect or recognize",
                    "Lose all your usual boundaries and standards",
                    "Act against your stated values and beliefs",
                    "Can't say no even when you desperately want to"
                ],
                'type': 'radio'
            },
            {
                'id': 'q10',
                'text': 'Complete this sentence quickly: "When I\'m truly happy, I..."',
                'options': [
                    "Embrace it fully and share it with others",
                    "Wait for the other shoe to drop",
                    "Feel uncomfortable, like I'm tempting fate",
                    "Sabotage it somehow or create problems",
                    "Feel guilty and try to tone it down"
                ],
                'type': 'radio'
            },
            {
                'id': 'q11',
                'text': 'Rate your agreement: "I feel guilty when things are going too well"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q12',
                'text': 'During a disagreement, you\'re most likely to:',
                'options': [
                    "Listen to understand their perspective",
                    "Attack their position aggressively",
                    "Withdraw and shut down emotionally",
                    "Manipulate the situation to get your way",
                    "Submit externally but feel resentful internally"
                ],
                'type': 'radio'
            },
            {
                'id': 'q13',
                'text': 'When you enter a room of strangers, you automatically think:',
                'options': [
                    "These seem like interesting people to meet",
                    "They're probably thinking something critical about me",
                    "I don't belong here",
                    "I need to figure out the social dynamics quickly",
                    "I hope I can get through this without embarrassing myself"
                ],
                'type': 'radio'
            },
            {
                'id': 'q14',
                'text': 'Complete this sentence: "In life, I have to choose between security _____ freedom"',
                'options': [
                    "AND (I can have both)",
                    "OR (I must choose one)",
                    "This sentence doesn't resonate with me",
                    "I've never thought about it this way",
                    "Both seem impossible to achieve"
                ],
                'type': 'radio'
            },
            {
                'id': 'q15',
                'text': 'Rate your agreement: "My worth depends on what I achieve"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q16',
                'text': 'There are areas of your life where you feel completely capable, and others where you feel powerless:',
                'options': [
                    "No, I feel consistently myself everywhere",
                    "Yes - I'm like two completely different people",
                    "I'm strong professionally but weak personally",
                    "I'm confident socially but insecure privately",
                    "I lead some groups but follow others completely"
                ],
                'type': 'radio'
            },
            {
                'id': 'q17',
                'text': 'You consistently have energy and motivation for:',
                'options': [
                    "Both personal and external responsibilities equally",
                    "Other people's goals but not your own",
                    "Work projects but not personal care",
                    "Helping others but not helping yourself",
                    "Everything except what your body needs"
                ],
                'type': 'radio'
            },
            {
                'id': 'q18',
                'text': 'When you think about what YOU actually want (separate from all expectations):',
                'options': [
                    "You can access it clearly and confidently",
                    "You honestly don't know anymore",
                    "You feel guilty for wanting something different",
                    "You feel like you'd be betraying someone important",
                    "You're afraid it's not worthy or important enough"
                ],
                'type': 'radio'
            },
            {
                'id': 'q19',
                'text': 'There are specific people around whom you consistently make choices you later regret:',
                'options': [
                    "No, I make similar choices regardless of who's around",
                    "Yes, and I know who they are but can't seem to stop",
                    "I become weak-willed around certain personality types",
                    "I desperately want their approval and will do anything for it",
                    "I'm afraid of conflict so I go along with things I hate"
                ],
                'type': 'radio'
            },
            {
                'id': 'q20',
                'text': 'Growing up, which phrase did you hear most often?',
                'options': [
                    "You can achieve anything you set your mind to",
                    "Life is tough, get used to it",
                    "Don't get your hopes up",
                    "We're not here to have fun",
                    "Good things happen to other people, not us"
                ],
                'type': 'radio'
            },
            {
                'id': 'q21',
                'text': 'While someone is explaining their viewpoint, you\'re typically:',
                'options': [
                    "Genuinely trying to understand their experience",
                    "Preparing your counterargument",
                    "Looking for flaws in their reasoning",
                    "Waiting for them to stop so you can respond",
                    "Feeling defensive or personally attacked"
                ],
                'type': 'radio'
            },
            {
                'id': 'q22',
                'text': 'You show your true, unfiltered self:',
                'options': [
                    "Pretty freely with most people",
                    "Only to one or two people maximum",
                    "Almost never - it's too dangerous",
                    "After extensive testing of the other person",
                    "When you're certain you won't be judged"
                ],
                'type': 'radio'
            },
            {
                'id': 'q23',
                'text': 'When you encounter people with very different beliefs or values:',
                'options': [
                    "You're curious about their perspective",
                    "You feel threatened or defensive",
                    "You see them as fundamentally wrong",
                    "You feel like you can't coexist peacefully",
                    "You try to convert them to your way of thinking"
                ],
                'type': 'radio'
            },
            {
                'id': 'q24',
                'text': 'When you take time to do absolutely nothing productive:',
                'options': [
                    "You can enjoy the rest completely",
                    "You feel guilty and anxious",
                    "You literally cannot do it",
                    "You feel worthless and lazy",
                    "You worry about what others will think"
                ],
                'type': 'radio'
            },
            {
                'id': 'q25',
                'text': 'Rate your agreement: "I have different versions of myself for different audiences"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q26',
                'text': 'When you think about doing something purely for your own pleasure or health:',
                'options': [
                    "You can do it without internal conflict",
                    "You feel guilty and selfish",
                    "You find excuses to avoid it",
                    "You start but don't follow through",
                    "You sabotage it somehow"
                ],
                'type': 'radio'
            },
            {
                'id': 'q27',
                'text': 'Rate your agreement: "I would disappoint or abandon someone important if I lived my true desires"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q28',
                'text': 'Rate your agreement: "I\'m much stronger in some relationships than others"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q29',
                'text': 'When you\'re on the verge of achieving something important, you often:',
                'options': [
                    "Feel excited and push through to completion",
                    "Find ways to sabotage or delay it",
                    "Become overwhelmed and want to quit",
                    "Start focusing on everything that could go wrong",
                    "Feel like you don't deserve to succeed"
                ],
                'type': 'radio'
            },
            {
                'id': 'q30',
                'text': 'Rate your agreement: "Being right is more important than being connected"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q31',
                'text': 'Rate your agreement: "If people really knew me, they\'d reject me"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q32',
                'text': 'Rate your agreement: "I often feel like I don\'t fit anywhere"',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q33',
                'text': 'When your efforts go completely unnoticed or unappreciated:',
                'options': [
                    "You know your worth isn't dependent on external recognition",
                    "You feel invisible and unimportant",
                    "You work even harder to get attention",
                    "You question whether what you did actually mattered",
                    "You feel resentful and want to stop trying"
                ],
                'type': 'radio'
            },
            {
                'id': 'q34',
                'text': 'With certain people or in specific situations, you act in ways that surprise even yourself:',
                'options': [
                    "No, I'm pretty consistent in my choices and values",
                    "Yes, and I don't understand why it happens",
                    "I become someone I don't recognize or like",
                    "I lose all my usual boundaries and standards",
                    "I do things that go completely against my core values"
                ],
                'type': 'radio'
            },
            {
                'id': 'q35',
                'text': 'Complete this: "Taking care of myself means I\'m..."',
                'options': [
                    "Being responsible and setting a good example",
                    "Being selfish and taking away from others",
                    "Not working hard enough on important things",
                    "Wasting time I should spend being productive",
                    "Being weak or self-indulgent"
                ],
                'type': 'radio'
            },
            {
                'id': 'q36',
                'text': 'Your current life path feels:',
                'options': [
                    "Like it genuinely reflects who you are",
                    "Like fulfilling someone else's dreams",
                    "Like honoring a debt you owe",
                    "Like the 'right' thing but not the authentic thing",
                    "Like you're afraid to choose differently"
                ],
                'type': 'radio'
            },
            {
                'id': 'q37',
                'text': 'In situations where there\'s social pressure to do something you don\'t want to do:',
                'options': [
                    "You can say no clearly and maintain your boundaries",
                    "You go along to avoid conflict or rejection",
                    "You feel paralyzed and unable to speak up",
                    "You do it but feel resentful and angry afterward",
                    "You convince yourself you actually want to do it"
                ],
                'type': 'radio'
            },
            {
                'id': 'q38',
                'text': 'When someone genuinely compliments you, you:',
                'options': [
                    'Say "thank you" and feel good about it',
                    "Deflect or minimize it immediately",
                    "Feel suspicious of their motives",
                    "Immediately point out your flaws",
                    "Feel uncomfortable and change the subject"
                ],
                'type': 'radio'
            },
            {
                'id': 'q39',
                'text': 'In group situations, you feel most comfortable when:',
                'options': [
                    "Everyone can contribute authentically",
                    "You're clearly in charge or leading",
                    "Others agree with your perspective",
                    "Conflict is avoided entirely",
                    "You can control the outcome"
                ],
                'type': 'radio'
            },
            {
                'id': 'q40',
                'text': 'When someone offers you genuine help or shows you kindness:',
                'options': [
                    "You can receive it gracefully",
                    "You immediately wonder what they want in return",
                    "You feel uncomfortable and try to reciprocate immediately",
                    "You assume they pity you or see you as weak",
                    "You worry about owing them something"
                ],
                'type': 'radio'
            },
            {
                'id': 'q41',
                'text': 'You feel most comfortable in:',
                'options': [
                    "Diverse, inclusive communities",
                    "Groups where everyone thinks like you",
                    '"Us versus them" situations with clear sides',
                    "Competitive rather than collaborative environments",
                    "Situations where you don't have to choose sides"
                ],
                'type': 'radio'
            },
            {
                'id': 'q42',
                'text': 'When asked "Who are you when you\'re not doing anything for anyone else?"',
                'options': [
                    "I know exactly who I am independent of my actions",
                    "I honestly don't know",
                    "I feel empty or lost",
                    "I feel guilty for even thinking about being selfish",
                    "I never allow myself to find out"
                ],
                'type': 'radio'
            },
            {
                'id': 'q43',
                'text': 'Your moral standards and personal boundaries:',
                'options': [
                    "Remain consistent regardless of who's around",
                    "Become flexible depending on the social context",
                    "Disappear entirely around certain people",
                    "Are strong in some relationships but weak in others",
                    "Change based on whether you want approval from specific people"
                ],
                'type': 'radio'
            },
            {
                'id': 'q44',
                'text': 'Your energy distribution typically follows this pattern:',
                'options': [
                    "Balanced between self-care and caring for others",
                    "80% for others, 20% for self",
                    "90% for others, 10% for self",
                    "100% for others until burnout, then collapse",
                    "Varies wildly with no consistent pattern"
                ],
                'type': 'radio'
            },
            {
                'id': 'q45',
                'text': 'If you completely followed your authentic desires, which relationship would be most threatened:',
                'options': [
                    "None - my relationships would likely improve",
                    "With parents who sacrificed for specific dreams",
                    "With the memory/legacy of someone who died",
                    "With family members who define success differently",
                    "With a community that has certain expectations"
                ],
                'type': 'radio'
            },
            {
                'id': 'q46',
                'text': 'When you\'re with people whose approval you crave:',
                'options': [
                    "You maintain your authentic self",
                    "You become someone completely different",
                    "You lose access to your own preferences and opinions",
                    "You do things that violate your core values",
                    "You feel powerless to make different choices"
                ],
                'type': 'radio'
            },
            {
                'id': 'q47',
                'text': 'Rate your willingness to question beliefs you\'ve held since childhood',
                'type': 'slider',
                'min': 1,
                'max': 10,
                'default': 5
            },
            {
                'id': 'q48',
                'text': 'What scares you most about completely solving your main problem?',
                'options': [
                    "Nothing really scares me about solving it",
                    "I wouldn't know who I am anymore",
                    "People might expect too much from me",
                    "I might lose connections with others who struggle similarly",
                    "I'd have to take full responsibility for my life and happiness"
                ],
                'type': 'radio'
            },
            {
                'id': 'q49',
                'text': 'Complete this sentence: "People like me don\'t get to have..."',
                'type': 'text',
                'placeholder': 'Your response...'
            },
            {
                'id': 'q50',
                'text': 'What does your current problem/pattern give you that you\'re not supposed to want?',
                'options': [
                    "I can't think of any hidden benefits",
                    "Permission to avoid bigger challenges or responsibilities",
                    "Attention, care, and sympathy from others",
                    "An excuse for not reaching my full potential",
                    "Control over situations and other people's behavior"
                ],
                'type': 'radio'
            }
        ]
    
    def _get_question_pattern_mapping(self):
        """Backend mapping of questions to patterns for scoring"""
        return {
            'q1': 1, 'q10': 1, 'q11': 1, 'q20': 1, 'q29': 1, 'q38': 1,  # Unhappiness Culture
            'q2': 2, 'q12': 2, 'q21': 2, 'q30': 2, 'q39': 2,  # Power Struggles  
            'q3': 3, 'q13': 3, 'q22': 3, 'q31': 3, 'q40': 3,  # Systematic Mistrust
            'q4': 4, 'q14': 4, 'q23': 4, 'q32': 4, 'q41': 4,  # Separation/Division
            'q5': 5, 'q15': 5, 'q24': 5, 'q33': 5, 'q42': 5,  # Doing vs Being
            'q6': 6, 'q16': 6, 'q25': 6, 'q34': 6, 'q43': 6,  # Compartmentalized Authenticity
            'q7': 7, 'q17': 7, 'q26': 7, 'q35': 7, 'q44': 7,  # Self-Care Avoidance
            'q8': 8, 'q18': 8, 'q27': 8, 'q36': 8, 'q45': 8,  # Inherited Missions
            'q9': 9, 'q19': 9, 'q28': 9, 'q37': 9, 'q46': 9   # Context-Dependent Weakness
        }
    
    def render(self):
        """Render the complete assessment page"""
        self._render_header()
        
        if not st.session_state.assessment_completed:
            self._render_progress()
            self._render_current_question()
            self._render_navigation()
        else:
            self._render_results()
    
    def _render_header(self):
        """Render assessment header"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <h1>Behavioral patterns assessment</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto;">
                This assessment helps us understand your unique patterns and design the most effective approach for your transformation. 
                Answer intuitively - your first response is usually most accurate.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_progress(self):
        """Render progress indicator"""
        current = st.session_state.current_question
        progress = (current - 1) / self.total_questions
        
        st.progress(progress)
        st.caption(f"Question {current} of {self.total_questions}")
    
    def _render_current_question(self):
        """Render current question"""
        current = st.session_state.current_question
        
        if current <= self.total_questions:
            question = self.questions[current - 1]
            self._render_question(question)
        else:
            self._render_contact_form()
    
    def _render_question(self, question):
        """Render individual question"""
        st.markdown(f"### {question['text']}")
        
        if question['type'] == 'radio':
            response = st.radio(
                question['id'],
                question['options'],
                label_visibility="collapsed",
                key=question['id']
            )
            
            if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response)
                st.session_state.current_question += 1
                st.rerun()
                
        elif question['type'] == 'slider':
            response = st.slider(
                question['id'],
                question['min'],
                question['max'],
                question['default'],
                label_visibility="collapsed",
                key=question['id']
            )
            
            if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response)
                st.session_state.current_question += 1
                st.rerun()
                
        elif question['type'] == 'text':
            response = st.text_input(
                question['id'],
                placeholder=question['placeholder'],
                label_visibility="collapsed",
                key=question['id']
            )
            
            if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response)
                st.session_state.current_question += 1
                st.rerun()
    
    def _render_contact_form(self):
        """Render final contact form"""
        st.markdown("### Almost Complete!")
        st.write("Please provide your contact details to receive your comprehensive assessment results:")
        
        with st.form("contact_form"):
            name = st.text_input("Full Name*", placeholder="Your full name")
            email = st.text_input("Email Address*", placeholder="your@email.com")
            concern = st.text_area("Primary Concern", placeholder="What specific issue brought you to this assessment?", height=100)
            
            if st.form_submit_button("Complete Assessment & Send Results", type="primary"):
                if self._validate_contact_info(name, email):
                    self._save_response('contact_name', name)
                    self._save_response('contact_email', email)
                    self._save_response('contact_concern', concern)
                    self._complete_assessment()
                    st.session_state.assessment_completed = True
                    st.rerun()
                else:
                    st.error("Please provide your name and a valid email address to receive your results.")
    
    def _render_navigation(self):
        """Render navigation buttons"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.session_state.current_question > 1:
                if st.button("Previous"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col3:
            if st.button("Save Progress"):
                st.success("Progress saved! You can return to complete the assessment anytime.")
    
    def _save_response(self, question_id, response):
        """Save question response"""
        st.session_state.assessment_data[question_id] = response
    
    def _validate_contact_info(self, name, email):
        """Validate contact information"""
        import re
        if not name or not email:
            return False
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None
    
    def _complete_assessment(self):
        """Process and score the complete assessment"""
        scores = self._calculate_pattern_scores()
        st.session_state.assessment_scores = scores
        self._send_assessment_email(scores)
    
    def _calculate_pattern_scores(self):
        """Calculate scores for each pattern"""
        scores = {pattern: 0 for pattern in self.patterns.keys()}
        
        for question_id, response in st.session_state.assessment_data.items():
            if question_id in self.question_patterns:
                pattern_id = self.question_patterns[question_id]
                
                # Score based on response type
                if isinstance(response, str) and question_id.startswith('q'):
                    # For radio questions, non-first options indicate activation
                    question = next((q for q in self.questions if q['id'] == question_id), None)
                    if question and 'options' in question:
                        try:
                            response_index = question['options'].index(response)
                            if response_index > 0:  # Not the first (healthy) option
                                scores[pattern_id] += 1
                        except ValueError:
                            pass  # Response not found in options
                            
                elif isinstance(response, (int, float)):
                    # For slider questions, scores 6+ indicate activation
                    if response >= 6:
                        scores[pattern_id] += 1
        
        return scores
    
    def _send_assessment_email(self, scores):
        """Send assessment results via email"""
        try:
            from utils.email_handler import send_discovery_call_email
            
            # Get contact info
            name = st.session_state.assessment_data.get('contact_name', 'Unknown')
            email = st.session_state.assessment_data.get('contact_email', 'Unknown')
            concern = st.session_state.assessment_data.get('contact_concern', 'Pattern Assessment')
            
            # Prepare comprehensive data for email
            assessment_data = {
                'name': name,
                'email': email,
                'concern': concern,
                'form_type': 'Complete Behavioral Pattern Assessment',
                'source': 'Assessment Page',
                'concern_description': self._format_assessment_summary(scores),
                'assessment_scores': scores,
                'raw_responses': st.session_state.assessment_data,
                'timestamp': datetime.now().isoformat(),
                'total_questions': self.total_questions,
                'completion_rate': '100%'
            }
            
            # Send email
            success = send_discovery_call_email(assessment_data)
            if success:
                st.success("Assessment results sent successfully!")
            else:
                st.warning("Results processed, but email notification failed.")
                
        except Exception as e:
            st.error(f"Error sending results: {str(e)}")
    
    def _format_assessment_summary(self, scores):
        """Format assessment summary for email"""
        primary_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
        summary = "COMPLETE BEHAVIORAL PATTERN ASSESSMENT RESULTS\n\n"
        summary += f"TOTAL QUESTIONS COMPLETED: {self.total_questions}\n"
        summary += f"ASSESSMENT DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        summary += "PATTERN ACTIVATION SCORES:\n"
        for pattern_id, score in primary_patterns:
            pattern_name = self.patterns[pattern_id]
            max_possible = len([q for q in self.question_patterns.values() if q == pattern_id])
            activation_level = "High" if score >= 4 else "Medium" if score >= 2 else "Low"
            summary += f"- {pattern_name}: {score}/{max_possible} ({activation_level})\n"
        
        summary += f"\nPRIMARY THERAPEUTIC TARGET: {self.patterns[primary_patterns[0][0]]}\n"
        summary += f"SECONDARY PATTERN: {self.patterns[primary_patterns[1][0]]}\n"
        
        # Add change readiness if captured
        readiness = st.session_state.assessment_data.get('q47', 'Not assessed')
        summary += f"CHANGE READINESS: {readiness}/10\n"
        
        # Add key responses for clinical insight
        summary += "\nKEY CLINICAL INDICATORS:\n"
        
        # Fear of change
        change_fear = st.session_state.assessment_data.get('q48', 'Not provided')
        summary += f"- Primary change fear: {change_fear}\n"
        
        # Hidden benefits
        hidden_benefits = st.session_state.assessment_data.get('q50', 'Not provided')
        summary += f"- Hidden benefits: {hidden_benefits}\n"
        
        # Limiting belief
        limiting_belief = st.session_state.assessment_data.get('q49', 'Not provided')
        summary += f"- Limiting belief: 'People like me don't get to have {limiting_belief}'\n"
        
        summary += "\nRECOMMENDED SESSION FOCUS:\n"
        summary += f"Session 1: Map {self.patterns[primary_patterns[0][0]]} and {self.patterns[primary_patterns[1][0]]} patterns\n"
        summary += f"Session 2: Neural rewiring targeting {self.patterns[primary_patterns[0][0]]}\n"
        
        return summary
    
    def _render_results(self):
        """Render assessment results"""
        st.markdown("## Assessment Complete!")
        st.success("Your comprehensive behavioral pattern analysis has been completed and sent to our clinical team.")
        
        scores = st.session_state.assessment_scores
        if scores:
            self._render_pattern_breakdown(scores)
            self._render_next_steps()
    
    def _render_pattern_breakdown(self, scores):
        """Render pattern score breakdown (neutral language)"""
        st.markdown("### Your Assessment Results")
        
        # Sort patterns by score
        sorted_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        st.write("Our clinical team will review your responses to identify the most effective approach for your transformation. Your detailed analysis includes:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_responses = len([r for r in st.session_state.assessment_data.values() if r])
            st.metric("Questions Completed", total_responses, "Comprehensive Analysis")
            
        with col2:
            readiness = st.session_state.assessment_data.get('q47', 5)
            st.metric("Change Readiness", f"{readiness}/10", "Self-Assessment")
            
        with col3:
            completion_time = "25-30 minutes"
            st.metric("Assessment Depth", completion_time, "Thorough Evaluation")
    
    def _render_next_steps(self):
        """Render next steps and booking options"""
        st.markdown("### Your Next Steps")
        
        readiness = st.session_state.assessment_data.get('q47', 5)
        
        if readiness >= 7:
            st.success("Your responses indicate strong readiness for transformation. You're an excellent candidate for our rapid change method.")
        else:
            st.info("Your assessment shows good potential for transformation. A discovery call will help determine the best approach.")
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical Review**: Your responses are analyzed to create a personalized transformation strategy
        2. **Discovery Call**: We discuss your specific patterns and design your approach  
        3. **Transformation Sessions**: Begin your rapid pattern rewiring process
        
        During your discovery call, we'll:
        - Review your assessment results together
        - Explain how your specific patterns can be transformed
        - Answer all your questions about the process
        - Determine if you're ready to proceed with sessions
        """)
        
        st.markdown("### Book Your Discovery Call")
        st.write("Let's discuss your personalized transformation plan based on your assessment.")
        
        # Use consistent styling for the CTA button
        st.markdown("""
        <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" class="cta-button">
            Schedule Your Free Discovery Call
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("**Confidential & professional**: Your assessment results are reviewed only by our clinical team and are kept strictly confidential. All discussions during your discovery call follow professional therapeutic standards.")


class AssessPage:
    """Main assessment page component"""
    
    def __init__(self):
        self.assessment = PatternAssessment()
    
    def render(self):
        """Render the complete assessment page"""
        self.assessment.render()


# Factory function for clean import
def create_assess_page():
    """Factory function to create AssessPage instance"""
    return AssessPage()
