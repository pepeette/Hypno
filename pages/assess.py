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
3-section comprehensive assessment with clinical mapping and email integration
55 total questions across core patterns, clinical insights, and transformation readiness
"""
import streamlit as st
from datetime import datetime
import re

class BehavioralPatternAssessment:
    """Comprehensive 55-question behavioral pattern assessment"""
    
    def __init__(self):
        # Initialize session state
        self._init_session_state()
        
        # Assessment structure
        self.sections = {
            1: {"name": "Core Behavioral Patterns", "questions": 25},
            2: {"name": "Clinical Insights & Triggers", "questions": 15}, 
            3: {"name": "Transformation Readiness", "questions": 15}
        }
        
        self.total_questions = 55
        
        # Pattern definitions for clinical mapping
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
        
        # Question weights for clinical priority
        self.question_weights = {
            'high': 3,    # Critical therapeutic targets
            'medium': 2,  # Important patterns
            'low': 1      # Supporting insights
        }
        
        # All 55 questions organized by section
        self.questions = self._get_all_questions()
        
        # Clinical mapping for pattern scoring
        self.pattern_mapping = self._get_pattern_mapping()
    
    def _init_session_state(self):
        """Initialize session state variables"""
        if 'assessment_responses' not in st.session_state:
            st.session_state.assessment_responses = {}
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 1
        if 'assessment_completed' not in st.session_state:
            st.session_state.assessment_completed = False
        if 'contact_provided' not in st.session_state:
            st.session_state.contact_provided = False
        if 'assessment_results' not in st.session_state:
            st.session_state.assessment_results = {}
    
    def _get_all_questions(self):
        """Return all 55 questions organized by section"""
        return {
            # SECTION 1: CORE BEHAVIORAL PATTERNS (25 questions)
            1: {
                'text': 'When something genuinely wonderful happens to you, within 60 seconds you typically:',
                'type': 'radio',
                'options': [
                    "Feel genuine joy and want to celebrate",
                    'Think "this won\'t last" or "what\'s the catch?"',
                    "Feel guilty, like you don't deserve it", 
                    "Immediately worry about what bad thing will happen to balance it",
                    "Try to downplay it so others don't feel bad"
                ],
                'pattern': 1, 'weight': 'high'
            },
            2: {
                'text': 'When someone disagrees with you or challenges your position, your body:',
                'type': 'radio',
                'options': [
                    "Stays relatively calm and curious",
                    "Tenses up immediately, ready to fight",
                    "Gets hot, heart races, adrenaline surges", 
                    "Shuts down, goes numb, wants to flee",
                    "Feels attacked, even if they're being respectful"
                ],
                'pattern': 2, 'weight': 'high'
            },
            3: {
                'text': 'Your default assumption about new people\'s intentions toward you:',
                'type': 'radio',
                'options': [
                    "Most people are generally well-meaning",
                    "They're probably judging me negatively",
                    "They want to use or manipulate me somehow",
                    "They'll reject me when they see my flaws",
                    "They have hidden agendas I need to figure out"
                ],
                'pattern': 3, 'weight': 'high'
            },
            4: {
                'text': 'When facing important life choices, you typically:',
                'type': 'radio',
                'options': [
                    "Look for creative solutions that honor multiple values",
                    "Feel trapped between impossible either/or options",
                    "See only two extreme alternatives",
                    "Get paralyzed by black-and-white thinking", 
                    "Feel like you can't have what you really want"
                ],
                'pattern': 4, 'weight': 'high'
            },
            5: {
                'text': 'Complete this honestly: "I am valuable when I..."',
                'type': 'radio',
                'options': [
                    "Simply exist as I am",
                    "Accomplish something important",
                    "Help or please other people",
                    "Prove my worth through performance",
                    "Stay busy and productive"
                ],
                'pattern': 5, 'weight': 'high'
            },
            6: {
                'text': 'Your personality or behavior significantly changes based on:',
                'type': 'radio',
                'options': [
                    "It stays pretty consistent across all contexts",
                    "Which group of people you're with",
                    "Professional versus personal settings",
                    "Whether you're in control or following others",
                    "If you're the expert or the newcomer"
                ],
                'pattern': 6, 'weight': 'high'
            },
            7: {
                'text': 'When it comes to your own health, fitness, or wellbeing:',
                'type': 'radio',
                'options': [
                    "I naturally prioritize my wellbeing alongside others'",
                    "I know what to do but can't make myself do it",
                    "I care for everyone else first, then there's no energy left",
                    "I feel selfish focusing on my own needs",
                    "I'm great at advising others but terrible at following my own advice"
                ],
                'pattern': 7, 'weight': 'high'
            },
            8: {
                'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
                'type': 'radio',
                'options': [
                    "Genuinely what you desire for your own life",
                    "What your family expected or dreamed for you",
                    "Honoring someone who died or sacrificed for you",
                    "Proving you're worthy of someone's love or sacrifice",
                    "What you think you 'should' want based on your background"
                ],
                'pattern': 8, 'weight': 'high'
            },
            9: {
                'text': 'With your closest friends or certain social groups, you:',
                'type': 'radio',
                'options': [
                    "Stay true to your values and boundaries",
                    "Become someone you don't respect or recognize",
                    "Lose all your usual boundaries and standards",
                    "Act against your stated values and beliefs",
                    "Can't say no even when you desperately want to"
                ],
                'pattern': 9, 'weight': 'high'
            },
            10: {
                'text': 'Rate your agreement: "I feel guilty when things are going too well"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 1, 'weight': 'medium'
            },
            11: {
                'text': 'During a disagreement, you\'re most likely to:',
                'type': 'radio',
                'options': [
                    "Listen to understand their perspective",
                    "Attack their position aggressively",
                    "Withdraw and shut down emotionally",
                    "Manipulate the situation to get your way",
                    "Submit externally but feel resentful internally"
                ],
                'pattern': 2, 'weight': 'medium'
            },
            12: {
                'text': 'When you enter a room of strangers, you automatically think:',
                'type': 'radio',
                'options': [
                    "These seem like interesting people to meet",
                    "They're probably thinking something critical about me",
                    "I don't belong here",
                    "I need to figure out the social dynamics quickly",
                    "I hope I can get through this without embarrassing myself"
                ],
                'pattern': 3, 'weight': 'medium'
            },
            13: {
                'text': 'Complete this sentence: "In life, I have to choose between security _____ freedom"',
                'type': 'radio',
                'options': [
                    "AND (I can have both)",
                    "OR (I must choose one)",
                    "This sentence doesn't resonate with me",
                    "I've never thought about it this way",
                    "Both seem impossible to achieve"
                ],
                'pattern': 4, 'weight': 'medium'
            },
            14: {
                'text': 'Rate your agreement: "My worth depends on what I achieve"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 5, 'weight': 'medium'
            },
            15: {
                'text': 'There are areas of your life where you feel completely capable, and others where you feel powerless:',
                'type': 'radio',
                'options': [
                    "No, I feel consistently myself everywhere",
                    "Yes - I'm like two completely different people",
                    "I'm strong professionally but weak personally",
                    "I'm confident socially but insecure privately",
                    "I lead some groups but follow others completely"
                ],
                'pattern': 6, 'weight': 'medium'
            },
            16: {
                'text': 'You consistently have energy and motivation for:',
                'type': 'radio',
                'options': [
                    "Both personal and external responsibilities equally",
                    "Other people's goals but not your own",
                    "Work projects but not personal care",
                    "Helping others but not helping yourself",
                    "Everything except what your body needs"
                ],
                'pattern': 7, 'weight': 'medium'
            },
            17: {
                'text': 'When you think about what YOU actually want (separate from all expectations):',
                'type': 'radio',
                'options': [
                    "You can access it clearly and confidently",
                    "You honestly don't know anymore",
                    "You feel guilty for wanting something different",
                    "You feel like you'd be betraying someone important",
                    "You're afraid it's not worthy or important enough"
                ],
                'pattern': 8, 'weight': 'medium'
            },
            18: {
                'text': 'There are specific people around whom you consistently make choices you later regret:',
                'type': 'radio',
                'options': [
                    "No, I make similar choices regardless of who's around",
                    "Yes, and I know who they are but can't seem to stop",
                    "I become weak-willed around certain personality types",
                    "I desperately want their approval and will do anything for it",
                    "I'm afraid of conflict so I go along with things I hate"
                ],
                'pattern': 9, 'weight': 'medium'
            },
            19: {
                'text': 'When you\'re on the verge of achieving something important, you often:',
                'type': 'radio',
                'options': [
                    "Feel excited and push through to completion",
                    "Find ways to sabotage or delay it",
                    "Become overwhelmed and want to quit",
                    "Start focusing on everything that could go wrong",
                    "Feel like you don't deserve to succeed"
                ],
                'pattern': 1, 'weight': 'medium'
            },
            20: {
                'text': 'Rate your agreement: "Being right is more important than being connected"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 2, 'weight': 'low'
            },
            21: {
                'text': 'Rate your agreement: "If people really knew me, they\'d reject me"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 3, 'weight': 'low'
            },
            22: {
                'text': 'Rate your agreement: "I often feel like I don\'t fit anywhere"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 4, 'weight': 'low'
            },
            23: {
                'text': 'When your efforts go completely unnoticed or unappreciated:',
                'type': 'radio',
                'options': [
                    "You know your worth isn't dependent on external recognition",
                    "You feel invisible and unimportant",
                    "You work even harder to get attention",
                    "You question whether what you did actually mattered",
                    "You feel resentful and want to stop trying"
                ],
                'pattern': 5, 'weight': 'low'
            },
            24: {
                'text': 'Rate your agreement: "I have different versions of myself for different audiences"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 6, 'weight': 'low'
            },
            25: {
                'text': 'When you think about doing something purely for your own pleasure or health:',
                'type': 'radio',
                'options': [
                    "You can do it without internal conflict",
                    "You feel guilty and selfish",
                    "You find excuses to avoid it",
                    "You start but don't follow through",
                    "You sabotage it somehow"
                ],
                'pattern': 7, 'weight': 'low'
            },
            
            # SECTION 2: CLINICAL INSIGHTS & TRIGGERS (15 questions)
            26: {
                'text': 'Growing up, which phrase did you hear most often?',
                'type': 'radio',
                'options': [
                    "You can achieve anything you set your mind to",
                    "Life is tough, get used to it",
                    "Don't get your hopes up",
                    "We're not here to have fun",
                    "Good things happen to other people, not us"
                ],
                'pattern': 1, 'weight': 'high', 'clinical': 'family_origin'
            },
            27: {
                'text': 'What does your current problem/pattern give you that you\'re not supposed to want?',
                'type': 'radio',
                'options': [
                    "I can't think of any hidden benefits",
                    "Permission to avoid bigger challenges or responsibilities",
                    "Attention, care, and sympathy from others",
                    "An excuse for not reaching my full potential",
                    "Control over situations and other people's behavior"
                ],
                'pattern': 'all', 'weight': 'high', 'clinical': 'secondary_gain'
            },
            28: {
                'text': 'Complete this sentence: "People like me don\'t get to have..."',
                'type': 'text',
                'placeholder': 'Complete the sentence with what first comes to mind...',
                'pattern': 'all', 'weight': 'high', 'clinical': 'limiting_belief'
            },
            29: {
                'text': 'What scares you most about completely solving your main problem?',
                'type': 'radio',
                'options': [
                    "Nothing really scares me about solving it",
                    "I wouldn't know who I am anymore",
                    "People might expect too much from me",
                    "I might lose connections with others who struggle similarly",
                    "I'd have to take full responsibility for my life and happiness"
                ],
                'pattern': 'all', 'weight': 'high', 'clinical': 'change_fear'
            },
            30: {
                'text': 'Rate your willingness to question beliefs you\'ve held since childhood',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 'all', 'weight': 'medium', 'clinical': 'cognitive_flexibility'
            },
            31: {
                'text': 'When someone offers you genuine help or shows you kindness:',
                'type': 'radio',
                'options': [
                    "You can receive it gracefully",
                    "You immediately wonder what they want in return",
                    "You feel uncomfortable and try to reciprocate immediately",
                    "You assume they pity you or see you as weak",
                    "You worry about owing them something"
                ],
                'pattern': 3, 'weight': 'medium', 'clinical': 'trust_capacity'
            },
            32: {
                'text': 'Your current life path feels:',
                'type': 'radio',
                'options': [
                    "Like it genuinely reflects who you are",
                    "Like fulfilling someone else's dreams",
                    "Like honoring a debt you owe",
                    "Like the 'right' thing but not the authentic thing",
                    "Like you're afraid to choose differently"
                ],
                'pattern': 8, 'weight': 'medium', 'clinical': 'authenticity_gap'
            },
            33: {
                'text': 'In situations where there\'s social pressure to do something you don\'t want to do:',
                'type': 'radio',
                'options': [
                    "You can say no clearly and maintain your boundaries",
                    "You go along to avoid conflict or rejection",
                    "You feel paralyzed and unable to speak up",
                    "You do it but feel resentful and angry afterward",
                    "You convince yourself you actually want to do it"
                ],
                'pattern': 9, 'weight': 'medium', 'clinical': 'boundary_strength'
            },
            34: {
                'text': 'Rate your agreement: "I would disappoint or abandon someone important if I lived my true desires"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 8, 'weight': 'medium', 'clinical': 'loyalty_conflict'
            },
            35: {
                'text': 'When someone genuinely compliments you, you:',
                'type': 'radio',
                'options': [
                    'Say "thank you" and feel good about it',
                    "Deflect or minimize it immediately",
                    "Feel suspicious of their motives",
                    "Immediately point out your flaws",
                    "Feel uncomfortable and change the subject"
                ],
                'pattern': 1, 'weight': 'low', 'clinical': 'self_worth'
            },
            36: {
                'text': 'Complete this: "Taking care of myself means I\'m..."',
                'type': 'radio',
                'options': [
                    "Being responsible and setting a good example",
                    "Being selfish and taking away from others",
                    "Not working hard enough on important things",
                    "Wasting time I should spend being productive",
                    "Being weak or self-indulgent"
                ],
                'pattern': 7, 'weight': 'low', 'clinical': 'self_care_beliefs'
            },
            37: {
                'text': 'Your energy distribution typically follows this pattern:',
                'type': 'radio',
                'options': [
                    "Balanced between self-care and caring for others",
                    "80% for others, 20% for self",
                    "90% for others, 10% for self",
                    "100% for others until burnout, then collapse",
                    "Varies wildly with no consistent pattern"
                ],
                'pattern': 7, 'weight': 'low', 'clinical': 'energy_allocation'
            },
            38: {
                'text': 'If you completely followed your authentic desires, which relationship would be most threatened:',
                'type': 'radio',
                'options': [
                    "None - my relationships would likely improve",
                    "With parents who sacrificed for specific dreams",
                    "With the memory/legacy of someone who died",
                    "With family members who define success differently",
                    "With a community that has certain expectations"
                ],
                'pattern': 8, 'weight': 'low', 'clinical': 'relationship_threats'
            },
            39: {
                'text': 'When you\'re with people whose approval you crave:',
                'type': 'radio',
                'options': [
                    "You maintain your authentic self",
                    "You become someone completely different",
                    "You lose access to your own preferences and opinions",
                    "You do things that violate your core values",
                    "You feel powerless to make different choices"
                ],
                'pattern': 9, 'weight': 'low', 'clinical': 'approval_seeking'
            },
            40: {
                'text': 'Rate your agreement: "I\'m much stronger in some relationships than others"',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 9, 'weight': 'low', 'clinical': 'relationship_consistency'
            },
            
            # SECTION 3: TRANSFORMATION READINESS (15 questions)
            41: {
                'text': 'How urgently do you need to resolve your main concern?',
                'type': 'radio',
                'options': [
                    "Extremely urgent - affecting my daily life significantly",
                    "Quite urgent - I need change within the next few months",
                    "Moderately urgent - would like change within 6 months",
                    "Somewhat urgent - exploring options for gradual change",
                    "Not urgent - just curious about possibilities"
                ],
                'pattern': 'readiness', 'weight': 'high', 'clinical': 'urgency_level'
            },
            42: {
                'text': 'Rate your current motivation level to make significant changes (1=no motivation, 10=extremely motivated)',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 'readiness', 'weight': 'high', 'clinical': 'motivation_level'
            },
            43: {
                'text': 'How much time and energy can you realistically commit to transformation work?',
                'type': 'radio',
                'options': [
                    "Unlimited - this is my top priority right now",
                    "High commitment - can prioritize this significantly",
                    "Moderate commitment - can fit it into my schedule",
                    "Limited commitment - very busy but can make some time",
                    "Minimal commitment - extremely limited availability"
                ],
                'pattern': 'readiness', 'weight': 'high', 'clinical': 'commitment_level'
            },
            44: {
                'text': 'Your experience with personal development or therapy:',
                'type': 'radio',
                'options': [
                    "Extensive experience with multiple approaches",
                    "Some experience - tried a few different methods",
                    "Limited experience - one or two attempts",
                    "No formal experience but read/researched extensively",
                    "Complete beginner to personal development work"
                ],
                'pattern': 'readiness', 'weight': 'medium', 'clinical': 'experience_level'
            },
            45: {
                'text': 'Rate your belief that rapid change (2-3 sessions) is possible for your situation',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 'readiness', 'weight': 'medium', 'clinical': 'rapid_change_belief'
            },
            46: {
                'text': 'Your preferred communication style during sessions:',
                'type': 'radio',
                'options': [
                    "Direct and analytical - I want to understand everything",
                    "Gentle and supportive - I need a lot of encouragement",
                    "Practical and solution-focused - just tell me what to do",
                    "Exploratory and intuitive - let's see what emerges",
                    "Collaborative - I want to be an active partner in the process"
                ],
                'pattern': 'preferences', 'weight': 'medium', 'clinical': 'communication_style'
            },
            47: {
                'text': 'Your biggest concern about starting hypnotherapy:',
                'type': 'radio',
                'options': [
                    "I have no significant concerns - I'm ready to begin",
                    "Worried about losing control or being manipulated",
                    "Concerned it won't work for my specific situation",
                    "Skeptical about the science/effectiveness of hypnosis",
                    "Worried about what I might discover about myself"
                ],
                'pattern': 'preferences', 'weight': 'medium', 'clinical': 'therapy_concerns'
            },
            48: {
                'text': 'Your learning style preference:',
                'type': 'radio',
                'options': [
                    "Visual - I need to see diagrams, models, or written explanations",
                    "Auditory - I learn best through listening and discussion",
                    "Kinesthetic - I need to experience and practice things physically",
                    "Analytical - I need logical explanations and step-by-step processes",
                    "Intuitive - I prefer to feel my way through and trust instincts"
                ],
                'pattern': 'preferences', 'weight': 'low', 'clinical': 'learning_style'
            },
            49: {
                'text': 'Rate your comfort level with exploring potentially uncomfortable emotions or memories',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 'readiness', 'weight': 'low', 'clinical': 'emotional_readiness'
            },
            50: {
                'text': 'Your support system for making changes:',
                'type': 'radio',
                'options': [
                    "Very strong - family/friends actively support my growth",
                    "Generally supportive - they want what's best for me",
                    "Mixed - some support, some resistance to change",
                    "Limited support - mostly indifferent to my changes",
                    "Potentially hostile - others might resist my transformation"
                ],
                'pattern': 'readiness', 'weight': 'low', 'clinical': 'support_system'
            },
            51: {
                'text': 'Your financial investment comfort level for transformation work:',
                'type': 'radio',
                'options': [
                    "Money is not a limiting factor for important change",
                    "Can invest significantly if the approach is right",
                    "Have a moderate budget for the right solution",
                    "Budget is tight but can prioritize for important change",
                    "Very limited budget - cost is a major factor"
                ],
                'pattern': 'readiness', 'weight': 'low', 'clinical': 'financial_readiness'
            },
            52: {
                'text': 'Preferred session format:',
                'type': 'radio',
                'options': [
                    "In-person sessions only - need physical presence",
                    "Prefer in-person but open to online if needed",
                    "No preference - either format works fine",
                    "Prefer online but open to in-person if better",
                    "Online sessions only - more convenient/comfortable"
                ],
                'pattern': 'preferences', 'weight': 'low', 'clinical': 'session_preference'
            },
            53: {
                'text': 'Your timeline for starting sessions:',
                'type': 'radio',
                'options': [
                    "Immediately - ready to book this week",
                    "Very soon - within 2-3 weeks",
                    "Near future - within 1-2 months",
                    "Planning ahead - within 3-6 months",
                    "Just exploring - no specific timeline yet"
                ],
                'pattern': 'readiness', 'weight': 'low', 'clinical': 'start_timeline'
            },
            54: {
                'text': 'Rate your overall confidence that hypnotherapy can help you achieve your goals',
                'type': 'slider',
                'min': 1, 'max': 10, 'default': 5,
                'pattern': 'readiness', 'weight': 'low', 'clinical': 'therapy_confidence'
            },
            55: {
                'text': 'What outcome would make this investment completely worthwhile for you?',
                'type': 'text',
                'placeholder': 'Describe the specific change or outcome that would make this completely successful...',
                'pattern': 'preferences', 'weight': 'low', 'clinical': 'success_criteria'
            }
        }
    
    def _get_pattern_mapping(self):
        """Map questions to patterns for clinical analysis"""
        mapping = {}
        for q_num, q_data in self.questions.items():
            pattern = q_data.get('pattern')
            weight = q_data.get('weight', 'low')
            if pattern != 'readiness' and pattern != 'preferences' and pattern != 'all':
                if pattern not in mapping:
                    mapping[pattern] = []
                mapping[pattern].append({
                    'question': q_num,
                    'weight': weight,
                    'clinical': q_data.get('clinical', None)
                })
        return mapping
    
    def render(self):
        """Render the complete assessment page"""
        self._render_header()
        
        if not st.session_state.contact_provided:
            if st.session_state.current_question <= self.total_questions:
                self._render_progress()
                self._render_current_question()
                self._render_navigation()
            else:
                self._render_contact_form()
        else:
            self._render_results()
    
    def _render_header(self):
        """Render assessment header with clear value proposition"""
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0 2rem 0;">
            <h1>Comprehensive Behavioral Pattern Assessment</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin: 0 auto;">
                This detailed assessment maps your unique behavioral patterns to design the most effective 
                hypnotherapy approach for your transformation. Your responses create a clinical template 
                that guides your personalized session strategy.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Assessment value explanation
        st.info("""
        **Why this assessment matters:** Traditional hypnotherapy uses generic scripts. 
        This comprehensive evaluation identifies your specific patterns, triggers, and readiness factors 
        to create a targeted approach that works with your unique psychological landscape.
        """)
    
    def _render_progress(self):
        """Render progress indicator"""
        current = st.session_state.current_question
        progress = (current - 1) / self.total_questions
        
        # Determine current section
        if current <= 25:
            section = 1
            section_progress = current / 25
        elif current <= 40:
            section = 2
            section_progress = (current - 25) / 15
        else:
            section = 3
            section_progress = (current - 40) / 15
        
        st.progress(progress)
        st.caption(f"Question {current} of {self.total_questions} • Section {section}: {self.sections[section]['name']}")
    
    def _render_current_question(self):
        """Render current question with appropriate input type"""
        current = st.session_state.current_question
        
        if current <= self.total_questions:
            question = self.questions[current]
            self._render_question(question, current)
    
    def _render_question(self, question, q_num):
        """Render individual question based on type"""
        st.markdown(f"### {question['text']}")
        
        # Store response key
        response_key = f"q_{q_num}"
        
        if question['type'] == 'radio':
            response = st.radio(
                f"Select your response:",
                question['options'],
                key=response_key,
                index=None
            )
            
            if response and st.button("Next Question", type="primary", key=f"next_{q_num}"):
                self._save_response(q_num, response)
                self._advance_question()
                
        elif question['type'] == 'slider':
            response = st.slider(
                f"Rate from {question['min']} to {question['max']}:",
                question['min'],
                question['max'],
                question['default'],
                key=response_key
            )
            
            if st.button("Next Question", type="primary", key=f"next_{q_num}"):
                self._save_response(q_num, response)
                self._advance_question()
                
        elif question['type'] == 'text':
            response = st.text_area(
                "Your response:",
                placeholder=question['placeholder'],
                key=response_key,
                height=100
            )
            
            if response.strip() and st.button("Next Question", type="primary", key=f"next_{q_num}"):
                self._save_response(q_num, response.strip())
                self._advance_question()
            elif not response.strip():
                st.info("Please provide your response to continue.")
    
    def _render_contact_form(self):
        """Render contact form after completing all questions"""
        st.markdown("### Assessment Complete - Get Your Results")
        st.write("Provide your contact details to receive your comprehensive behavioral pattern analysis and personalized transformation recommendations.")
        
        with st.form("assessment_contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name*", placeholder="Your full name")
                email = st.text_input("Email Address*", placeholder="your@email.com")
            
            with col2:
                phone = st.text_input("Phone (Optional)", placeholder="+66 xxx xxx xxx")
                urgency = st.selectbox(
                    "How urgent is addressing your main concern?",
                    ["Select urgency level...", "Extremely urgent", "Very urgent", "Moderately urgent", "Not urgent"]
                )
            
            primary_concern = st.text_area(
                "Primary Concern*",
                placeholder="What specific issue brought you to this assessment? Be as detailed as you'd like.",
                height=100
            )
            
            session_preference = st.selectbox(
                "Preferred next step:",
                ["Select preference...", "Schedule discovery call to discuss results", "Book transformation package directly", "Request detailed written analysis first"]
            )
            
            submitted = st.form_submit_button("Complete Assessment & Send Results", type="primary")
            
            if submitted:
                if self._validate_contact_form(name, email, primary_concern, urgency, session_preference):
                    self._save_contact_info(name, email, phone, urgency, primary_concern, session_preference)
                    self._complete_assessment()
                    st.session_state.contact_provided = True
                    st.rerun()
    
    def _render_navigation(self):
        """Render navigation buttons"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.session_state.current_question > 1:
                if st.button("← Previous", key="prev_btn"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        with col3:
            if st.button("Save Progress", key="save_btn"):
                st.success("Progress saved! You can return anytime to complete the assessment.")
    
    def _render_results(self):
        """Render comprehensive assessment results"""
        st.markdown("## Assessment Analysis Complete")
        st.success("Your comprehensive behavioral pattern analysis has been completed and sent to our clinical team for detailed review.")
        
        # Show summary metrics
        self._render_results_summary()
        
        # Show readiness assessment
        self._render_readiness_analysis()
        
        # Show next steps
        self._render_next_steps()
    
    def _render_results_summary(self):
        """Render results summary"""
        st.markdown("### Your Assessment Summary")
        
        # Calculate completion metrics
        total_responses = len(st.session_state.assessment_responses)
        readiness_scores = self._calculate_readiness_metrics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Questions Completed", f"{total_responses}/{self.total_questions}", "Comprehensive analysis")
        
        with col2:
            avg_readiness = sum(readiness_scores.values()) / len(readiness_scores) if readiness_scores else 5
            st.metric("Overall Readiness", f"{avg_readiness:.1f}/10", "For transformation")
        
        with col3:
            completion_time = "30-35 minutes"
            st.metric("Assessment Depth", completion_time, "Thorough evaluation")
    
    def _render_readiness_analysis(self):
        """Render readiness analysis"""
        st.markdown("### Transformation Readiness Analysis")
        
        readiness_scores = self._calculate_readiness_metrics()
        
        if readiness_scores.get('motivation_level', 5) >= 7:
            st.success("High motivation level indicates excellent potential for rapid transformation.")
        elif readiness_scores.get('motivation_level', 5) >= 5:
            st.info("Good motivation level shows solid readiness for the transformation process.")
        else:
            st.warning("Lower motivation suggests a discovery call would help clarify the best approach.")
        
        # Show clinical priorities based on responses
        clinical_insights = self._extract_clinical_insights()
        if clinical_insights:
            with st.expander("Clinical Analysis Preview"):
                for insight_type, insight_data in clinical_insights.items():
                    if insight_data:
                        st.write(f"**{insight_type.replace('_', ' ').title()}:** {insight_data}")
    
    def _render_next_steps(self):
        """Render next steps based on assessment"""
        st.markdown("### Your Personalized Next Steps")
        
        # Get session preference from contact form
        contact_info = st.session_state.assessment_responses.get('contact_info', {})
        preference = contact_info.get('session_preference', '')
        
        if 'discovery call' in preference.lower():
            st.info("Based on your preference, we'll contact you to schedule a discovery call to discuss your results in detail.")
        elif 'package directly' in preference.lower():
            st.success("You've indicated readiness for the transformation package. We'll contact you with scheduling options.")
        elif 'written analysis' in preference.lower():
            st.info("You'll receive a detailed written analysis within 24 hours, followed by a consultation offer.")
        else:
            st.info("We'll review your assessment and contact you with personalized recommendations.")
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical Review** (Within 24 hours): Your responses are analyzed to identify your primary patterns and optimal treatment approach
        2. **Personalized Contact** (Within 48 hours): We'll reach out with specific recommendations based on your assessment
        3. **Discovery Call** (Optional): Discuss your results and answer questions about the process
        4. **Transformation Sessions**: Begin your personalized rapid pattern rewiring program
        """)
        
        # CTA for immediate booking
        st.markdown("### Ready to Take Action?")
        st.write("Don't wait for our contact - you can schedule your discovery call immediately to discuss your assessment results.")
        
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1.1rem;">
                Schedule Your Discovery Call Now
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    def _save_response(self, question_num, response):
        """Save question response to session state"""
        st.session_state.assessment_responses[f'q_{question_num}'] = {
            'response': response,
            'question_text': self.questions[question_num]['text'],
            'pattern': self.questions[question_num].get('pattern'),
            'weight': self.questions[question_num].get('weight'),
            'clinical': self.questions[question_num].get('clinical'),
            'timestamp': datetime.now().isoformat()
        }
    
    def _save_contact_info(self, name, email, phone, urgency, concern, preference):
        """Save contact information"""
        st.session_state.assessment_responses['contact_info'] = {
            'name': name,
            'email': email,
            'phone': phone,
            'urgency': urgency,
            'primary_concern': concern,
            'session_preference': preference,
            'timestamp': datetime.now().isoformat()
        }
    
    def _advance_question(self):
        """Advance to next question"""
        st.session_state.current_question += 1
        st.rerun()
    
    def _validate_contact_form(self, name, email, concern, urgency, preference):
        """Validate contact form inputs"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        
        if not email.strip():
            errors.append("Email is required")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
            errors.append("Please enter a valid email address")
        
        if not concern.strip():
            errors.append("Primary concern is required")
        
        if urgency == "Select urgency level...":
            errors.append("Please select your urgency level")
        
        if preference == "Select preference...":
            errors.append("Please select your preferred next step")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _complete_assessment(self):
        """Process completed assessment and send results"""
        try:
            # Calculate pattern scores
            pattern_scores = self._calculate_pattern_scores()
            
            # Extract clinical insights
            clinical_insights = self._extract_clinical_insights()
            
            # Calculate readiness metrics
            readiness_metrics = self._calculate_readiness_metrics()
            
            # Store results
            st.session_state.assessment_results = {
                'pattern_scores': pattern_scores,
                'clinical_insights': clinical_insights,
                'readiness_metrics': readiness_metrics,
                'completion_timestamp': datetime.now().isoformat()
            }
            
            # Send comprehensive email
            self._send_assessment_email()
            
        except Exception as e:
            st.error(f"Error processing assessment: {str(e)}")
    
    def _calculate_pattern_scores(self):
        """Calculate weighted scores for each behavioral pattern"""
        pattern_scores = {pattern_id: 0 for pattern_id in self.patterns.keys()}
        
        for response_key, response_data in st.session_state.assessment_responses.items():
            if response_key.startswith('q_'):
                pattern = response_data.get('pattern')
                weight = response_data.get('weight', 'low')
                response = response_data.get('response')
                
                if pattern in pattern_scores and response:
                    # Weight multiplier
                    weight_multiplier = self.question_weights.get(weight, 1)
                    
                    # Score based on response type
                    if isinstance(response, str) and len(response) > 10:  # Text responses
                        pattern_scores[pattern] += weight_multiplier
                    elif isinstance(response, (int, float)):  # Slider responses
                        if response >= 6:
                            pattern_scores[pattern] += weight_multiplier
                    elif isinstance(response, str):  # Radio responses
                        # First option is typically the healthy response
                        question_num = int(response_key.split('_')[1])
                        question = self.questions[question_num]
                        if 'options' in question:
                            try:
                                response_index = question['options'].index(response)
                                if response_index > 0:  # Not the first (healthy) option
                                    pattern_scores[pattern] += weight_multiplier
                            except ValueError:
                                pass
        
        return pattern_scores
    
    def _extract_clinical_insights(self):
        """Extract key clinical insights from responses"""
        insights = {}
        
        for response_key, response_data in st.session_state.assessment_responses.items():
            clinical_type = response_data.get('clinical')
            response = response_data.get('response')
            
            if clinical_type and response:
                insights[clinical_type] = response
        
        return insights
    
    def _calculate_readiness_metrics(self):
        """Calculate transformation readiness metrics"""
        readiness_metrics = {}
        
        # Extract specific readiness responses
        readiness_questions = {
            'urgency_level': 41,
            'motivation_level': 42,
            'commitment_level': 43,
            'rapid_change_belief': 45,
            'emotional_readiness': 49,
            'therapy_confidence': 54
        }
        
        for metric, question_num in readiness_questions.items():
            response_key = f'q_{question_num}'
            if response_key in st.session_state.assessment_responses:
                response = st.session_state.assessment_responses[response_key]['response']
                
                if isinstance(response, (int, float)):
                    readiness_metrics[metric] = response
                elif isinstance(response, str):
                    # Convert text responses to numeric scale
                    if 'extremely' in response.lower() or 'unlimited' in response.lower():
                        readiness_metrics[metric] = 10
                    elif 'quite' in response.lower() or 'high' in response.lower():
                        readiness_metrics[metric] = 8
                    elif 'moderate' in response.lower():
                        readiness_metrics[metric] = 6
                    elif 'somewhat' in response.lower() or 'limited' in response.lower():
                        readiness_metrics[metric] = 4
                    else:
                        readiness_metrics[metric] = 2
        
        return readiness_metrics
    
    def _send_assessment_email(self):
        """Send comprehensive assessment results via email"""
        try:
            from utils.email_handler import send_discovery_call_email
            
            # Get contact info
            contact_info = st.session_state.assessment_responses.get('contact_info', {})
            
            # Prepare comprehensive assessment data
            assessment_data = {
                'name': contact_info.get('name', 'Unknown'),
                'email': contact_info.get('email', 'Unknown'),
                'phone': contact_info.get('phone', 'Not provided'),
                'concern': contact_info.get('primary_concern', 'Comprehensive Assessment'),
                'urgency': contact_info.get('urgency', 'Not specified'),
                'session_preference': contact_info.get('session_preference', 'Not specified'),
                'form_type': 'Complete Behavioral Pattern Assessment',
                'source': 'Assessment Page',
                'total_questions': self.total_questions,
                'completion_rate': '100%',
                'assessment_results': st.session_state.assessment_results,
                'raw_responses': st.session_state.assessment_responses,
                'clinical_template': self._generate_clinical_template(),
                'timestamp': datetime.now().isoformat()
            }
            
            # Send email
            success = send_discovery_call_email(assessment_data)
            
            if success:
                st.success("✅ Assessment results sent successfully to our clinical team!")
            else:
                st.warning("⚠️ Assessment completed, but email notification failed. We have your responses saved.")
                
        except Exception as e:
            st.error(f"Error sending assessment results: {str(e)}")
    
    def _generate_clinical_template(self):
        """Generate comprehensive clinical template for therapist"""
        template = []
        
        # Header
        template.append("COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT - CLINICAL TEMPLATE")
        template.append("=" * 70)
        template.append(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        template.append(f"Total Questions: {self.total_questions}")
        template.append("")
        
        # Contact & Urgency Info
        contact_info = st.session_state.assessment_responses.get('contact_info', {})
        template.append("CLIENT INFORMATION:")
        template.append(f"Name: {contact_info.get('name', 'Not provided')}")
        template.append(f"Email: {contact_info.get('email', 'Not provided')}")
        template.append(f"Phone: {contact_info.get('phone', 'Not provided')}")
        template.append(f"Urgency Level: {contact_info.get('urgency', 'Not specified')}")
        template.append(f"Primary Concern: {contact_info.get('primary_concern', 'Not provided')}")
        template.append(f"Preferred Next Step: {contact_info.get('session_preference', 'Not specified')}")
        template.append("")
        
        # Pattern Analysis
        pattern_scores = st.session_state.assessment_results.get('pattern_scores', {})
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        template.append("BEHAVIORAL PATTERN ANALYSIS:")
        template.append("Primary Therapeutic Targets (Highest Activation):")
        for pattern_id, score in sorted_patterns[:3]:
            pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
            template.append(f"- {pattern_name}: Activation Level {score}")
        template.append("")
        
        # Clinical Insights
        clinical_insights = st.session_state.assessment_results.get('clinical_insights', {})
        if clinical_insights:
            template.append("KEY CLINICAL INSIGHTS:")
            for insight_type, insight_data in clinical_insights.items():
                template.append(f"- {insight_type.replace('_', ' ').title()}: {insight_data}")
            template.append("")
        
        # Readiness Assessment
        readiness_metrics = st.session_state.assessment_results.get('readiness_metrics', {})
        if readiness_metrics:
            template.append("TRANSFORMATION READINESS METRICS:")
            for metric, score in readiness_metrics.items():
                template.append(f"- {metric.replace('_', ' ').title()}: {score}/10")
            template.append("")
        
        # Session Recommendations
        template.append("RECOMMENDED SESSION APPROACH:")
        primary_pattern = sorted_patterns[0][0] if sorted_patterns else 1
        secondary_pattern = sorted_patterns[1][0] if len(sorted_patterns) > 1 else 2
        
        template.append(f"Session 1: Map {self.patterns[primary_pattern]} and {self.patterns[secondary_pattern]} patterns")
        template.append(f"Session 2: Neural rewiring targeting {self.patterns[primary_pattern]}")
        template.append("Session 3: Reinforcement if needed (assess after Session 2)")
        template.append("")
        
        # Communication Preferences
        comm_style = clinical_insights.get('communication_style', 'Not specified')
        learning_style = clinical_insights.get('learning_style', 'Not specified')
        template.append("THERAPEUTIC COMMUNICATION NOTES:")
        template.append(f"Preferred Communication Style: {comm_style}")
        template.append(f"Learning Style: {learning_style}")
        template.append("")
        
        return "\n".join(template)


class AssessPage:
    """Main assessment page component"""
    
    def __init__(self):
        self.assessment = BehavioralPatternAssessment()
    
    def render(self):
        """Render the complete assessment page"""
        self.assessment.render()


# Factory function for clean import
def create_assess_page():
    """Factory function to create AssessPage instance"""
    return AssessPage()
