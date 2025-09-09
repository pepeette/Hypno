# """
# Complete Pattern Discovery & Mapping Assessment Page
# Streamlit implementation - neutral presentation without pattern categorization
# """
# import streamlit as st
# from datetime import datetime
# import json

# class PatternAssessment:
#     """Complete pattern assessment with neutral question presentation"""
    
#     def __init__(self):
#         # Initialize session state for assessment
#         if 'assessment_data' not in st.session_state:
#             st.session_state.assessment_data = {}
#         if 'assessment_completed' not in st.session_state:
#             st.session_state.assessment_completed = False
#         if 'current_question' not in st.session_state:
#             st.session_state.current_question = 1
#         if 'assessment_scores' not in st.session_state:
#             st.session_state.assessment_scores = {}
        
#         # Pattern definitions for backend scoring only
#         self.patterns = {
#             1: "Unhappiness Culture",
#             2: "Power Struggles", 
#             3: "Systematic Mistrust",
#             4: "Separation/Division",
#             5: "Doing vs Being",
#             6: "Compartmentalized Authenticity",
#             7: "Self-Sacrifice/Care Avoidance",
#             8: "Inherited Missions",
#             9: "Context-Dependent Weakness"
#         }
        
#         # All questions in neutral sequence without categorization
#         self.questions = self._get_all_questions()
#         self.total_questions = len(self.questions)
        
#         # Backend mapping for scoring (not visible to user)
#         self.question_patterns = self._get_question_pattern_mapping()
    
#     def _get_all_questions(self):
#         """Return all questions in mixed order without pattern grouping"""
#         return [
#             {
#                 'id': 'q1',
#                 'text': 'When something genuinely wonderful happens to you, within 60 seconds you typically:',
#                 'options': [
#                     "Feel genuine joy and want to celebrate",
#                     'Think "this won\'t last" or "what\'s the catch?"',
#                     "Feel guilty, like you don't deserve it",
#                     "Immediately worry about what bad thing will happen to balance it",
#                     "Try to downplay it so others don't feel bad"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q2',
#                 'text': 'When someone disagrees with you or challenges your position, your body:',
#                 'options': [
#                     "Stays relatively calm and curious",
#                     "Tenses up immediately, ready to fight",
#                     "Gets hot, heart races, adrenaline surges",
#                     "Shuts down, goes numb, wants to flee",
#                     "Feels attacked, even if they're being respectful"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q3',
#                 'text': 'Your default assumption about new people\'s intentions toward you:',
#                 'options': [
#                     "Most people are generally well-meaning",
#                     "They're probably judging me negatively",
#                     "They want to use or manipulate me somehow",
#                     "They'll reject me when they see my flaws",
#                     "They have hidden agendas I need to figure out"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q4',
#                 'text': 'When facing important life choices, you typically:',
#                 'options': [
#                     "Look for creative solutions that honor multiple values",
#                     "Feel trapped between impossible either/or options",
#                     "See only two extreme alternatives",
#                     "Get paralyzed by black-and-white thinking",
#                     "Feel like you can't have what you really want"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q5',
#                 'text': 'Complete this honestly: "I am valuable when I..."',
#                 'options': [
#                     "Simply exist as I am",
#                     "Accomplish something important",
#                     "Help or please other people",
#                     "Prove my worth through performance",
#                     "Stay busy and productive"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q6',
#                 'text': 'Your personality or behavior significantly changes based on:',
#                 'options': [
#                     "It stays pretty consistent across all contexts",
#                     "Which group of people you're with",
#                     "Professional versus personal settings",
#                     "Whether you're in control or following others",
#                     "If you're the expert or the newcomer"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q7',
#                 'text': 'When it comes to your own health, fitness, or wellbeing:',
#                 'options': [
#                     "I naturally prioritize my wellbeing alongside others'",
#                     "I know what to do but can't make myself do it",
#                     "I care for everyone else first, then there's no energy left",
#                     "I feel selfish focusing on my own needs",
#                     "I'm great at advising others but terrible at following my own advice"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q8',
#                 'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
#                 'options': [
#                     "Genuinely what you desire for your own life",
#                     "What your family expected or dreamed for you",
#                     "Honoring someone who died or sacrificed for you",
#                     "Proving you're worthy of someone's love or sacrifice",
#                     "What you think you 'should' want based on your background"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q9',
#                 'text': 'With your closest friends or certain social groups, you:',
#                 'options': [
#                     "Stay true to your values and boundaries",
#                     "Become someone you don't respect or recognize",
#                     "Lose all your usual boundaries and standards",
#                     "Act against your stated values and beliefs",
#                     "Can't say no even when you desperately want to"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q10',
#                 'text': 'Complete this sentence quickly: "When I\'m truly happy, I..."',
#                 'options': [
#                     "Embrace it fully and share it with others",
#                     "Wait for the other shoe to drop",
#                     "Feel uncomfortable, like I'm tempting fate",
#                     "Sabotage it somehow or create problems",
#                     "Feel guilty and try to tone it down"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q11',
#                 'text': 'Rate your agreement: "I feel guilty when things are going too well"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q12',
#                 'text': 'During a disagreement, you\'re most likely to:',
#                 'options': [
#                     "Listen to understand their perspective",
#                     "Attack their position aggressively",
#                     "Withdraw and shut down emotionally",
#                     "Manipulate the situation to get your way",
#                     "Submit externally but feel resentful internally"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q13',
#                 'text': 'When you enter a room of strangers, you automatically think:',
#                 'options': [
#                     "These seem like interesting people to meet",
#                     "They're probably thinking something critical about me",
#                     "I don't belong here",
#                     "I need to figure out the social dynamics quickly",
#                     "I hope I can get through this without embarrassing myself"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q14',
#                 'text': 'Complete this sentence: "In life, I have to choose between security _____ freedom"',
#                 'options': [
#                     "AND (I can have both)",
#                     "OR (I must choose one)",
#                     "This sentence doesn't resonate with me",
#                     "I've never thought about it this way",
#                     "Both seem impossible to achieve"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q15',
#                 'text': 'Rate your agreement: "My worth depends on what I achieve"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q16',
#                 'text': 'There are areas of your life where you feel completely capable, and others where you feel powerless:',
#                 'options': [
#                     "No, I feel consistently myself everywhere",
#                     "Yes - I'm like two completely different people",
#                     "I'm strong professionally but weak personally",
#                     "I'm confident socially but insecure privately",
#                     "I lead some groups but follow others completely"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q17',
#                 'text': 'You consistently have energy and motivation for:',
#                 'options': [
#                     "Both personal and external responsibilities equally",
#                     "Other people's goals but not your own",
#                     "Work projects but not personal care",
#                     "Helping others but not helping yourself",
#                     "Everything except what your body needs"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q18',
#                 'text': 'When you think about what YOU actually want (separate from all expectations):',
#                 'options': [
#                     "You can access it clearly and confidently",
#                     "You honestly don't know anymore",
#                     "You feel guilty for wanting something different",
#                     "You feel like you'd be betraying someone important",
#                     "You're afraid it's not worthy or important enough"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q19',
#                 'text': 'There are specific people around whom you consistently make choices you later regret:',
#                 'options': [
#                     "No, I make similar choices regardless of who's around",
#                     "Yes, and I know who they are but can't seem to stop",
#                     "I become weak-willed around certain personality types",
#                     "I desperately want their approval and will do anything for it",
#                     "I'm afraid of conflict so I go along with things I hate"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q20',
#                 'text': 'Growing up, which phrase did you hear most often?',
#                 'options': [
#                     "You can achieve anything you set your mind to",
#                     "Life is tough, get used to it",
#                     "Don't get your hopes up",
#                     "We're not here to have fun",
#                     "Good things happen to other people, not us"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q21',
#                 'text': 'While someone is explaining their viewpoint, you\'re typically:',
#                 'options': [
#                     "Genuinely trying to understand their experience",
#                     "Preparing your counterargument",
#                     "Looking for flaws in their reasoning",
#                     "Waiting for them to stop so you can respond",
#                     "Feeling defensive or personally attacked"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q22',
#                 'text': 'You show your true, unfiltered self:',
#                 'options': [
#                     "Pretty freely with most people",
#                     "Only to one or two people maximum",
#                     "Almost never - it's too dangerous",
#                     "After extensive testing of the other person",
#                     "When you're certain you won't be judged"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q23',
#                 'text': 'When you encounter people with very different beliefs or values:',
#                 'options': [
#                     "You're curious about their perspective",
#                     "You feel threatened or defensive",
#                     "You see them as fundamentally wrong",
#                     "You feel like you can't coexist peacefully",
#                     "You try to convert them to your way of thinking"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q24',
#                 'text': 'When you take time to do absolutely nothing productive:',
#                 'options': [
#                     "You can enjoy the rest completely",
#                     "You feel guilty and anxious",
#                     "You literally cannot do it",
#                     "You feel worthless and lazy",
#                     "You worry about what others will think"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q25',
#                 'text': 'Rate your agreement: "I have different versions of myself for different audiences"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q26',
#                 'text': 'When you think about doing something purely for your own pleasure or health:',
#                 'options': [
#                     "You can do it without internal conflict",
#                     "You feel guilty and selfish",
#                     "You find excuses to avoid it",
#                     "You start but don't follow through",
#                     "You sabotage it somehow"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q27',
#                 'text': 'Rate your agreement: "I would disappoint or abandon someone important if I lived my true desires"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q28',
#                 'text': 'Rate your agreement: "I\'m much stronger in some relationships than others"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q29',
#                 'text': 'When you\'re on the verge of achieving something important, you often:',
#                 'options': [
#                     "Feel excited and push through to completion",
#                     "Find ways to sabotage or delay it",
#                     "Become overwhelmed and want to quit",
#                     "Start focusing on everything that could go wrong",
#                     "Feel like you don't deserve to succeed"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q30',
#                 'text': 'Rate your agreement: "Being right is more important than being connected"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q31',
#                 'text': 'Rate your agreement: "If people really knew me, they\'d reject me"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q32',
#                 'text': 'Rate your agreement: "I often feel like I don\'t fit anywhere"',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q33',
#                 'text': 'When your efforts go completely unnoticed or unappreciated:',
#                 'options': [
#                     "You know your worth isn't dependent on external recognition",
#                     "You feel invisible and unimportant",
#                     "You work even harder to get attention",
#                     "You question whether what you did actually mattered",
#                     "You feel resentful and want to stop trying"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q34',
#                 'text': 'With certain people or in specific situations, you act in ways that surprise even yourself:',
#                 'options': [
#                     "No, I'm pretty consistent in my choices and values",
#                     "Yes, and I don't understand why it happens",
#                     "I become someone I don't recognize or like",
#                     "I lose all my usual boundaries and standards",
#                     "I do things that go completely against my core values"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q35',
#                 'text': 'Complete this: "Taking care of myself means I\'m..."',
#                 'options': [
#                     "Being responsible and setting a good example",
#                     "Being selfish and taking away from others",
#                     "Not working hard enough on important things",
#                     "Wasting time I should spend being productive",
#                     "Being weak or self-indulgent"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q36',
#                 'text': 'Your current life path feels:',
#                 'options': [
#                     "Like it genuinely reflects who you are",
#                     "Like fulfilling someone else's dreams",
#                     "Like honoring a debt you owe",
#                     "Like the 'right' thing but not the authentic thing",
#                     "Like you're afraid to choose differently"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q37',
#                 'text': 'In situations where there\'s social pressure to do something you don\'t want to do:',
#                 'options': [
#                     "You can say no clearly and maintain your boundaries",
#                     "You go along to avoid conflict or rejection",
#                     "You feel paralyzed and unable to speak up",
#                     "You do it but feel resentful and angry afterward",
#                     "You convince yourself you actually want to do it"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q38',
#                 'text': 'When someone genuinely compliments you, you:',
#                 'options': [
#                     'Say "thank you" and feel good about it',
#                     "Deflect or minimize it immediately",
#                     "Feel suspicious of their motives",
#                     "Immediately point out your flaws",
#                     "Feel uncomfortable and change the subject"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q39',
#                 'text': 'In group situations, you feel most comfortable when:',
#                 'options': [
#                     "Everyone can contribute authentically",
#                     "You're clearly in charge or leading",
#                     "Others agree with your perspective",
#                     "Conflict is avoided entirely",
#                     "You can control the outcome"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q40',
#                 'text': 'When someone offers you genuine help or shows you kindness:',
#                 'options': [
#                     "You can receive it gracefully",
#                     "You immediately wonder what they want in return",
#                     "You feel uncomfortable and try to reciprocate immediately",
#                     "You assume they pity you or see you as weak",
#                     "You worry about owing them something"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q41',
#                 'text': 'You feel most comfortable in:',
#                 'options': [
#                     "Diverse, inclusive communities",
#                     "Groups where everyone thinks like you",
#                     '"Us versus them" situations with clear sides',
#                     "Competitive rather than collaborative environments",
#                     "Situations where you don't have to choose sides"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q42',
#                 'text': 'When asked "Who are you when you\'re not doing anything for anyone else?"',
#                 'options': [
#                     "I know exactly who I am independent of my actions",
#                     "I honestly don't know",
#                     "I feel empty or lost",
#                     "I feel guilty for even thinking about being selfish",
#                     "I never allow myself to find out"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q43',
#                 'text': 'Your moral standards and personal boundaries:',
#                 'options': [
#                     "Remain consistent regardless of who's around",
#                     "Become flexible depending on the social context",
#                     "Disappear entirely around certain people",
#                     "Are strong in some relationships but weak in others",
#                     "Change based on whether you want approval from specific people"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q44',
#                 'text': 'Your energy distribution typically follows this pattern:',
#                 'options': [
#                     "Balanced between self-care and caring for others",
#                     "80% for others, 20% for self",
#                     "90% for others, 10% for self",
#                     "100% for others until burnout, then collapse",
#                     "Varies wildly with no consistent pattern"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q45',
#                 'text': 'If you completely followed your authentic desires, which relationship would be most threatened:',
#                 'options': [
#                     "None - my relationships would likely improve",
#                     "With parents who sacrificed for specific dreams",
#                     "With the memory/legacy of someone who died",
#                     "With family members who define success differently",
#                     "With a community that has certain expectations"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q46',
#                 'text': 'When you\'re with people whose approval you crave:',
#                 'options': [
#                     "You maintain your authentic self",
#                     "You become someone completely different",
#                     "You lose access to your own preferences and opinions",
#                     "You do things that violate your core values",
#                     "You feel powerless to make different choices"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q47',
#                 'text': 'Rate your willingness to question beliefs you\'ve held since childhood',
#                 'type': 'slider',
#                 'min': 1,
#                 'max': 10,
#                 'default': 5
#             },
#             {
#                 'id': 'q48',
#                 'text': 'What scares you most about completely solving your main problem?',
#                 'options': [
#                     "Nothing really scares me about solving it",
#                     "I wouldn't know who I am anymore",
#                     "People might expect too much from me",
#                     "I might lose connections with others who struggle similarly",
#                     "I'd have to take full responsibility for my life and happiness"
#                 ],
#                 'type': 'radio'
#             },
#             {
#                 'id': 'q49',
#                 'text': 'Complete this sentence: "People like me don\'t get to have..."',
#                 'type': 'text',
#                 'placeholder': 'Your response...'
#             },
#             {
#                 'id': 'q50',
#                 'text': 'What does your current problem/pattern give you that you\'re not supposed to want?',
#                 'options': [
#                     "I can't think of any hidden benefits",
#                     "Permission to avoid bigger challenges or responsibilities",
#                     "Attention, care, and sympathy from others",
#                     "An excuse for not reaching my full potential",
#                     "Control over situations and other people's behavior"
#                 ],
#                 'type': 'radio'
#             }
#         ]
    
#     def _get_question_pattern_mapping(self):
#         """Backend mapping of questions to patterns for scoring"""
#         return {
#             'q1': 1, 'q10': 1, 'q11': 1, 'q20': 1, 'q29': 1, 'q38': 1,  # Unhappiness Culture
#             'q2': 2, 'q12': 2, 'q21': 2, 'q30': 2, 'q39': 2,  # Power Struggles  
#             'q3': 3, 'q13': 3, 'q22': 3, 'q31': 3, 'q40': 3,  # Systematic Mistrust
#             'q4': 4, 'q14': 4, 'q23': 4, 'q32': 4, 'q41': 4,  # Separation/Division
#             'q5': 5, 'q15': 5, 'q24': 5, 'q33': 5, 'q42': 5,  # Doing vs Being
#             'q6': 6, 'q16': 6, 'q25': 6, 'q34': 6, 'q43': 6,  # Compartmentalized Authenticity
#             'q7': 7, 'q17': 7, 'q26': 7, 'q35': 7, 'q44': 7,  # Self-Care Avoidance
#             'q8': 8, 'q18': 8, 'q27': 8, 'q36': 8, 'q45': 8,  # Inherited Missions
#             'q9': 9, 'q19': 9, 'q28': 9, 'q37': 9, 'q46': 9   # Context-Dependent Weakness
#         }
    
#     def render(self):
#         """Render the complete assessment page"""
#         self._render_header()
        
#         if not st.session_state.assessment_completed:
#             self._render_progress()
#             self._render_current_question()
#             self._render_navigation()
#         else:
#             self._render_results()
    
#     def _render_header(self):
#         """Render assessment header"""
#         st.markdown("""
#         <div style="text-align: center; margin: 1rem 0 1rem 0;">
#             <h1>Behavioral pattern assessment</h1>
#             <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto;">
#                 This assessment helps us understand your unique patterns and design the most effective approach for your transformation. 
#                 Answer intuitively - your first response is usually most accurate.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _render_progress(self):
#         """Render progress indicator"""
#         current = st.session_state.current_question
#         progress = (current - 1) / self.total_questions
        
#         st.progress(progress)
#         st.caption(f"Question {current} of {self.total_questions}")
    
#     def _render_current_question(self):
#         """Render current question"""
#         current = st.session_state.current_question
        
#         if current <= self.total_questions:
#             question = self.questions[current - 1]
#             self._render_question(question)
#         else:
#             self._render_contact_form()
    
#     def _render_question(self, question):
#         """Render individual question"""
#         st.markdown(f"### {question['text']}")
        
#         if question['type'] == 'radio':
#             response = st.radio(
#                 question['id'],
#                 question['options'],
#                 label_visibility="collapsed",
#                 key=question['id']
#             )
            
#             if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
#                 self._save_response(question['id'], response)
#                 st.session_state.current_question += 1
#                 st.rerun()
                
#         elif question['type'] == 'slider':
#             response = st.slider(
#                 question['id'],
#                 question['min'],
#                 question['max'],
#                 question['default'],
#                 label_visibility="collapsed",
#                 key=question['id']
#             )
            
#             if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
#                 self._save_response(question['id'], response)
#                 st.session_state.current_question += 1
#                 st.rerun()
                
#         elif question['type'] == 'text':
#             response = st.text_input(
#                 question['id'],
#                 placeholder=question['placeholder'],
#                 label_visibility="collapsed",
#                 key=question['id']
#             )
            
#             if st.button("Next Question", type="primary", key=f"next_{question['id']}"):
#                 self._save_response(question['id'], response)
#                 st.session_state.current_question += 1
#                 st.rerun()
    
#     def _render_contact_form(self):
#         """Render final contact form"""
#         st.markdown("### Almost Complete!")
#         st.write("Please provide your contact details to receive your comprehensive assessment results:")
        
#         with st.form("contact_form"):
#             name = st.text_input("Full Name*", placeholder="Your full name")
#             email = st.text_input("Email Address*", placeholder="your@email.com")
#             concern = st.text_area("Primary Concern", placeholder="What specific issue brought you to this assessment?", height=100)
            
#             if st.form_submit_button("Complete Assessment & Send Results", type="primary"):
#                 if self._validate_contact_info(name, email):
#                     self._save_response('contact_name', name)
#                     self._save_response('contact_email', email)
#                     self._save_response('contact_concern', concern)
#                     self._complete_assessment()
#                     st.session_state.assessment_completed = True
#                     st.rerun()
#                 else:
#                     st.error("Please provide your name and a valid email address to receive your results.")
    
#     def _render_navigation(self):
#         """Render navigation buttons"""
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col1:
#             if st.session_state.current_question > 1:
#                 if st.button("Previous"):
#                     st.session_state.current_question -= 1
#                     st.rerun()
        
#         with col3:
#             if st.button("Save Progress"):
#                 st.success("Progress saved! You can return to complete the assessment anytime.")
    
#     def _save_response(self, question_id, response):
#         """Save question response"""
#         st.session_state.assessment_data[question_id] = response
    
#     def _validate_contact_info(self, name, email):
#         """Validate contact information"""
#         import re
#         if not name or not email:
#             return False
#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         return re.match(email_pattern, email) is not None
    
#     def _complete_assessment(self):
#         """Process and score the complete assessment"""
#         scores = self._calculate_pattern_scores()
#         st.session_state.assessment_scores = scores
#         self._send_assessment_email(scores)
    
#     def _calculate_pattern_scores(self):
#         """Calculate scores for each pattern"""
#         scores = {pattern: 0 for pattern in self.patterns.keys()}
        
#         for question_id, response in st.session_state.assessment_data.items():
#             if question_id in self.question_patterns:
#                 pattern_id = self.question_patterns[question_id]
                
#                 # Score based on response type
#                 if isinstance(response, str) and question_id.startswith('q'):
#                     # For radio questions, non-first options indicate activation
#                     question = next((q for q in self.questions if q['id'] == question_id), None)
#                     if question and 'options' in question:
#                         try:
#                             response_index = question['options'].index(response)
#                             if response_index > 0:  # Not the first (healthy) option
#                                 scores[pattern_id] += 1
#                         except ValueError:
#                             pass  # Response not found in options
                            
#                 elif isinstance(response, (int, float)):
#                     # For slider questions, scores 6+ indicate activation
#                     if response >= 6:
#                         scores[pattern_id] += 1
        
#         return scores
    
#     def _send_assessment_email(self, scores):
#         """Send assessment results via email"""
#         try:
#             from utils.email_handler import send_discovery_call_email
            
#             # Get contact info
#             name = st.session_state.assessment_data.get('contact_name', 'Unknown')
#             email = st.session_state.assessment_data.get('contact_email', 'Unknown')
#             concern = st.session_state.assessment_data.get('contact_concern', 'Pattern Assessment')
            
#             # Prepare comprehensive data for email
#             assessment_data = {
#                 'name': name,
#                 'email': email,
#                 'concern': concern,
#                 'form_type': 'Complete Behavioral Pattern Assessment',
#                 'source': 'Assessment Page',
#                 'concern_description': self._format_assessment_summary(scores),
#                 'assessment_scores': scores,
#                 'raw_responses': st.session_state.assessment_data,
#                 'timestamp': datetime.now().isoformat(),
#                 'total_questions': self.total_questions,
#                 'completion_rate': '100%'
#             }
            
#             # Send email
#             success = send_discovery_call_email(assessment_data)
#             if success:
#                 st.success("Assessment results sent successfully!")
#             else:
#                 st.warning("Results processed, but email notification failed.")
                
#         except Exception as e:
#             st.error(f"Error sending results: {str(e)}")
    
#     def _format_assessment_summary(self, scores):
#         """Format assessment summary for email"""
#         primary_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
#         summary = "COMPLETE BEHAVIORAL PATTERN ASSESSMENT RESULTS\n\n"
#         summary += f"TOTAL QUESTIONS COMPLETED: {self.total_questions}\n"
#         summary += f"ASSESSMENT DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
#         summary += "PATTERN ACTIVATION SCORES:\n"
#         for pattern_id, score in primary_patterns:
#             pattern_name = self.patterns[pattern_id]
#             max_possible = len([q for q in self.question_patterns.values() if q == pattern_id])
#             activation_level = "High" if score >= 4 else "Medium" if score >= 2 else "Low"
#             summary += f"- {pattern_name}: {score}/{max_possible} ({activation_level})\n"
        
#         summary += f"\nPRIMARY THERAPEUTIC TARGET: {self.patterns[primary_patterns[0][0]]}\n"
#         summary += f"SECONDARY PATTERN: {self.patterns[primary_patterns[1][0]]}\n"
        
#         # Add change readiness if captured
#         readiness = st.session_state.assessment_data.get('q47', 'Not assessed')
#         summary += f"CHANGE READINESS: {readiness}/10\n"
        
#         # Add key responses for clinical insight
#         summary += "\nKEY CLINICAL INDICATORS:\n"
        
#         # Fear of change
#         change_fear = st.session_state.assessment_data.get('q48', 'Not provided')
#         summary += f"- Primary change fear: {change_fear}\n"
        
#         # Hidden benefits
#         hidden_benefits = st.session_state.assessment_data.get('q50', 'Not provided')
#         summary += f"- Hidden benefits: {hidden_benefits}\n"
        
#         # Limiting belief
#         limiting_belief = st.session_state.assessment_data.get('q49', 'Not provided')
#         summary += f"- Limiting belief: 'People like me don't get to have {limiting_belief}'\n"
        
#         summary += "\nRECOMMENDED SESSION FOCUS:\n"
#         summary += f"Session 1: Map {self.patterns[primary_patterns[0][0]]} and {self.patterns[primary_patterns[1][0]]} patterns\n"
#         summary += f"Session 2: Neural rewiring targeting {self.patterns[primary_patterns[0][0]]}\n"
        
#         return summary
    
#     def _render_results(self):
#         """Render assessment results"""
#         st.markdown("## Assessment complete!")
#         st.success("Your comprehensive behavioral pattern analysis has been completed and sent to our clinical team.")
        
#         scores = st.session_state.assessment_scores
#         if scores:
#             self._render_pattern_breakdown(scores)
#             self._render_next_steps()
    
#     def _render_pattern_breakdown(self, scores):
#         """Render pattern score breakdown (neutral language)"""
#         st.markdown("### Your assessment results")
        
#         # Sort patterns by score
#         sorted_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
#         st.write("Your responses are being reviewed to identify the most effective approach for your transformation. Current detailed analysis includes:")
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             total_responses = len([r for r in st.session_state.assessment_data.values() if r])
#             st.metric("Questions completed", total_responses, "Comprehensive analysis")
            
#         with col2:
#             readiness = st.session_state.assessment_data.get('q47', 5)
#             st.metric("Change readiness", f"{readiness}/10", "Self-assessment")
            
#         with col3:
#             completion_time = "25-30 minutes"
#             st.metric("Assessment depth", completion_time, "Thorough evaluation")
    
#     def _render_next_steps(self):
#         """Render next steps and booking options"""
#         st.markdown("### Your next steps")
        
#         readiness = st.session_state.assessment_data.get('q47', 5)
        
#         if readiness >= 7:
#             st.success("Your responses indicate strong readiness for transformation. You're an excellent candidate for the rapid change method.")
#         else:
#             st.info("Your assessment shows good potential for transformation. A discovery call will help determine the best approach.")
        
#         st.markdown("""
#         **What happens next:**
        
#         1. **Clinical Review**: Your responses are analyzed to create a personalized transformation strategy
#         2. **Discovery Call**: We discuss your specific patterns and design your approach  
#         3. **Transformation Sessions**: Begin your rapid pattern rewiring process
        
#         During your discovery call, we'll:
#         - Review your assessment results together
#         - Explain how your specific patterns can be transformed
#         - Answer all your questions about the process
#         - Determine if you're ready to proceed with sessions
#         """)
        
#         st.markdown("### Book your discovery call")
#         st.write("Let's discuss your personalized transformation plan based on your assessment. Review the 2+1 steps proven method at https://hypnotherapy.streamlit.app/")
        
#         # Use consistent styling for the CTA button
#         st.markdown("""
#         <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" class="cta-button">
#             Schedule Your Free Discovery Call
#         </a>
#         """, unsafe_allow_html=True)
        
#         st.markdown("---")
#         st.markdown("**Confidential & professional**: Your assessment results are reviewed only by our clinical team and are kept strictly confidential. All discussions during your discovery call follow professional therapeutic standards.")


# class AssessPage:
#     """Main assessment page component"""
    
#     def __init__(self):
#         self.assessment = PatternAssessment()
    
#     def render(self):
#         """Render the complete assessment page"""
#         self.assessment.render()


# # Factory function for clean import
# def create_assess_page():
#     """Factory function to create AssessPage instance"""
#     return AssessPage()










"""
Complete Behavioral Pattern Assessment Page
pages/assess.py - Ready for production deployment
"""
import streamlit as st
from datetime import datetime
import json

class PatternAssessment:
    """Pattern assessment with comprehensive clinical mapping"""
    
    def __init__(self):
        # Initialize session state
        if 'assessment_data' not in st.session_state:
            st.session_state.assessment_data = {}
        if 'assessment_completed' not in st.session_state:
            st.session_state.assessment_completed = False
        if 'current_section' not in st.session_state:
            st.session_state.current_section = 1
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 1
        if 'assessment_scores' not in st.session_state:
            st.session_state.assessment_scores = {}
        if 'clinical_insights' not in st.session_state:
            st.session_state.clinical_insights = {}
        
        # Pattern definitions
        self.patterns = {
            1: "Unhappiness culture",
            2: "Power struggles", 
            3: "Systematic mistrust",
            4: "Separation/Division",
            5: "Doing vs being",
            6: "Compartmentalized authenticity",
            7: "Self-sacrifice/Care avoidance",
            8: "Inherited missions",
            9: "Context-dependent weakness"
        }
        
        # Progressive disclosure sections
        self.sections = {
            1: {"name": "Pattern identification", "questions": 10},
            2: {"name": "Clinical insights", "questions": 8}, 
            3: {"name": "Change readiness", "questions": 7}
        }
        
        # Question sets
        self.questions = self._get_questions()
        
        # Clinical mapping
        self.question_patterns = self._get_question_pattern_mapping()
    
    def _get_questions(self):
        """Comprehensive question set with clinical mapping focus"""
        return {
            # Section 1: Core pattern identification (15 questions)
            1: [
                {
                    'id': 'q1_1',
                    'text': 'When something genuinely wonderful happens to you, within 60 seconds you typically:',
                    'options': [
                        "Feel genuine joy and want to celebrate",
                        'Think "this won\'t last" or "what\'s the catch?"',
                        "Feel guilty, like you don't deserve it",
                        "Immediately worry about what bad thing will happen to balance it",
                        "Try to downplay it so others don't feel bad"
                    ],
                    'type': 'radio',
                    'pattern': 1,
                    'weight': 'high'
                },
                {
                    'id': 'q1_2',
                    'text': 'Complete this quickly: "When I\'m truly happy, I..."',
                    'options': [
                        "Embrace it fully and share it with others",
                        "Wait for the other shoe to drop",
                        "Feel uncomfortable, like I'm tempting fate",
                        "Sabotage it somehow or create problems",
                        "Feel guilty and try to tone it down"
                    ],
                    'type': 'radio',
                    'pattern': 1,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_3',
                    'text': 'Rate your agreement: "I feel guilty when things are going too well"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 1,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_4',
                    'text': 'When someone disagrees with you or challenges your position, your body:',
                    'options': [
                        "Stays relatively calm and curious",
                        "Tenses up immediately, ready to fight",
                        "Gets hot, heart races, adrenaline surges",
                        "Shuts down, goes numb, wants to flee",
                        "Feels attacked, even if they're being respectful"
                    ],
                    'type': 'radio',
                    'pattern': 2,
                    'weight': 'high'
                },
                {
                    'id': 'q1_5',
                    'text': 'During a disagreement, you\'re most likely to:',
                    'options': [
                        "Listen to understand their perspective",
                        "Attack their position aggressively",
                        "Withdraw and shut down emotionally",
                        "Manipulate the situation to get your way",
                        "Submit externally but feel resentful internally"
                    ],
                    'type': 'radio',
                    'pattern': 2,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_6',
                    'text': 'Rate your agreement: "Being right is more important than being connected"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 2,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_7',
                    'text': 'Your default assumption about new people\'s intentions toward you:',
                    'options': [
                        "Most people are generally well-meaning",
                        "They're probably judging me negatively",
                        "They want to use or manipulate me somehow",
                        "They'll reject me when they see my flaws",
                        "They have hidden agendas I need to figure out"
                    ],
                    'type': 'radio',
                    'pattern': 3,
                    'weight': 'high'
                },
                {
                    'id': 'q1_8',
                    'text': 'When you enter a room of strangers, you automatically think:',
                    'options': [
                        "These seem like interesting people to meet",
                        "They're probably thinking something critical about me",
                        "I don't belong here",
                        "I need to figure out the social dynamics quickly",
                        "I hope I can get through this without embarrassing myself"
                    ],
                    'type': 'radio',
                    'pattern': 3,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_9',
                    'text': 'Rate your agreement: "If people really knew me, they\'d reject me"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 3,
                    'weight': 'high'
                },
                {
                    'id': 'q1_10',
                    'text': 'When facing important life choices, you typically:',
                    'options': [
                        "Look for creative solutions that honor multiple values",
                        "Feel trapped between impossible either/or options",
                        "See only two extreme alternatives",
                        "Get paralyzed by all-or-nothing thinking",
                        "Feel like you can't have what you really want"
                    ],
                    'type': 'radio',
                    'pattern': 4,
                    'weight': 'high'
                },
                {
                    'id': 'q1_11',
                    'text': 'Complete this sentence: "In life, I have to choose between security _____ freedom"',
                    'options': [
                        "AND (I can have both)",
                        "OR (I must choose one)",
                        "This sentence doesn't resonate with me",
                        "I've never thought about it this way",
                        "Both seem impossible to achieve"
                    ],
                    'type': 'radio',
                    'pattern': 4,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_12',
                    'text': 'Complete this honestly: "I am valuable when I..."',
                    'options': [
                        "Simply exist as I am",
                        "Accomplish something important",
                        "Help or please other people",
                        "Prove my worth through performance",
                        "Stay busy and productive"
                    ],
                    'type': 'radio',
                    'pattern': 5,
                    'weight': 'high'
                },
                {
                    'id': 'q1_13',
                    'text': 'Rate your agreement: "My worth depends on what I achieve"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 5,
                    'weight': 'high'
                },
                {
                    'id': 'q1_14',
                    'text': 'When you take time to do absolutely nothing productive:',
                    'options': [
                        "You can enjoy the rest completely",
                        "You feel guilty and anxious",
                        "You literally cannot do it",
                        "You feel worthless and lazy",
                        "You worry about what others will think"
                    ],
                    'type': 'radio',
                    'pattern': 5,
                    'weight': 'medium'
                },
                {
                    'id': 'q1_15',
                    'text': 'Your personality or behavior significantly changes based on:',
                    'options': [
                        "It stays pretty consistent across all contexts",
                        "Which group of people you're with",
                        "Professional versus personal settings",
                        "Whether you're in control or following others",
                        "If you're the expert or the newcomer"
                    ],
                    'type': 'radio',
                    'pattern': 6,
                    'weight': 'high'
                }
            ],
            
            # Section 2: Deeper insights (15 questions)
            2: [
                {
                    'id': 'q2_1',
                    'text': 'Rate your agreement: "I have different versions of myself for different audiences"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 6,
                    'weight': 'high'
                },
                {
                    'id': 'q2_2',
                    'text': 'There are areas of your life where you feel completely capable, and others where you feel powerless:',
                    'options': [
                        "No, I feel consistently myself everywhere",
                        "Yes - I'm like two completely different people",
                        "I'm strong professionally but weak personally",
                        "I'm confident socially but insecure privately",
                        "I lead some groups but follow others completely"
                    ],
                    'type': 'radio',
                    'pattern': 6,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_3',
                    'text': 'When it comes to your own health, fitness, or wellbeing:',
                    'options': [
                        "I naturally prioritize my wellbeing alongside others'",
                        "I know what to do but can't make myself do it",
                        "I care for everyone else first, then there's no energy left",
                        "I feel selfish focusing on my own needs",
                        "I'm great at advising others but terrible at following my own advice"
                    ],
                    'type': 'radio',
                    'pattern': 7,
                    'weight': 'high'
                },
                {
                    'id': 'q2_4',
                    'text': 'You consistently have energy and motivation for:',
                    'options': [
                        "Both personal and external responsibilities equally",
                        "Other people's goals but not your own",
                        "Work projects but not personal care",
                        "Helping others but not helping yourself",
                        "Everything except what your body needs"
                    ],
                    'type': 'radio',
                    'pattern': 7,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_5',
                    'text': 'When you think about doing something purely for your own pleasure or health:',
                    'options': [
                        "You can do it without internal conflict",
                        "You feel guilty and selfish",
                        "You find excuses to avoid it",
                        "You start but don't follow through",
                        "You sabotage it somehow"
                    ],
                    'type': 'radio',
                    'pattern': 7,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_6',
                    'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
                    'options': [
                        "Genuinely what you desire for your own life",
                        "What your family expected or dreamed for you",
                        "Honoring someone who died or sacrificed for you",
                        "Proving you're worthy of someone's love or sacrifice",
                        "What you think you 'should' want based on your background"
                    ],
                    'type': 'radio',
                    'pattern': 8,
                    'weight': 'high'
                },
                {
                    'id': 'q2_7',
                    'text': 'When you think about what YOU actually want (separate from all expectations):',
                    'options': [
                        "You can access it clearly and confidently",
                        "You honestly don't know anymore",
                        "You feel guilty for wanting something different",
                        "You feel like you'd be betraying someone important",
                        "You're afraid it's not worthy or important enough"
                    ],
                    'type': 'radio',
                    'pattern': 8,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_8',
                    'text': 'Rate your agreement: "I would disappoint or abandon someone important if I lived my true desires"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 8,
                    'weight': 'high'
                },
                {
                    'id': 'q2_9',
                    'text': 'With your closest friends or certain social groups, you:',
                    'options': [
                        "Stay true to your values and boundaries",
                        "Become someone you don't respect or recognize",
                        "Lose all your usual boundaries and standards",
                        "Act against your stated values and beliefs",
                        "Can't say no even when you desperately want to"
                    ],
                    'type': 'radio',
                    'pattern': 9,
                    'weight': 'high'
                },
                {
                    'id': 'q2_10',
                    'text': 'There are specific people around whom you consistently make choices you later regret:',
                    'options': [
                        "No, I make similar choices regardless of who's around",
                        "Yes, and I know who they are but can't seem to stop",
                        "I become weak-willed around certain personality types",
                        "I desperately want their approval and will do anything for it",
                        "I'm afraid of conflict so I go along with things I hate"
                    ],
                    'type': 'radio',
                    'pattern': 9,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_11',
                    'text': 'Rate your agreement: "I\'m much stronger in some relationships than others"',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'pattern': 9,
                    'weight': 'medium'
                },
                {
                    'id': 'q2_12',
                    'text': 'Complete this sentence: "I can\'t have what I want because..."',
                    'type': 'text',
                    'placeholder': 'Complete this thought honestly...',
                    'insight': 'core_limiting_belief'
                },
                {
                    'id': 'q2_13',
                    'text': 'What would you lose if this problem disappeared completely?',
                    'options': [
                        "Nothing - I can't think of any benefits",
                        "Attention, sympathy, and care from others",
                        "An excuse for not reaching my full potential",
                        "Permission to avoid bigger challenges",
                        "Control over situations and other people's reactions"
                    ],
                    'type': 'radio',
                    'insight': 'hidden_benefits'
                },
                {
                    'id': 'q2_14',
                    'text': 'Who would you be without this problem?',
                    'type': 'text',
                    'placeholder': 'Describe the identity shift that might concern you...',
                    'insight': 'identity_threat'
                },
                {
                    'id': 'q2_15',
                    'text': 'Who in your life benefits from you staying the same?',
                    'type': 'text',
                    'placeholder': 'Name specific people and how they benefit...',
                    'insight': 'systemic_resistance'
                }
            ],
            
            # Section 3: Transformation readiness (15 questions)
            3: [
                {
                    'id': 'q3_1',
                    'text': 'Rate your willingness to question beliefs you\'ve held since childhood:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'clinical': True,
                    'insight': 'change_readiness'
                },
                {
                    'id': 'q3_2',
                    'text': 'Rate your commitment to doing whatever it takes to change:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'clinical': True,
                    'insight': 'change_commitment'
                },
                {
                    'id': 'q3_3',
                    'text': 'What percentage of responsibility do you take for your current situation?',
                    'type': 'slider',
                    'min': 0,
                    'max': 100,
                    'default': 50,
                    'clinical': True,
                    'insight': 'responsibility_taking'
                },
                {
                    'id': 'q3_4',
                    'text': 'How much are you willing to invest (time/money/effort) in transformation?',
                    'options': [
                        "Whatever it takes - this is my priority",
                        "Significant investment if I believe it will work",
                        "Moderate investment with clear guarantees",
                        "Minimal investment - want easy solutions",
                        "Hoping for change without much effort from me"
                    ],
                    'type': 'radio',
                    'insight': 'investment_readiness'
                },
                {
                    'id': 'q3_5',
                    'text': 'When you\'ve tried to change before, what pattern always stops you?',
                    'options': [
                        "I sabotage myself right before success",
                        "I get overwhelmed and give up",
                        "Other people undermine my efforts",
                        "I convince myself it\'s not worth it",
                        "I find excuses to avoid the hard work"
                    ],
                    'type': 'radio',
                    'insight': 'sabotage_pattern'
                },
                {
                    'id': 'q3_6',
                    'text': 'When you\'re stressed, what\'s your default escape/avoidance pattern?',
                    'options': [
                        "Scroll social media or binge watch",
                        "Sleep or withdraw from everyone",
                        "Work obsessively on unimportant tasks",
                        "Eat, drink, or use substances",
                        "Start fights or create drama"
                    ],
                    'type': 'radio',
                    'insight': 'stress_response'
                },
                {
                    'id': 'q3_7',
                    'text': 'What words or phrases motivate you most?',
                    'type': 'text',
                    'placeholder': 'Language that inspires action in you...',
                    'insight': 'motivational_language'
                },
                {
                    'id': 'q3_8',
                    'text': 'What words or phrases trigger resistance in you?',
                    'type': 'text',
                    'placeholder': 'Language that makes you shut down...',
                    'insight': 'trigger_language'
                },
                {
                    'id': 'q3_9',
                    'text': 'How do you prefer to receive feedback or guidance?',
                    'options': [
                        "Direct and straightforward",
                        "Gentle and supportive",
                        "Challenging and provocative",
                        "Logical and evidence-based",
                        "Intuitive and metaphorical"
                    ],
                    'type': 'radio',
                    'insight': 'feedback_preference'
                },
                {
                    'id': 'q3_10',
                    'text': 'Rate your trust in your own ability to handle whatever comes up:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'insight': 'self_trust'
                },
                {
                    'id': 'q3_11',
                    'text': 'What would convince you that change is actually possible for you?',
                    'type': 'text',
                    'placeholder': 'What evidence or experience would you need?',
                    'insight': 'possibility_criteria'
                },
                {
                    'id': 'q3_12',
                    'text': 'What scares you most about completely solving your main problem?',
                    'options': [
                        "Nothing really scares me about solving it",
                        "I wouldn't know who I am anymore",
                        "People might expect too much from me",
                        "I might lose connections with others who struggle similarly",
                        "I'd have to take full responsibility for my life and happiness"
                    ],
                    'type': 'radio',
                    'insight': 'change_fear'
                },
                {
                    'id': 'q3_13',
                    'text': 'Complete this sentence: "People like me don\'t get to have..."',
                    'type': 'text',
                    'placeholder': 'Your response...',
                    'insight': 'limiting_belief_identity'
                },
                {
                    'id': 'q3_14',
                    'text': 'What does your current problem/pattern give you that you\'re not supposed to want?',
                    'options': [
                        "I can't think of any hidden benefits",
                        "Permission to avoid bigger challenges or responsibilities",
                        "Attention, care, and sympathy from others",
                        "An excuse for not reaching my full potential",
                        "Control over situations and other people's behavior"
                    ],
                    'type': 'radio',
                    'insight': 'secondary_gains'
                },
                {
                    'id': 'q3_15',
                    'text': 'Rate your overall readiness to begin transformation work right now:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'insight': 'overall_readiness'
                }
            ]
        }                                "Whether you're in control or following others",
                        "If you're the expert or the newcomer"
                    ],
                    'type': 'radio',
                    'pattern': 6,
                    'weight': 'high'
                },
                {
                    'id': 'q1_7',
                    'text': 'When it comes to your own health, fitness, or wellbeing:',
                    'options': [
                        "I naturally prioritize my wellbeing alongside others'",
                        "I know what to do but can't make myself do it",
                        "I care for everyone else first, then there's no energy left",
                        "I feel selfish focusing on my own needs",
                        "I'm great at advising others but terrible at following my own advice"
                    ],
                    'type': 'radio',
                    'pattern': 7,
                    'weight': 'high'
                },
                {
                    'id': 'q1_8',
                    'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
                    'options': [
                        "Genuinely what you desire for your own life",
                        "What your family expected or dreamed for you",
                        "Honoring someone who died or sacrificed for you",
                        "Proving you're worthy of someone's love or sacrifice",
                        "What you think you 'should' want based on your background"
                    ],
                    'type': 'radio',
                    'pattern': 8,
                    'weight': 'high'
                },
                {
                    'id': 'q1_9',
                    'text': 'With your closest friends or certain social groups, you:',
                    'options': [
                        "Stay true to your values and boundaries",
                        "Become someone you don't respect or recognize",
                        "Lose all your usual boundaries and standards",
                        "Act against your stated values and beliefs",
                        "Can't say no even when you desperately want to"
                    ],
                    'type': 'radio',
                    'pattern': 9,
                    'weight': 'high'
                },
                {
                    'id': 'q1_10',
                    'text': 'Rate your willingness to question beliefs you\'ve held since childhood:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'clinical': True,
                    'insight': 'change_readiness'
                }
            ],
            
            # Section 2: Clinical insights (8 questions)
            2: [
                {
                    'id': 'q2_1',
                    'text': 'Complete this sentence: "I can\'t have what I want because..."',
                    'type': 'text',
                    'placeholder': 'Complete this thought honestly...',
                    'insight': 'core_limiting_belief'
                },
                {
                    'id': 'q2_2',
                    'text': 'What would you lose if this problem disappeared completely?',
                    'options': [
                        "Nothing - I can't think of any benefits",
                        "Attention, sympathy, and care from others",
                        "An excuse for not reaching my full potential",
                        "Permission to avoid bigger challenges",
                        "Control over situations and other people's reactions"
                    ],
                    'type': 'radio',
                    'insight': 'hidden_benefits'
                },
                {
                    'id': 'q2_3',
                    'text': 'Who would you be without this problem?',
                    'type': 'text',
                    'placeholder': 'Describe the identity shift that might concern you...',
                    'insight': 'identity_threat'
                },
                {
                    'id': 'q2_4',
                    'text': 'Who in your life benefits from you staying the same?',
                    'type': 'text',
                    'placeholder': 'Name specific people and how they benefit...',
                    'insight': 'systemic_resistance'
                },
                {
                    'id': 'q2_5',
                    'text': 'When you\'ve tried to change before, what pattern always stops you?',
                    'options': [
                        "I sabotage myself right before success",
                        "I get overwhelmed and give up",
                        "Other people undermine my efforts",
                        "I convince myself it\'s not worth it",
                        "I find excuses to avoid the hard work"
                    ],
                    'type': 'radio',
                    'insight': 'sabotage_pattern'
                },
                {
                    'id': 'q2_6',
                    'text': 'What words or phrases motivate you most?',
                    'type': 'text',
                    'placeholder': 'Language that inspires action in you...',
                    'insight': 'motivational_language'
                },
                {
                    'id': 'q2_7',
                    'text': 'What words or phrases trigger resistance in you?',
                    'type': 'text',
                    'placeholder': 'Language that makes you shut down...',
                    'insight': 'trigger_language'
                },
                {
                    'id': 'q2_8',
                    'text': 'Rate your commitment to doing whatever it takes to change:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'clinical': True,
                    'insight': 'change_commitment'
                }
            ],
            
            # Section 3: Change readiness (7 questions)
            3: [
                {
                    'id': 'q3_1',
                    'text': 'What percentage of responsibility do you take for your current situation?',
                    'type': 'slider',
                    'min': 0,
                    'max': 100,
                    'default': 50,
                    'clinical': True,
                    'insight': 'responsibility_taking'
                },
                {
                    'id': 'q3_2',
                    'text': 'How much are you willing to invest (time/money/effort) in transformation?',
                    'options': [
                        "Whatever it takes - this is my priority",
                        "Significant investment if I believe it will work",
                        "Moderate investment with clear guarantees",
                        "Minimal investment - want easy solutions",
                        "Hoping for change without much effort from me"
                    ],
                    'type': 'radio',
                    'insight': 'investment_readiness'
                },
                {
                    'id': 'q3_3',
                    'text': 'When you\'re stressed, what\'s your default escape/avoidance pattern?',
                    'options': [
                        "Scroll social media or binge watch",
                        "Sleep or withdraw from everyone",
                        "Work obsessively on unimportant tasks",
                        "Eat, drink, or use substances",
                        "Start fights or create drama"
                    ],
                    'type': 'radio',
                    'insight': 'stress_response'
                },
                {
                    'id': 'q3_4',
                    'text': 'How do you prefer to receive feedback or guidance?',
                    'options': [
                        "Direct and straightforward",
                        "Gentle and supportive",
                        "Challenging and provocative",
                        "Logical and evidence-based",
                        "Intuitive and metaphorical"
                    ],
                    'type': 'radio',
                    'insight': 'feedback_preference'
                },
                {
                    'id': 'q3_5',
                    'text': 'Rate your trust in your own ability to handle whatever comes up:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'insight': 'self_trust'
                },
                {
                    'id': 'q3_6',
                    'text': 'What would convince you that change is actually possible for you?',
                    'type': 'text',
                    'placeholder': 'What evidence or experience would you need?',
                    'insight': 'possibility_criteria'
                },
                {
                    'id': 'q3_7',
                    'text': 'Rate your overall readiness to begin transformation work right now:',
                    'type': 'slider',
                    'min': 1,
                    'max': 10,
                    'default': 5,
                    'insight': 'overall_readiness'
                }
            ]
        }
    
    def _get_question_pattern_mapping(self):
        """Mapping with weights and insights"""
        mapping = {}
        for section_num, questions in self.questions.items():
            for question in questions:
                if 'pattern' in question:
                    mapping[question['id']] = {
                        'pattern': question['pattern'],
                        'weight': question.get('weight', 'medium'),
                        'insight': question.get('insight', None)
                    }
        return mapping
    
    def render(self):
        """Render the progressive assessment"""
        self._render_header()
        
        if not st.session_state.assessment_completed:
            self._render_section_progress()
            self._render_current_section()
        else:
            self._render_results()
    
    def _render_header(self):
        """Header with section context"""
        current_section = st.session_state.current_section
        section_name = self.sections[current_section]['name']
        
        st.markdown(f"""
        <div style="text-align: center; margin: 1rem 0 2rem 0;">
            <h1>Behavioral pattern assessment</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto;">
                Section {current_section}: {section_name}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_section_progress(self):
        """Progress with section awareness"""
        current_section = st.session_state.current_section
        current_question = st.session_state.current_question
        
        # Overall progress
        total_questions = sum(section['questions'] for section in self.sections.values())
        questions_completed = 0
        
        for section_num in range(1, current_section):
            questions_completed += self.sections[section_num]['questions']
        questions_completed += current_question - 1
        
        overall_progress = questions_completed / total_questions
        
        # Section progress
        section_questions = self.sections[current_section]['questions']
        section_progress = (current_question - 1) / section_questions
        
        st.progress(overall_progress, text=f"Overall progress: {int(overall_progress * 100)}%")
        st.progress(section_progress, text=f"Section {current_section}: Question {current_question} of {section_questions}")
    
    def _render_current_section(self):
        """Render current section questions"""
        current_section = st.session_state.current_section
        current_question = st.session_state.current_question
        
        if current_section in self.questions:
            questions = self.questions[current_section]
            if current_question <= len(questions):
                question = questions[current_question - 1]
                self._render_question(question)
            else:
                self._advance_section()
        else:
            self._render_contact_form()
    
    def _render_question(self, question):
        """Render question with UX"""
        st.markdown(f"### {question['text']}")
        
        # Add context for clinical questions
        if question.get('clinical'):
            st.caption("This helps us understand your current context")
        elif question.get('insight'):
            st.caption("This helps us design your personalized approach")
        
        if question['type'] == 'radio':
            response = st.radio(
                question['id'],
                question['options'],
                label_visibility="collapsed",
                key=question['id']
            )
            
            if st.button("Continue", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response, question)
                self._advance_question()
                
        elif question['type'] == 'slider':
            response = st.slider(
                question['id'],
                question['min'],
                question['max'],
                question['default'],
                label_visibility="collapsed",
                key=question['id']
            )
            
            # Add helpful labels for sliders
            col1, col2, col3 = st.columns(3)
            with col1:
                st.caption(f"{question['min']} - Low")
            with col2:
                st.caption("Current rating")
            with col3:
                st.caption(f"{question['max']} - High")
            
            if st.button("Continue", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response, question)
                self._advance_question()
                
        elif question['type'] == 'text':
            response = st.text_area(
                question['id'],
                placeholder=question['placeholder'],
                label_visibility="collapsed",
                key=question['id'],
                height=100
            )
            
            if st.button("Continue", type="primary", key=f"next_{question['id']}"):
                self._save_response(question['id'], response, question)
                self._advance_question()
        
        # Navigation
        self._render_section_navigation()
    
    def _render_section_navigation(self):
        """Navigation with section awareness"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.session_state.current_question > 1:
                if st.button("Previous"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col2:
            if st.button("Save progress"):
                st.success("Progress saved! You can return to complete the assessment anytime.")
        
        with col3:
            current_section = st.session_state.current_section
            section_questions = self.sections[current_section]['questions']
            if st.session_state.current_question < section_questions:
                if st.button("Skip question"):
                    self._advance_question()
    
    def _advance_question(self):
        """Advance to next question or section"""
        current_section = st.session_state.current_section
        section_questions = self.sections[current_section]['questions']
        
        if st.session_state.current_question < section_questions:
            st.session_state.current_question += 1
        else:
            self._advance_section()
        
        st.rerun()
    
    def _advance_section(self):
        """Advance to next section"""
        if st.session_state.current_section < len(self.sections):
            st.session_state.current_section += 1
            st.session_state.current_question = 1
        else:
            self._render_contact_form()
    
    def _save_response(self, question_id, response, question):
        """Response saving with clinical insights"""
        st.session_state.assessment_data[question_id] = response
        
        # Save clinical insights
        if 'insight' in question and question['insight']:
            insight_category = question['insight']
            if insight_category not in st.session_state.clinical_insights:
                st.session_state.clinical_insights[insight_category] = []
            
            st.session_state.clinical_insights[insight_category].append({
                'question_id': question_id,
                'response': response,
                'question_text': question['text']
            })
    
    def _render_contact_form(self):
        """Contact form with assessment context"""
        st.markdown("### Complete your assessment")
        st.write("Provide your details to receive your comprehensive behavioral pattern analysis and personalized transformation plan.")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full name*", placeholder="Your full name")
                email = st.text_input("Email address*", placeholder="your@email.com")
            
            with col2:
                phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
                preferred_contact = st.selectbox(
                    "Preferred contact method",
                    ["Email", "Phone", "WhatsApp", "No preference"]
                )
            
            primary_concern = st.text_area(
                "What specific issue brought you to this assessment?*",
                placeholder="Describe the main challenge you want to transform...",
                height=100
            )
            
            urgency = st.selectbox(
                "How urgent is resolving this issue for you?",
                ["Very urgent - affecting daily life significantly",
                 "Moderately urgent - want to address within 1-2 months", 
                 "Not urgent - exploring options for future",
                 "Curious about the process but not ready to commit"]
            )
            
            if st.form_submit_button("Complete assessment & receive results", type="primary"):
                if self._validate_contact_info(name, email, primary_concern):
                    self._save_response('contact_name', name, {'insight': 'contact_info'})
                    self._save_response('contact_email', email, {'insight': 'contact_info'})
                    self._save_response('contact_phone', phone, {'insight': 'contact_info'})
                    self._save_response('contact_preferred', preferred_contact, {'insight': 'contact_info'})
                    self._save_response('contact_concern', primary_concern, {'insight': 'primary_concern'})
                    self._save_response('contact_urgency', urgency, {'insight': 'urgency_level'})
                    
                    self._complete_assessment()
                    st.session_state.assessment_completed = True
                    st.rerun()
                else:
                    st.error("Please provide your name, valid email, and describe your primary concern.")
    
    def _validate_contact_info(self, name, email, concern):
        """Contact validation"""
        import re
        if not name or not email or not concern:
            return False
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None
    
    def _complete_assessment(self):
        """Complete assessment with comprehensive analysis"""
        # Calculate pattern scores
        pattern_scores = self._calculate_pattern_scores()
        
        # Extract clinical insights
        clinical_mapping = self._extract_clinical_mapping()
        
        # Store results
        st.session_state.assessment_scores = pattern_scores
        st.session_state.clinical_mapping = clinical_mapping
        
        # Send comprehensive email
        self._send_assessment_email(pattern_scores, clinical_mapping)
    
    def _calculate_pattern_scores(self):
        """Scoring with weights"""
        scores = {pattern: 0 for pattern in self.patterns.keys()}
        
        for question_id, response in st.session_state.assessment_data.items():
            if question_id in self.question_patterns:
                mapping = self.question_patterns[question_id]
                pattern_id = mapping['pattern']
                weight = mapping['weight']
                
                # Calculate weighted score
                score_value = 0
                
                if isinstance(response, str) and question_id.startswith('q'):
                    # Find the question to get options
                    question = None
                    for section_questions in self.questions.values():
                        for q in section_questions:
                            if q['id'] == question_id:
                                question = q
                                break
                    
                    if question and 'options' in question:
                        try:
                            response_index = question['options'].index(response)
                            if response_index > 0:  # Not the first (healthy) option
                                if weight == 'high':
                                    score_value = 2
                                elif weight == 'medium':
                                    score_value = 1.5
                                else:
                                    score_value = 1
                        except ValueError:
                            pass
                            
                elif isinstance(response, (int, float)):
                    # For slider questions
                    if response >= 7:
                        score_value = 2 if weight == 'high' else 1.5 if weight == 'medium' else 1
                    elif response >= 5:
                        score_value = 1 if weight == 'high' else 0.5
                
                scores[pattern_id] += score_value
        
        return scores
    
    def _extract_clinical_mapping(self):
        """Extract comprehensive clinical mapping for therapist"""
        mapping = {
            'core_limiting_belief': '',
            'hidden_benefits': '',
            'systemic_resistance': '',
            'identity_threat': '',
            'change_readiness_score': 0,
            'predicted_resistance_points': [],
            'intervention_keywords': '',
            'avoid_language': '',
            'session_1_focus': '',
            'session_2_target': '',
            'potential_session_3_need': ''
        }
        
        # Extract core limiting belief
        core_belief_responses = []
        if 'core_limiting_belief' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['core_limiting_belief']:
                core_belief_responses.append(item['response'])
        mapping['core_limiting_belief'] = ' | '.join(filter(None, core_belief_responses))
        
        # Extract hidden benefits
        hidden_benefits_responses = []
        if 'hidden_benefits' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['hidden_benefits']:
                hidden_benefits_responses.append(item['response'])
        mapping['hidden_benefits'] = ' | '.join(filter(None, hidden_benefits_responses))
        
        # Extract systemic resistance
        systemic_responses = []
        if 'systemic_resistance' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['systemic_resistance']:
                systemic_responses.append(item['response'])
        mapping['systemic_resistance'] = ' | '.join(filter(None, systemic_responses))
        
        # Extract identity threat
        identity_responses = []
        if 'identity_threat' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['identity_threat']:
                identity_responses.append(item['response'])
        mapping['identity_threat'] = ' | '.join(filter(None, identity_responses))
        
        # Calculate change readiness score
        readiness_scores = []
        for insight_key in ['change_readiness', 'change_commitment', 'overall_readiness']:
            if insight_key in st.session_state.clinical_insights:
                for item in st.session_state.clinical_insights[insight_key]:
                    if isinstance(item['response'], (int, float)):
                        readiness_scores.append(item['response'])
        mapping['change_readiness_score'] = round(sum(readiness_scores) / len(readiness_scores)) if readiness_scores else 5
        
        # Extract resistance patterns
        resistance_patterns = []
        if 'sabotage_pattern' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['sabotage_pattern']:
                resistance_patterns.append(item['response'])
        if 'stress_response' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['stress_response']:
                resistance_patterns.append(item['response'])
        mapping['predicted_resistance_points'] = resistance_patterns
        
        # Extract communication preferences
        motivational_lang = []
        trigger_lang = []
        if 'motivational_language' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['motivational_language']:
                motivational_lang.append(item['response'])
        if 'trigger_language' in st.session_state.clinical_insights:
            for item in st.session_state.clinical_insights['trigger_language']:
                trigger_lang.append(item['response'])
        
        mapping['intervention_keywords'] = ' | '.join(filter(None, motivational_lang))
        mapping['avoid_language'] = ' | '.join(filter(None, trigger_lang))
        
        # Determine session focus based on dominant patterns
        pattern_scores = self._calculate_pattern_scores()
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        if sorted_patterns:
            dominant_pattern = self.patterns[sorted_patterns[0][0]]
            primary_pattern = self.patterns[sorted_patterns[1][0]] if len(sorted_patterns) > 1 else ""
            
            mapping['session_1_focus'] = f"Map {dominant_pattern} and {primary_pattern} patterns"
            mapping['session_2_target'] = f"Neural rewiring targeting {dominant_pattern}"
            
            # Predict session 3 need
            if mapping['change_readiness_score'] < 6 or len(resistance_patterns) > 1:
                mapping['potential_session_3_need'] = "Likely - multiple resistance patterns and lower readiness"
            else:
                mapping['potential_session_3_need'] = "Unlikely - good readiness and clear patterns"
        
        return mapping
    
    def _send_assessment_email(self, pattern_scores, clinical_mapping):
        """Send comprehensive assessment email"""
        try:
            from utils.email_handler import send_discovery_call_email
            
            # Get contact info
            name = st.session_state.assessment_data.get('contact_name', 'Unknown')
            email = st.session_state.assessment_data.get('contact_email', 'Unknown')
            concern = st.session_state.assessment_data.get('contact_concern', 'Comprehensive Assessment')
            
            # Format comprehensive clinical report
            clinical_report = self._format_clinical_report(pattern_scores, clinical_mapping)
            
            # Prepare comprehensive email data
            email_data = {
                'name': name,
                'email': email,
                'concern': concern,
                'form_type': 'Behavioral Pattern Assessment',
                'source': 'Comprehensive Assessment Page',
                'concern_description': clinical_report,
                'pattern_scores': pattern_scores,
                'clinical_mapping': clinical_mapping,
                'raw_responses': st.session_state.assessment_data,
                'clinical_insights': st.session_state.clinical_insights,
                'timestamp': datetime.now().isoformat(),
                'total_sections': len(self.sections),
                'completion_rate': '100%',
                'urgency': st.session_state.assessment_data.get('contact_urgency', 'Standard'),
                'preferred_contact': st.session_state.assessment_data.get('contact_preferred', 'Email'),
                'phone': st.session_state.assessment_data.get('contact_phone', ''),
                'clinical_template': self._generate_clinical_template(pattern_scores, clinical_mapping)
            }
            
            # Send email
            success = send_discovery_call_email(email_data)
            if success:
                st.success("Comprehensive assessment results sent successfully!")
            else:
                st.warning("Assessment processed, but email notification failed.")
                
        except Exception as e:
            st.error(f"Error sending results: {str(e)}")
    
    def _format_clinical_report(self, pattern_scores, clinical_mapping):
        """Format comprehensive clinical report"""
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        report = "═══ BEHAVIORAL PATTERN ASSESSMENT ═══\n\n"
        report += f"CLIENT: {st.session_state.assessment_data.get('contact_name', 'Unknown')}\n"
        report += f"DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"ASSESSMENT TYPE: Comprehensive 3-Section Analysis\n\n"
        
        # Pattern scoring
        report += "═══ PATTERN ANALYSIS ═══\n"
        if sorted_patterns:
            report += f"DOMINANT PATTERN: {self.patterns[sorted_patterns[0][0]]} (Score: {sorted_patterns[0][1]:.1f}/8)\n"
            if len(sorted_patterns) > 1:
                report += f"PRIMARY PATTERN: {self.patterns[sorted_patterns[1][0]]} (Score: {sorted_patterns[1][1]:.1f}/8)\n"
            if len(sorted_patterns) > 2:
                report += f"SECONDARY PATTERN: {self.patterns[sorted_patterns[2][0]]} (Score: {sorted_patterns[2][1]:.1f}/8)\n"
        
        report += "\n═══ CLINICAL MAPPING ═══\n"
        report += f"CORE LIMITING BELIEF: {clinical_mapping['core_limiting_belief'][:200]}...\n"
        report += f"HIDDEN BENEFITS: {clinical_mapping['hidden_benefits'][:200]}...\n"
        report += f"SYSTEMIC RESISTANCE: {clinical_mapping['systemic_resistance'][:200]}...\n"
        report += f"IDENTITY THREAT: {clinical_mapping['identity_threat'][:200]}...\n"
        
        report += "\n═══ CHANGE READINESS ═══\n"
        report += f"CHANGE READINESS SCORE: {clinical_mapping['change_readiness_score']}/10\n"
        
        report += "\nPREDICTED RESISTANCE POINTS:\n"
        for i, resistance in enumerate(clinical_mapping['predicted_resistance_points'][:3], 1):
            report += f"{i}. {resistance}\n"
        
        report += "\n═══ THERAPEUTIC APPROACH ═══\n"
        report += f"SESSION 1 FOCUS: {clinical_mapping['session_1_focus']}\n"
        report += f"SESSION 2 TARGET: {clinical_mapping['session_2_target']}\n"
        report += f"POTENTIAL SESSION 3 NEED: {clinical_mapping['potential_session_3_need']}\n"
        
        report += "\n═══ COMMUNICATION PREFERENCES ═══\n"
        report += f"INTERVENTION KEYWORDS: {clinical_mapping['intervention_keywords'][:150]}...\n"
        report += f"AVOID LANGUAGE: {clinical_mapping['avoid_language'][:150]}...\n"
        
        return report
    
    def _generate_clinical_template(self, pattern_scores, clinical_mapping):
        """Generate clinical template for therapist use"""
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Extract data safely to avoid f-string issues
        client_name = st.session_state.assessment_data.get('contact_name', '_____________')
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # Safely extract pattern data
        dominant_pattern = self.patterns[sorted_patterns[0][0]] if sorted_patterns else '_____________'
        dominant_score = f"{sorted_patterns[0][1]:.1f}/8" if sorted_patterns else '___'
        
        primary_pattern = self.patterns[sorted_patterns[1][0]] if len(sorted_patterns) > 1 else '_____________'
        primary_score = f"{sorted_patterns[1][1]:.1f}/8" if len(sorted_patterns) > 1 else '___'
        
        secondary_pattern = self.patterns[sorted_patterns[2][0]] if len(sorted_patterns) > 2 else '_____________'
        secondary_score = f"{sorted_patterns[2][1]:.1f}/8" if len(sorted_patterns) > 2 else '___'
        
        # Safely extract resistance points
        resistance_1 = clinical_mapping['predicted_resistance_points'][0] if len(clinical_mapping['predicted_resistance_points']) > 0 else ''
        resistance_2 = clinical_mapping['predicted_resistance_points'][1] if len(clinical_mapping['predicted_resistance_points']) > 1 else ''
        
        template = f"""
CLIENT: {client_name}
DATE: {date_str}

DOMINANT PATTERN: {dominant_pattern} (Score: {dominant_score})
PRIMARY PATTERN: {primary_pattern} (Score: {primary_score})
SECONDARY PATTERN: {secondary_pattern} (Score: {secondary_score})

CORE LIMITING BELIEF: {clinical_mapping['core_limiting_belief'][:100]}...
HIDDEN BENEFITS: {clinical_mapping['hidden_benefits'][:100]}...
SYSTEMIC RESISTANCE: {clinical_mapping['systemic_resistance'][:100]}...
IDENTITY THREAT: {clinical_mapping['identity_threat'][:100]}...

SESSION 1 FOCUS: {clinical_mapping['session_1_focus']}
SESSION 2 TARGET: {clinical_mapping['session_2_target']}
POTENTIAL SESSION 3 NEED: {clinical_mapping['potential_session_3_need']}

CHANGE READINESS SCORE: {clinical_mapping['change_readiness_score']}/10

PREDICTED RESISTANCE POINTS:
1. {resistance_1}
2. {resistance_2}

INTERVENTION KEYWORDS: {clinical_mapping['intervention_keywords'][:100]}...
AVOID LANGUAGE: {clinical_mapping['avoid_language'][:100]}...
        """
        return template
    
    def _render_results(self):
        """Render comprehensive results page"""
        st.markdown("## Assessment complete!")
        st.success("Your comprehensive behavioral pattern analysis has been completed and sent to our clinical team.")
        
        pattern_scores = st.session_state.assessment_scores
        clinical_mapping = st.session_state.clinical_mapping
        
        if pattern_scores:
            self._render_pattern_summary(pattern_scores)
            self._render_readiness_assessment(clinical_mapping)
            self._render_next_steps(clinical_mapping)
    
    def _render_pattern_summary(self, pattern_scores):
        """Render pattern summary for client"""
        st.markdown("### Your assessment insights")
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_questions = sum(len(questions) for questions in self.questions.values())
            st.metric("Questions completed", total_questions, "Comprehensive analysis")
            
        with col2:
            readiness = st.session_state.clinical_mapping.get('change_readiness_score', 5)
            st.metric("Change readiness", f"{readiness}/10", "Self-assessment")
            
        with col3:
            if sorted_patterns:
                dominant_pattern = self.patterns[sorted_patterns[0][0]]
                st.metric("Primary focus area", dominant_pattern.replace('_', ' ').title(), "For session planning")
    
    def _render_readiness_assessment(self, clinical_mapping):
        """Render readiness assessment"""
        readiness = clinical_mapping.get('change_readiness_score', 5)
        
        if readiness >= 8:
            st.success("Excellent transformation readiness! You show strong commitment and self-awareness. You're an ideal candidate for rapid change work.")
        elif readiness >= 6:
            st.success("Good transformation potential! Your assessment shows solid readiness with some areas to address. The 2-session method should be very effective.")
        elif readiness >= 4:
            st.info("Moderate readiness for change. A discovery call will help us address any concerns and design the optimal approach for your situation.")
        else:
            st.warning("Early exploration phase. Let's discuss what might help you feel more ready for transformation during your discovery call.")
    
    def _render_next_steps(self, clinical_mapping):
        """Render personalized next steps"""
        st.markdown("### Your personalized next steps")
        
        readiness = clinical_mapping.get('change_readiness_score', 5)
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical review**: Your comprehensive responses are analyzed by our clinical team
        2. **Personalized strategy**: We design your specific transformation approach  
        3. **Discovery call**: We discuss your patterns and answer all your questions
        4. **Transformation sessions**: Begin your personalized rapid change process
        """)
        
        if readiness >= 7:
            st.markdown("""
            **Based on your high readiness score, during your discovery call we'll:**
            - Review your dominant patterns and how they can be rapidly transformed
            - Confirm you're ready to proceed directly to the 2-session transformation
            - Schedule your sessions and provide pre-session preparation materials
            """)
        else:
            st.markdown("""
            **Based on your responses, during your discovery call we'll:**
            - Address any concerns or hesitations about the change process
            - Ensure you feel completely confident before proceeding
            - Design the optimal approach for your specific situation and readiness level
            """)
        
        st.markdown("### Book your discovery call")
        st.write("Let's discuss your personalized transformation plan based on your comprehensive assessment.")
        
        # CTA with clinical context
        urgency = st.session_state.assessment_data.get('contact_urgency', '')
        if 'Very urgent' in urgency:
            st.error("Your assessment indicates this issue is significantly affecting your daily life. Priority booking recommended.")
        elif 'Moderately urgent' in urgency:
            st.warning("You indicated moderate urgency. We recommend scheduling within the next week.")
        
        st.markdown("""
        <div style="background: var(--card-bg); border: 2px solid var(--accent); border-radius: var(--radius-md); 
                    padding: 2rem; text-align: center; margin: 2rem 0;">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">Schedule your free discovery call</h3>
            <p style="margin-bottom: 1.5rem;">Review your assessment results and design your transformation plan</p>
            <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1.1rem;">
                Book your discovery call
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.caption("**Confidential & professional**: Your assessment results are reviewed only by our clinical team and are kept strictly confidential. All discussions follow professional therapeutic standards.")


class AssessPage:
    """Main assessment page component"""
    
    def __init__(self):
        self.assessment = PatternAssessment()
    
    def render(self):
        """Render the complete assessment page"""
        # Apply consistent styling
        st.markdown("""
        <style>
        /* Assessment specific styles */
        .assessment-section {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            padding: var(--space-lg);
            margin: var(--space-md) 0;
            border: 1px solid var(--border);
        }
        
        .progress-container {
            margin: var(--space-md) 0;
        }
        
        .question-container {
            background: var(--card-bg);
            border-radius: var(--radius-sm);
            padding: var(--space-lg);
            margin: var(--space-md) 0;
            border-left: 4px solid var(--accent);
        }
        
        .clinical-insight {
            background: rgba(76, 161, 163, 0.1);
            border-radius: var(--radius-sm);
            padding: var(--space-sm);
            margin: var(--space-xs) 0;
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        
        .results-summary {
            background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
            border-radius: var(--radius-md);
            padding: var(--space-xl);
            text-align: center;
            margin: var(--space-lg) 0;
        }
        
        .cta-assessment {
            background: var(--card-bg);
            border: 2px solid var(--accent);
            border-radius: var(--radius-md);
            padding: var(--space-xl);
            text-align: center;
            margin: var(--space-lg) 0;
            box-shadow: var(--shadow-md);
        }
        
        .assessment-complete {
            background: var(--success);
            color: white;
            border-radius: var(--radius-md);
            padding: var(--space-lg);
            text-align: center;
            margin: var(--space-lg) 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
        self.assessment.render()


# Factory function for clean import
def create_assess_page():
    """Factory function to create AssessPage instance"""
    return AssessPage()
