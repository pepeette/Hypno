# """
# Complete Behavioral Pattern Assessment Page
# 3-section comprehensive assessment with clinical mapping and email integration
# 55 total questions across core patterns, clinical insights, and transformation readiness
# """
# import streamlit as st
# from datetime import datetime
# import re
# try:
#     from components.paywall import create_clinical_paywall
#     PAYWALL_AVAILABLE = True
# except ImportError:
#     PAYWALL_AVAILABLE = False
#     print("Paywall component not available")

# class BehavioralPatternAssessment:
#     """Comprehensive 55-question behavioral pattern assessment"""
    
#     def __init__(self):
#         # Initialize session state
#         self._init_session_state()
        
#         # Assessment structure
#         self.sections = {
#             1: {"name": "Core Behavioral Patterns", "questions": 25},
#             2: {"name": "Clinical Insights & Triggers", "questions": 15}, 
#             3: {"name": "Transformation Readiness", "questions": 15}
#         }
        
#         self.total_questions = 55
        
#         # Pattern definitions for clinical mapping
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
        
#         # Question weights for clinical priority
#         self.question_weights = {
#             'high': 3,    # Critical therapeutic targets
#             'medium': 2,  # Important patterns
#             'low': 1      # Supporting insights
#         }
        
#         # All 55 questions organized by section
#         self.questions = self._get_all_questions()
        
#         # Clinical mapping for pattern scoring
#         self.pattern_mapping = self._get_pattern_mapping()
    
#     def _init_session_state(self):
#         """Initialize session state variables"""
#         if 'assessment_responses' not in st.session_state:
#             st.session_state.assessment_responses = {}
#         if 'current_question' not in st.session_state:
#             st.session_state.current_question = 1
#         if 'assessment_completed' not in st.session_state:
#             st.session_state.assessment_completed = False
#         if 'contact_provided' not in st.session_state:
#             st.session_state.contact_provided = False
#         if 'assessment_results' not in st.session_state:
#             st.session_state.assessment_results = {}
    
#     def _get_all_questions(self):
#         """Return all 55 questions organized by section"""
#         return {
#             # SECTION 1: CORE BEHAVIORAL PATTERNS (25 questions)
#             1: {
#                 'text': 'When something genuinely wonderful happens to you, within 60 seconds you typically:',
#                 'type': 'radio',
#                 'options': [
#                     "Feel genuine joy and want to celebrate",
#                     'Think "this won\'t last" or "what\'s the catch?"',
#                     "Feel guilty, like you don't deserve it", 
#                     "Immediately worry about what bad thing will happen to balance it",
#                     "Try to downplay it so others don't feel bad"
#                 ],
#                 'pattern': 1, 'weight': 'high'
#             },
#             2: {
#                 'text': 'When someone disagrees with you or challenges your position, your body:',
#                 'type': 'radio',
#                 'options': [
#                     "Stays relatively calm and curious",
#                     "Tenses up immediately, ready to fight",
#                     "Gets hot, heart races, adrenaline surges", 
#                     "Shuts down, goes numb, wants to flee",
#                     "Feels attacked, even if they're being respectful"
#                 ],
#                 'pattern': 2, 'weight': 'high'
#             },
#             3: {
#                 'text': 'Your default assumption about new people\'s intentions toward you:',
#                 'type': 'radio',
#                 'options': [
#                     "Most people are generally well-meaning",
#                     "They're probably judging me negatively",
#                     "They want to use or manipulate me somehow",
#                     "They'll reject me when they see my flaws",
#                     "They have hidden agendas I need to figure out"
#                 ],
#                 'pattern': 3, 'weight': 'high'
#             },
#             4: {
#                 'text': 'When facing important life choices, you typically:',
#                 'type': 'radio',
#                 'options': [
#                     "Look for creative solutions that honor multiple values",
#                     "Feel trapped between impossible either/or options",
#                     "See only two extreme alternatives",
#                     "Get paralyzed by black-and-white thinking", 
#                     "Feel like you can't have what you really want"
#                 ],
#                 'pattern': 4, 'weight': 'high'
#             },
#             5: {
#                 'text': 'Complete this honestly: "I am valuable when I..."',
#                 'type': 'radio',
#                 'options': [
#                     "Simply exist as I am",
#                     "Accomplish something important",
#                     "Help or please other people",
#                     "Prove my worth through performance",
#                     "Stay busy and productive"
#                 ],
#                 'pattern': 5, 'weight': 'high'
#             },
#             6: {
#                 'text': 'Your personality or behavior significantly changes based on:',
#                 'type': 'radio',
#                 'options': [
#                     "It stays pretty consistent across all contexts",
#                     "Which group of people you're with",
#                     "Professional versus personal settings",
#                     "Whether you're in control or following others",
#                     "If you're the expert or the newcomer"
#                 ],
#                 'pattern': 6, 'weight': 'high'
#             },
#             7: {
#                 'text': 'When it comes to your own health, fitness, or wellbeing:',
#                 'type': 'radio',
#                 'options': [
#                     "I naturally prioritize my wellbeing alongside others'",
#                     "I know what to do but can't make myself do it",
#                     "I care for everyone else first, then there's no energy left",
#                     "I feel selfish focusing on my own needs",
#                     "I'm great at advising others but terrible at following my own advice"
#                 ],
#                 'pattern': 7, 'weight': 'high'
#             },
#             8: {
#                 'text': 'Your major life goals (career, lifestyle, achievements) are primarily:',
#                 'type': 'radio',
#                 'options': [
#                     "Genuinely what you desire for your own life",
#                     "What your family expected or dreamed for you",
#                     "Honoring someone who died or sacrificed for you",
#                     "Proving you're worthy of someone's love or sacrifice",
#                     "What you think you 'should' want based on your background"
#                 ],
#                 'pattern': 8, 'weight': 'high'
#             },
#             9: {
#                 'text': 'With your closest friends or certain social groups, you:',
#                 'type': 'radio',
#                 'options': [
#                     "Stay true to your values and boundaries",
#                     "Become someone you don't respect or recognize",
#                     "Lose all your usual boundaries and standards",
#                     "Act against your stated values and beliefs",
#                     "Can't say no even when you desperately want to"
#                 ],
#                 'pattern': 9, 'weight': 'high'
#             },
#             10: {
#                 'text': 'Rate your agreement: "I feel guilty when things are going too well"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 1, 'weight': 'medium'
#             },
#             11: {
#                 'text': 'During a disagreement, you\'re most likely to:',
#                 'type': 'radio',
#                 'options': [
#                     "Listen to understand their perspective",
#                     "Attack their position aggressively",
#                     "Withdraw and shut down emotionally",
#                     "Manipulate the situation to get your way",
#                     "Submit externally but feel resentful internally"
#                 ],
#                 'pattern': 2, 'weight': 'medium'
#             },
#             12: {
#                 'text': 'When you enter a room of strangers, you automatically think:',
#                 'type': 'radio',
#                 'options': [
#                     "These seem like interesting people to meet",
#                     "They're probably thinking something critical about me",
#                     "I don't belong here",
#                     "I need to figure out the social dynamics quickly",
#                     "I hope I can get through this without embarrassing myself"
#                 ],
#                 'pattern': 3, 'weight': 'medium'
#             },
#             13: {
#                 'text': 'Complete this sentence: "In life, I have to choose between security _____ freedom"',
#                 'type': 'radio',
#                 'options': [
#                     "AND (I can have both)",
#                     "OR (I must choose one)",
#                     "This sentence doesn't resonate with me",
#                     "I've never thought about it this way",
#                     "Both seem impossible to achieve"
#                 ],
#                 'pattern': 4, 'weight': 'medium'
#             },
#             14: {
#                 'text': 'Rate your agreement: "My worth depends on what I achieve"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 5, 'weight': 'medium'
#             },
#             15: {
#                 'text': 'There are areas of your life where you feel completely capable, and others where you feel powerless:',
#                 'type': 'radio',
#                 'options': [
#                     "No, I feel consistently myself everywhere",
#                     "Yes - I'm like two completely different people",
#                     "I'm strong professionally but weak personally",
#                     "I'm confident socially but insecure privately",
#                     "I lead some groups but follow others completely"
#                 ],
#                 'pattern': 6, 'weight': 'medium'
#             },
#             16: {
#                 'text': 'You consistently have energy and motivation for:',
#                 'type': 'radio',
#                 'options': [
#                     "Both personal and external responsibilities equally",
#                     "Other people's goals but not your own",
#                     "Work projects but not personal care",
#                     "Helping others but not helping yourself",
#                     "Everything except what your body needs"
#                 ],
#                 'pattern': 7, 'weight': 'medium'
#             },
#             17: {
#                 'text': 'When you think about what YOU actually want (separate from all expectations):',
#                 'type': 'radio',
#                 'options': [
#                     "You can access it clearly and confidently",
#                     "You honestly don't know anymore",
#                     "You feel guilty for wanting something different",
#                     "You feel like you'd be betraying someone important",
#                     "You're afraid it's not worthy or important enough"
#                 ],
#                 'pattern': 8, 'weight': 'medium'
#             },
#             18: {
#                 'text': 'There are specific people around whom you consistently make choices you later regret:',
#                 'type': 'radio',
#                 'options': [
#                     "No, I make similar choices regardless of who's around",
#                     "Yes, and I know who they are but can't seem to stop",
#                     "I become weak-willed around certain personality types",
#                     "I desperately want their approval and will do anything for it",
#                     "I'm afraid of conflict so I go along with things I hate"
#                 ],
#                 'pattern': 9, 'weight': 'medium'
#             },
#             19: {
#                 'text': 'When you\'re on the verge of achieving something important, you often:',
#                 'type': 'radio',
#                 'options': [
#                     "Feel excited and push through to completion",
#                     "Find ways to sabotage or delay it",
#                     "Become overwhelmed and want to quit",
#                     "Start focusing on everything that could go wrong",
#                     "Feel like you don't deserve to succeed"
#                 ],
#                 'pattern': 1, 'weight': 'medium'
#             },
#             20: {
#                 'text': 'Rate your agreement: "Being right is more important than being connected"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 2, 'weight': 'low'
#             },
#             21: {
#                 'text': 'Rate your agreement: "If people really knew me, they\'d reject me"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 3, 'weight': 'low'
#             },
#             22: {
#                 'text': 'Rate your agreement: "I often feel like I don\'t fit anywhere"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 4, 'weight': 'low'
#             },
#             23: {
#                 'text': 'When your efforts go completely unnoticed or unappreciated:',
#                 'type': 'radio',
#                 'options': [
#                     "You know your worth isn't dependent on external recognition",
#                     "You feel invisible and unimportant",
#                     "You work even harder to get attention",
#                     "You question whether what you did actually mattered",
#                     "You feel resentful and want to stop trying"
#                 ],
#                 'pattern': 5, 'weight': 'low'
#             },
#             24: {
#                 'text': 'Rate your agreement: "I have different versions of myself for different audiences"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 6, 'weight': 'low'
#             },
#             25: {
#                 'text': 'When you think about doing something purely for your own pleasure or health:',
#                 'type': 'radio',
#                 'options': [
#                     "You can do it without internal conflict",
#                     "You feel guilty and selfish",
#                     "You find excuses to avoid it",
#                     "You start but don't follow through",
#                     "You sabotage it somehow"
#                 ],
#                 'pattern': 7, 'weight': 'low'
#             },
            
#             # SECTION 2: CLINICAL INSIGHTS & TRIGGERS (15 questions)
#             26: {
#                 'text': 'Growing up, which phrase did you hear most often?',
#                 'type': 'radio',
#                 'options': [
#                     "You can achieve anything you set your mind to",
#                     "Life is tough, get used to it",
#                     "Don't get your hopes up",
#                     "We're not here to have fun",
#                     "Good things happen to other people, not us"
#                 ],
#                 'pattern': 1, 'weight': 'high', 'clinical': 'family_origin'
#             },
#             27: {
#                 'text': 'What does your current problem/pattern give you that you\'re not supposed to want?',
#                 'type': 'radio',
#                 'options': [
#                     "I can't think of any hidden benefits",
#                     "Permission to avoid bigger challenges or responsibilities",
#                     "Attention, care, and sympathy from others",
#                     "An excuse for not reaching my full potential",
#                     "Control over situations and other people's behavior"
#                 ],
#                 'pattern': 'all', 'weight': 'high', 'clinical': 'secondary_gain'
#             },
#             28: {
#                 'text': 'Complete this sentence: "People like me don\'t get to have..."',
#                 'type': 'text',
#                 'placeholder': 'Complete the sentence with what first comes to mind...',
#                 'pattern': 'all', 'weight': 'high', 'clinical': 'limiting_belief'
#             },
#             29: {
#                 'text': 'What scares you most about completely solving your main problem?',
#                 'type': 'radio',
#                 'options': [
#                     "Nothing really scares me about solving it",
#                     "I wouldn't know who I am anymore",
#                     "People might expect too much from me",
#                     "I might lose connections with others who struggle similarly",
#                     "I'd have to take full responsibility for my life and happiness"
#                 ],
#                 'pattern': 'all', 'weight': 'high', 'clinical': 'change_fear'
#             },
#             30: {
#                 'text': 'Rate your willingness to question beliefs you\'ve held since childhood',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 'all', 'weight': 'medium', 'clinical': 'cognitive_flexibility'
#             },
#             31: {
#                 'text': 'When someone offers you genuine help or shows you kindness:',
#                 'type': 'radio',
#                 'options': [
#                     "You can receive it gracefully",
#                     "You immediately wonder what they want in return",
#                     "You feel uncomfortable and try to reciprocate immediately",
#                     "You assume they pity you or see you as weak",
#                     "You worry about owing them something"
#                 ],
#                 'pattern': 3, 'weight': 'medium', 'clinical': 'trust_capacity'
#             },
#             32: {
#                 'text': 'Your current life path feels:',
#                 'type': 'radio',
#                 'options': [
#                     "Like it genuinely reflects who you are",
#                     "Like fulfilling someone else's dreams",
#                     "Like honoring a debt you owe",
#                     "Like the 'right' thing but not the authentic thing",
#                     "Like you're afraid to choose differently"
#                 ],
#                 'pattern': 8, 'weight': 'medium', 'clinical': 'authenticity_gap'
#             },
#             33: {
#                 'text': 'In situations where there\'s social pressure to do something you don\'t want to do:',
#                 'type': 'radio',
#                 'options': [
#                     "You can say no clearly and maintain your boundaries",
#                     "You go along to avoid conflict or rejection",
#                     "You feel paralyzed and unable to speak up",
#                     "You do it but feel resentful and angry afterward",
#                     "You convince yourself you actually want to do it"
#                 ],
#                 'pattern': 9, 'weight': 'medium', 'clinical': 'boundary_strength'
#             },
#             34: {
#                 'text': 'Rate your agreement: "I would disappoint or abandon someone important if I lived my true desires"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 8, 'weight': 'medium', 'clinical': 'loyalty_conflict'
#             },
#             35: {
#                 'text': 'When someone genuinely compliments you, you:',
#                 'type': 'radio',
#                 'options': [
#                     'Say "thank you" and feel good about it',
#                     "Deflect or minimize it immediately",
#                     "Feel suspicious of their motives",
#                     "Immediately point out your flaws",
#                     "Feel uncomfortable and change the subject"
#                 ],
#                 'pattern': 1, 'weight': 'low', 'clinical': 'self_worth'
#             },
#             36: {
#                 'text': 'Complete this: "Taking care of myself means I\'m..."',
#                 'type': 'radio',
#                 'options': [
#                     "Being responsible and setting a good example",
#                     "Being selfish and taking away from others",
#                     "Not working hard enough on important things",
#                     "Wasting time I should spend being productive",
#                     "Being weak or self-indulgent"
#                 ],
#                 'pattern': 7, 'weight': 'low', 'clinical': 'self_care_beliefs'
#             },
#             37: {
#                 'text': 'Your energy distribution typically follows this pattern:',
#                 'type': 'radio',
#                 'options': [
#                     "Balanced between self-care and caring for others",
#                     "80% for others, 20% for self",
#                     "90% for others, 10% for self",
#                     "100% for others until burnout, then collapse",
#                     "Varies wildly with no consistent pattern"
#                 ],
#                 'pattern': 7, 'weight': 'low', 'clinical': 'energy_allocation'
#             },
#             38: {
#                 'text': 'If you completely followed your authentic desires, which relationship would be most threatened:',
#                 'type': 'radio',
#                 'options': [
#                     "None - my relationships would likely improve",
#                     "With parents who sacrificed for specific dreams",
#                     "With the memory/legacy of someone who died",
#                     "With family members who define success differently",
#                     "With a community that has certain expectations"
#                 ],
#                 'pattern': 8, 'weight': 'low', 'clinical': 'relationship_threats'
#             },
#             39: {
#                 'text': 'When you\'re with people whose approval you crave:',
#                 'type': 'radio',
#                 'options': [
#                     "You maintain your authentic self",
#                     "You become someone completely different",
#                     "You lose access to your own preferences and opinions",
#                     "You do things that violate your core values",
#                     "You feel powerless to make different choices"
#                 ],
#                 'pattern': 9, 'weight': 'low', 'clinical': 'approval_seeking'
#             },
#             40: {
#                 'text': 'Rate your agreement: "I\'m much stronger in some relationships than others"',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 9, 'weight': 'low', 'clinical': 'relationship_consistency'
#             },
            
#             # SECTION 3: TRANSFORMATION READINESS (15 questions)
#             41: {
#                 'text': 'How urgently do you need to resolve your main concern?',
#                 'type': 'radio',
#                 'options': [
#                     "Extremely urgent - affecting my daily life significantly",
#                     "Quite urgent - I need change within the next few months",
#                     "Moderately urgent - would like change within 6 months",
#                     "Somewhat urgent - exploring options for gradual change",
#                     "Not urgent - just curious about possibilities"
#                 ],
#                 'pattern': 'readiness', 'weight': 'high', 'clinical': 'urgency_level'
#             },
#             42: {
#                 'text': 'Rate your current motivation level to make significant changes (1=no motivation, 10=extremely motivated)',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 'readiness', 'weight': 'high', 'clinical': 'motivation_level'
#             },
#             43: {
#                 'text': 'How much time and energy can you realistically commit to transformation work?',
#                 'type': 'radio',
#                 'options': [
#                     "Unlimited - this is my top priority right now",
#                     "High commitment - can prioritize this significantly",
#                     "Moderate commitment - can fit it into my schedule",
#                     "Limited commitment - very busy but can make some time",
#                     "Minimal commitment - extremely limited availability"
#                 ],
#                 'pattern': 'readiness', 'weight': 'high', 'clinical': 'commitment_level'
#             },
#             44: {
#                 'text': 'Your experience with personal development or therapy:',
#                 'type': 'radio',
#                 'options': [
#                     "Extensive experience with multiple approaches",
#                     "Some experience - tried a few different methods",
#                     "Limited experience - one or two attempts",
#                     "No formal experience but read/researched extensively",
#                     "Complete beginner to personal development work"
#                 ],
#                 'pattern': 'readiness', 'weight': 'medium', 'clinical': 'experience_level'
#             },
#             45: {
#                 'text': 'Rate your belief that rapid change (2-3 sessions) is possible for your situation',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 'readiness', 'weight': 'medium', 'clinical': 'rapid_change_belief'
#             },
#             46: {
#                 'text': 'Your preferred communication style during sessions:',
#                 'type': 'radio',
#                 'options': [
#                     "Direct and analytical - I want to understand everything",
#                     "Gentle and supportive - I need a lot of encouragement",
#                     "Practical and solution-focused - just tell me what to do",
#                     "Exploratory and intuitive - let's see what emerges",
#                     "Collaborative - I want to be an active partner in the process"
#                 ],
#                 'pattern': 'preferences', 'weight': 'medium', 'clinical': 'communication_style'
#             },
#             47: {
#                 'text': 'Your biggest concern about starting hypnotherapy:',
#                 'type': 'radio',
#                 'options': [
#                     "I have no significant concerns - I'm ready to begin",
#                     "Worried about losing control or being manipulated",
#                     "Concerned it won't work for my specific situation",
#                     "Skeptical about the science/effectiveness of hypnosis",
#                     "Worried about what I might discover about myself"
#                 ],
#                 'pattern': 'preferences', 'weight': 'medium', 'clinical': 'therapy_concerns'
#             },
#             48: {
#                 'text': 'Your learning style preference:',
#                 'type': 'radio',
#                 'options': [
#                     "Visual - I need to see diagrams, models, or written explanations",
#                     "Auditory - I learn best through listening and discussion",
#                     "Kinesthetic - I need to experience and practice things physically",
#                     "Analytical - I need logical explanations and step-by-step processes",
#                     "Intuitive - I prefer to feel my way through and trust instincts"
#                 ],
#                 'pattern': 'preferences', 'weight': 'low', 'clinical': 'learning_style'
#             },
#             49: {
#                 'text': 'Rate your comfort level with exploring potentially uncomfortable emotions or memories',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 'readiness', 'weight': 'low', 'clinical': 'emotional_readiness'
#             },
#             50: {
#                 'text': 'Your support system for making changes:',
#                 'type': 'radio',
#                 'options': [
#                     "Very strong - family/friends actively support my growth",
#                     "Generally supportive - they want what's best for me",
#                     "Mixed - some support, some resistance to change",
#                     "Limited support - mostly indifferent to my changes",
#                     "Potentially hostile - others might resist my transformation"
#                 ],
#                 'pattern': 'readiness', 'weight': 'low', 'clinical': 'support_system'
#             },
#             51: {
#                 'text': 'Your financial investment comfort level for transformation work:',
#                 'type': 'radio',
#                 'options': [
#                     "Money is not a limiting factor for important change",
#                     "Can invest significantly if the approach is right",
#                     "Have a moderate budget for the right solution",
#                     "Budget is tight but can prioritize for important change",
#                     "Very limited budget - cost is a major factor"
#                 ],
#                 'pattern': 'readiness', 'weight': 'low', 'clinical': 'financial_readiness'
#             },
#             52: {
#                 'text': 'Preferred session format:',
#                 'type': 'radio',
#                 'options': [
#                     "In-person sessions only - need physical presence",
#                     "Prefer in-person but open to online if needed",
#                     "No preference - either format works fine",
#                     "Prefer online but open to in-person if better",
#                     "Online sessions only - more convenient/comfortable"
#                 ],
#                 'pattern': 'preferences', 'weight': 'low', 'clinical': 'session_preference'
#             },
#             53: {
#                 'text': 'Your timeline for starting sessions:',
#                 'type': 'radio',
#                 'options': [
#                     "Immediately - ready to book this week",
#                     "Very soon - within 2-3 weeks",
#                     "Near future - within 1-2 months",
#                     "Planning ahead - within 3-6 months",
#                     "Just exploring - no specific timeline yet"
#                 ],
#                 'pattern': 'readiness', 'weight': 'low', 'clinical': 'start_timeline'
#             },
#             54: {
#                 'text': 'Rate your overall confidence that hypnotherapy can help you achieve your goals',
#                 'type': 'slider',
#                 'min': 1, 'max': 10, 'default': 5,
#                 'pattern': 'readiness', 'weight': 'low', 'clinical': 'therapy_confidence'
#             },
#             55: {
#                 'text': 'What outcome would make this investment completely worthwhile for you?',
#                 'type': 'text',
#                 'placeholder': 'Describe the specific change or outcome that would make this completely successful...',
#                 'pattern': 'preferences', 'weight': 'low', 'clinical': 'success_criteria'
#             }
#         }
    
#     def _get_pattern_mapping(self):
#         """Map questions to patterns for clinical analysis"""
#         mapping = {}
#         for q_num, q_data in self.questions.items():
#             pattern = q_data.get('pattern')
#             weight = q_data.get('weight', 'low')
#             if pattern != 'readiness' and pattern != 'preferences' and pattern != 'all':
#                 if pattern not in mapping:
#                     mapping[pattern] = []
#                 mapping[pattern].append({
#                     'question': q_num,
#                     'weight': weight,
#                     'clinical': q_data.get('clinical', None)
#                 })
#         return mapping
    
#     def render(self):
#         """Render the complete assessment page"""
#         self._render_header()
        
#         if not st.session_state.contact_provided:
#             if st.session_state.current_question <= self.total_questions:
#                 self._render_progress()
#                 self._render_current_question()
#                 self._render_navigation()
#             else:
#                 self._render_contact_form()
#         else:
#             self._render_results()
    
#     def _render_header(self):
#         """Render assessment header with clear value proposition"""
#         st.markdown("""
#         <div style="text-align: center; margin: 1rem 0 2rem 0;">
#             <h1>Behavioral pattern assessment</h1>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Assessment value explanation
#         st.info("""
#         **Why this assessment matters:** Most hypnotherapy uses general scripts. 
#         This assessment detects your habits and triggers to build a plan that fits your needs. 
#         The assessment matches your behavior with the best neural rewiring hypnotherapy for you.
#         """)
    
#     def _render_progress(self):
#         """Render progress indicator"""
#         current = st.session_state.current_question
#         progress = (current - 1) / self.total_questions
        
#         st.progress(progress)
#         st.caption(f"Question {current} of {self.total_questions}")
    
#     def _render_current_question(self):
#         """Render current question with appropriate input type"""
#         current = st.session_state.current_question
        
#         if current <= self.total_questions:
#             question = self.questions[current]
#             self._render_question(question, current)
    
#     def _render_question(self, question, q_num):
#         """Render individual question based on type"""
#         st.markdown(f"### {question['text']}")
        
#         # Store response key
#         response_key = f"q_{q_num}"
        
#         if question['type'] == 'radio':
#             response = st.radio(
#                 f"Select your response:",
#                 question['options'],
#                 key=response_key,
#                 index=None
#             )
            
#             if response and st.button("Next Question", type="primary", key=f"next_{q_num}"):
#                 self._save_response(q_num, response)
#                 self._advance_question()
                
#         elif question['type'] == 'slider':
#             response = st.slider(
#                 f"Rate from {question['min']} to {question['max']}:",
#                 question['min'],
#                 question['max'],
#                 question['default'],
#                 key=response_key
#             )
            
#             if st.button("Next Question", type="primary", key=f"next_{q_num}"):
#                 self._save_response(q_num, response)
#                 self._advance_question()
                
#         elif question['type'] == 'text':
#             response = st.text_area(
#                 "Your response:",
#                 placeholder=question['placeholder'],
#                 key=response_key,
#                 height=100
#             )
            
#             if response.strip() and st.button("Next Question", type="primary", key=f"next_{q_num}"):
#                 self._save_response(q_num, response.strip())
#                 self._advance_question()
#             elif not response.strip():
#                 st.info("Please provide your response to continue.")
    
#     def _render_contact_form(self):
#         """Render contact form after completing all questions"""
#         st.markdown("### Assessment Complete - Get Your Results")
#         st.write("Provide your contact details to receive your comprehensive behavioral pattern analysis and personalized transformation recommendations.")
        
#         with st.form("assessment_contact_form"):
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 name = st.text_input("Full Name*", placeholder="Your full name")
#                 email = st.text_input("Email Address*", placeholder="your@email.com")
            
#             with col2:
#                 phone = st.text_input("Phone (Optional)", placeholder="+66 xxx xxx xxx")
#                 urgency = st.selectbox(
#                     "How urgent is addressing your main concern?",
#                     ["Select urgency level...", "Extremely urgent", "Very urgent", "Moderately urgent", "Not urgent"]
#                 )
            
#             primary_concern = st.text_area(
#                 "Primary Concern*",
#                 placeholder="What specific issue brought you to this assessment? Be as detailed as you'd like.",
#                 height=100
#             )
            
#             session_preference = st.selectbox(
#                 "Preferred next step:",
#                 ["Select preference...", "Schedule discovery call to discuss results", "Book transformation package directly", "Request detailed written analysis first"]
#             )
            
#             submitted = st.form_submit_button("Complete Assessment & Send Results", type="primary")
            
#             if submitted:
#                 if self._validate_contact_form(name, email, primary_concern, urgency, session_preference):
#                     self._save_contact_info(name, email, phone, urgency, primary_concern, session_preference)
#                     self._complete_assessment()
#                     st.session_state.contact_provided = True
#                     st.rerun()
    
#     def _render_navigation(self):
#         """Render navigation buttons"""
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col1:
#             if st.session_state.current_question > 1:
#                 if st.button("← Previous", key="prev_btn"):
#                     st.session_state.current_question -= 1
#                     st.rerun()
        
#         with col3:
#             if st.button("Save Progress", key="save_btn"):
#                 st.success("Progress saved! You can return anytime to complete the assessment.")
    
#     def _render_results(self):
#         """Render comprehensive assessment results"""
#         st.markdown("## Assessment Analysis Complete")
#         st.success("Your comprehensive behavioral pattern analysis has been completed and sent to our clinical team for detailed review.")
        
#         # Show summary metrics
#         self._render_results_summary()
        
#         # Show readiness assessment
#         self._render_readiness_analysis()
        
#         # Show next steps
#         self._render_next_steps()
    
#     def _render_results_summary(self):
#         """Render results summary with fixed question count"""
#         st.markdown("### Your Assessment Summary")
        
#         # Fix: Calculate actual responses count correctly (exclude contact_info)
#         response_count = 0
#         for key in st.session_state.assessment_responses.keys():
#             if key.startswith('q_') and not key == 'contact_info':
#                 response_count += 1
        
#         readiness_scores = self._calculate_readiness_metrics()
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.metric("Questions Completed", f"{response_count}/{self.total_questions}", "Comprehensive Analysis")
        
#         with col2:
#             avg_readiness = sum(readiness_scores.values()) / len(readiness_scores) if readiness_scores else 5
#             st.metric("Overall Readiness", f"{avg_readiness:.1f}/10", "For Transformation")
        
#         with col3:
#             completion_time = "30-35 minutes"
#             st.metric("Assessment Depth", completion_time, "Thorough Evaluation")
    
#     def _render_readiness_analysis(self):
#         """Render readiness analysis with paywall for clinical insights"""
#         st.markdown("### Transformation Readiness Analysis")
        
#         readiness_scores = self._calculate_readiness_metrics()
        
#         if readiness_scores.get('motivation_level', 5) >= 7:
#             st.success("High motivation level indicates excellent potential for rapid transformation.")
#         elif readiness_scores.get('motivation_level', 5) >= 5:
#             st.info("Good motivation level shows solid readiness for the transformation process.")
#         else:
#             st.warning("Lower motivation suggests a discovery call would help clarify the best approach.")
        
#         # Enhanced Clinical Analysis with Paywall
#         self._render_clinical_analysis_section()

    
#     def _render_clinical_analysis_section(self):
#         """Render clinical analysis section with paywall protection"""
#         st.markdown("### Clinical Pattern Analysis")
        
#         if PAYWALL_AVAILABLE:
#             try:
#                 paywall = create_clinical_paywall()
                
#                 # Prepare assessment data - check if results exist
#                 if hasattr(st.session_state, 'assessment_results') and st.session_state.assessment_results:
#                     assessment_data = {
#                         'assessment_results': st.session_state.assessment_results,
#                         'assessment_responses': st.session_state.assessment_responses,
#                     }
                    
#                     # Add contact info if available
#                     contact_info = st.session_state.assessment_responses.get('contact_info', {})
#                     assessment_data.update(contact_info)
                    
#                     # Check if user has paid access
#                     if paywall.check_payment_status():
#                         # Show premium analysis
#                         paywall.render_premium_analysis(assessment_data)
#                     else:
#                         # Show preview and paywall
#                         self._render_analysis_preview()
                        
#                         # Show paywall interface
#                         with st.expander("Unlock Complete Clinical Analysis", expanded=False):
#                             paywall.render_paywall_interface(assessment_data)
#                 else:
#                     st.info("Complete your assessment first to access clinical analysis.")
                    
#             except Exception as e:
#                 st.error(f"Error loading clinical analysis: {str(e)}")
#                 # Fallback to basic preview
#                 self._render_analysis_preview()
#         else:
#             # Fallback if paywall component is not available
#             st.info("Clinical analysis feature is being updated. Please contact us directly for detailed insights.")
#             self._render_analysis_preview()

#     def _render_analysis_preview(self):
#         """Render a preview of what's available in the clinical analysis"""
#         st.markdown("""
#         **Free Preview:** Your assessment reveals significant patterns that could benefit from professional analysis.
        
#         **Complete Clinical Analysis includes:**
#         - Detailed breakdown of your 9 behavioral patterns
#         - Therapeutic priorities ranked by importance  
#         - Professional interpretation of your responses
#         - Personalized session planning recommendations
#         - Communication style adaptations for optimal results
#         """)
        
#         # Show basic pattern summary (limited) - only if results exist
#         if hasattr(st.session_state, 'assessment_results') and st.session_state.assessment_results:
#             assessment_results = st.session_state.assessment_results
#             pattern_scores = assessment_results.get('pattern_scores', {})
            
#             if pattern_scores:
#                 # Show only top 2 patterns as preview
#                 sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
#                 pattern_names = {
#                     1: "Unhappiness Culture",
#                     2: "Power Struggles", 
#                     3: "Systematic Mistrust",
#                     4: "Separation/Division",
#                     5: "Doing vs Being",
#                     6: "Compartmentalized Authenticity",
#                     7: "Self-Sacrifice/Care Avoidance",
#                     8: "Inherited Missions",
#                     9: "Context-Dependent Weakness"
#                 }
                
#                 st.markdown("**Preview - Your Top Patterns:**")
#                 for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
#                     pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                     st.write(f"• {pattern_name}: Activation detected")
                
#                 if len(sorted_patterns) > 2:
#                     remaining = len(sorted_patterns) - 2
#                     st.write(f"• Plus {remaining} additional patterns analyzed...")
        
#         st.info("Unlock the complete analysis to see detailed insights, therapeutic priorities, and your personalized transformation roadmap.")
        
#     def _render_next_steps(self):
#         """Render next steps based on assessment"""
#         st.markdown("### Your personalized next steps")
        
#         # Get session preference from contact form
#         contact_info = st.session_state.assessment_responses.get('contact_info', {})
#         preference = contact_info.get('session_preference', '')
        
#         if 'discovery call' in preference.lower():
#             st.info("Based on your preference, we'll contact you to schedule a discovery call to discuss your results in detail.")
#         elif 'package directly' in preference.lower():
#             st.success("You've indicated readiness for the transformation package. We'll contact you with scheduling options.")
#         elif 'written analysis' in preference.lower():
#             st.info("You'll receive a detailed written analysis within 24 hours, followed by a consultation offer.")
#         else:
#             st.info("We'll review your assessment and contact you with personalized recommendations.")
        
#         st.markdown("""
#         **What happens next:**
        
#         1. **Clinical review** (Within 24 hours): Your responses are analyzed to identify your primary patterns and optimal treatment approach
#         2. **Personalized contact** (Within 48 hours): We'll reach out with specific recommendations based on your assessment
#         3. **Discovery call** (Optional): Discuss your results and answer questions about the process
#         4. **Transformation sessions**: Begin your personalized rapid pattern rewiring program
#         """)
        
#         # CTA for immediate booking
#         st.markdown("### Ready to take action?")
#         st.write("Don't wait for our contact - you can schedule your discovery call immediately to discuss your assessment results.")
        
#         st.markdown("""
#         <div style="text-align: center; margin: 2rem 0;">
#             <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" 
#                style="display: inline-block; background-color: var(--accent); color: white;
#                       text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
#                       font-weight: 600; font-size: 1.1rem;">
#                 Schedule Your Discovery Call Now
#             </a>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _save_response(self, question_num, response):
#         """Save question response to session state"""
#         st.session_state.assessment_responses[f'q_{question_num}'] = {
#             'response': response,
#             'question_text': self.questions[question_num]['text'],
#             'pattern': self.questions[question_num].get('pattern'),
#             'weight': self.questions[question_num].get('weight'),
#             'clinical': self.questions[question_num].get('clinical'),
#             'timestamp': datetime.now().isoformat()
#         }
    
#     def _save_contact_info(self, name, email, phone, urgency, concern, preference):
#         """Save contact information"""
#         st.session_state.assessment_responses['contact_info'] = {
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'urgency': urgency,
#             'primary_concern': concern,
#             'session_preference': preference,
#             'timestamp': datetime.now().isoformat()
#         }
    
#     def _advance_question(self):
#         """Advance to next question"""
#         st.session_state.current_question += 1
#         st.rerun()
    
#     def _validate_contact_form(self, name, email, concern, urgency, preference):
#         """Validate contact form inputs"""
#         errors = []
        
#         if not name.strip():
#             errors.append("Name is required")
        
#         if not email.strip():
#             errors.append("Email is required")
#         elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#             errors.append("Please enter a valid email address")
        
#         if not concern.strip():
#             errors.append("Primary concern is required")
        
#         if urgency == "Select urgency level...":
#             errors.append("Please select your urgency level")
        
#         if preference == "Select preference...":
#             errors.append("Please select your preferred next step")
        
#         if errors:
#             for error in errors:
#                 st.error(f"❌ {error}")
#             return False
        
#         return True
    
#     def _complete_assessment(self):
#         """Process completed assessment and send results"""
#         try:
#             # Calculate pattern scores
#             pattern_scores = self._calculate_pattern_scores()
            
#             # Extract clinical insights
#             clinical_insights = self._extract_clinical_insights()
            
#             # Calculate readiness metrics
#             readiness_metrics = self._calculate_readiness_metrics()
            
#             # Store results
#             st.session_state.assessment_results = {
#                 'pattern_scores': pattern_scores,
#                 'clinical_insights': clinical_insights,
#                 'readiness_metrics': readiness_metrics,
#                 'completion_timestamp': datetime.now().isoformat()
#             }
            
#             # Send comprehensive email
#             self._send_assessment_email()
            
#         except Exception as e:
#             st.error(f"Error processing assessment: {str(e)}")
    
#     def _calculate_pattern_scores(self):
#         """Calculate weighted scores for each behavioral pattern"""
#         pattern_scores = {pattern_id: 0 for pattern_id in self.patterns.keys()}
        
#         for response_key, response_data in st.session_state.assessment_responses.items():
#             if response_key.startswith('q_'):
#                 pattern = response_data.get('pattern')
#                 weight = response_data.get('weight', 'low')
#                 response = response_data.get('response')
                
#                 if pattern in pattern_scores and response:
#                     # Weight multiplier
#                     weight_multiplier = self.question_weights.get(weight, 1)
                    
#                     # Score based on response type
#                     if isinstance(response, str) and len(response) > 10:  # Text responses
#                         pattern_scores[pattern] += weight_multiplier
#                     elif isinstance(response, (int, float)):  # Slider responses
#                         if response >= 6:
#                             pattern_scores[pattern] += weight_multiplier
#                     elif isinstance(response, str):  # Radio responses
#                         # First option is typically the healthy response
#                         question_num = int(response_key.split('_')[1])
#                         question = self.questions[question_num]
#                         if 'options' in question:
#                             try:
#                                 response_index = question['options'].index(response)
#                                 if response_index > 0:  # Not the first (healthy) option
#                                     pattern_scores[pattern] += weight_multiplier
#                             except ValueError:
#                                 pass
        
#         return pattern_scores
    
#     def _extract_clinical_insights(self):
#         """Extract key clinical insights from responses"""
#         insights = {}
        
#         for response_key, response_data in st.session_state.assessment_responses.items():
#             clinical_type = response_data.get('clinical')
#             response = response_data.get('response')
            
#             if clinical_type and response:
#                 insights[clinical_type] = response
        
#         return insights
    
#     def _calculate_readiness_metrics(self):
#         """Calculate transformation readiness metrics"""
#         readiness_metrics = {}
        
#         # Extract specific readiness responses
#         readiness_questions = {
#             'urgency_level': 41,
#             'motivation_level': 42,
#             'commitment_level': 43,
#             'rapid_change_belief': 45,
#             'emotional_readiness': 49,
#             'therapy_confidence': 54
#         }
        
#         for metric, question_num in readiness_questions.items():
#             response_key = f'q_{question_num}'
#             if response_key in st.session_state.assessment_responses:
#                 response = st.session_state.assessment_responses[response_key]['response']
                
#                 if isinstance(response, (int, float)):
#                     readiness_metrics[metric] = response
#                 elif isinstance(response, str):
#                     # Convert text responses to numeric scale
#                     if 'extremely' in response.lower() or 'unlimited' in response.lower():
#                         readiness_metrics[metric] = 10
#                     elif 'quite' in response.lower() or 'high' in response.lower():
#                         readiness_metrics[metric] = 8
#                     elif 'moderate' in response.lower():
#                         readiness_metrics[metric] = 6
#                     elif 'somewhat' in response.lower() or 'limited' in response.lower():
#                         readiness_metrics[metric] = 4
#                     else:
#                         readiness_metrics[metric] = 2
        
#         return readiness_metrics
    
#     def _send_assessment_email(self):
#         """Send comprehensive assessment results via email"""
#         try:
#             from utils.email_handler import send_discovery_call_email
            
#             # Get contact info
#             contact_info = st.session_state.assessment_responses.get('contact_info', {})
            
#             # Prepare comprehensive assessment data
#             assessment_data = {
#                 'name': contact_info.get('name', 'Unknown'),
#                 'email': contact_info.get('email', 'Unknown'),
#                 'phone': contact_info.get('phone', 'Not provided'),
#                 'concern': contact_info.get('primary_concern', 'Comprehensive Assessment'),
#                 'urgency': contact_info.get('urgency', 'Not specified'),
#                 'session_preference': contact_info.get('session_preference', 'Not specified'),
#                 'form_type': 'Complete Behavioral Pattern Assessment',
#                 'source': 'Assessment Page',
#                 'total_questions': self.total_questions,
#                 'completion_rate': '100%',
#                 'assessment_results': st.session_state.assessment_results,
#                 'raw_responses': st.session_state.assessment_responses,
#                 'clinical_template': self._generate_clinical_template(),
#                 'timestamp': datetime.now().isoformat()
#             }
            
#             # Send email
#             success = send_discovery_call_email(assessment_data)
            
#             if success:
#                 st.success("✅ Assessment results sent successfully to our clinical team!")
#             else:
#                 st.warning("⚠️ Assessment completed, but email notification failed. We have your responses saved.")
                
#         except Exception as e:
#             st.error(f"Error sending assessment results: {str(e)}")
    
#     def _generate_clinical_template(self):
#         """Generate comprehensive clinical template for therapist"""
#         template = []
        
#         # Header
#         template.append("COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT - CLINICAL TEMPLATE")
#         template.append("=" * 70)
#         template.append(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#         template.append(f"Total Questions: {self.total_questions}")
#         template.append("")
        
#         # Contact & Urgency Info
#         contact_info = st.session_state.assessment_responses.get('contact_info', {})
#         template.append("CLIENT INFORMATION:")
#         template.append(f"Name: {contact_info.get('name', 'Not provided')}")
#         template.append(f"Email: {contact_info.get('email', 'Not provided')}")
#         template.append(f"Phone: {contact_info.get('phone', 'Not provided')}")
#         template.append(f"Urgency Level: {contact_info.get('urgency', 'Not specified')}")
#         template.append(f"Primary Concern: {contact_info.get('primary_concern', 'Not provided')}")
#         template.append(f"Preferred Next Step: {contact_info.get('session_preference', 'Not specified')}")
#         template.append("")
        
#         # Pattern Analysis
#         pattern_scores = st.session_state.assessment_results.get('pattern_scores', {})
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
#         template.append("BEHAVIORAL PATTERN ANALYSIS:")
#         template.append("Primary Therapeutic Targets (Highest Activation):")
#         for pattern_id, score in sorted_patterns[:3]:
#             pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
#             template.append(f"- {pattern_name}: Activation Level {score}")
#         template.append("")
        
#         # Clinical Insights
#         clinical_insights = st.session_state.assessment_results.get('clinical_insights', {})
#         if clinical_insights:
#             template.append("KEY CLINICAL INSIGHTS:")
#             for insight_type, insight_data in clinical_insights.items():
#                 template.append(f"- {insight_type.replace('_', ' ').title()}: {insight_data}")
#             template.append("")
        
#         # Readiness Assessment
#         readiness_metrics = st.session_state.assessment_results.get('readiness_metrics', {})
#         if readiness_metrics:
#             template.append("TRANSFORMATION READINESS METRICS:")
#             for metric, score in readiness_metrics.items():
#                 template.append(f"- {metric.replace('_', ' ').title()}: {score}/10")
#             template.append("")
        
#         # Session Recommendations
#         template.append("RECOMMENDED SESSION APPROACH:")
#         primary_pattern = sorted_patterns[0][0] if sorted_patterns else 1
#         secondary_pattern = sorted_patterns[1][0] if len(sorted_patterns) > 1 else 2
        
#         template.append(f"Session 1: Map {self.patterns[primary_pattern]} and {self.patterns[secondary_pattern]} patterns")
#         template.append(f"Session 2: Neural rewiring targeting {self.patterns[primary_pattern]}")
#         template.append("Session 3: Reinforcement if needed (assess after Session 2)")
#         template.append("")
        
#         # Communication Preferences
#         comm_style = clinical_insights.get('communication_style', 'Not specified')
#         learning_style = clinical_insights.get('learning_style', 'Not specified')
#         template.append("THERAPEUTIC COMMUNICATION NOTES:")
#         template.append(f"Preferred Communication Style: {comm_style}")
#         template.append(f"Learning Style: {learning_style}")
#         template.append("")
        
#         return "\n".join(template)


# class AssessPage:
#     """Main assessment page component"""
    
#     def __init__(self):
#         self.assessment = BehavioralPatternAssessment()
    
#     def render(self):
#         """Render the complete assessment page"""
#         self.assessment.render()


# # Factory function for clean import
# def create_assess_page():
#     """Factory function to create AssessPage instance"""
#     return AssessPage()


















"""
Enhanced Behavioral Pattern Assessment with Adaptive Flow
Advanced pattern detection with therapeutic precision
Mobile-optimized card-based UX
"""
import streamlit as st
from datetime import datetime
import re
import json

try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False
    print("Paywall component not available")

class AdaptiveBehavioralAssessment:
    """Advanced behavioral pattern assessment with adaptive questioning"""
    
    def __init__(self):
        self._init_session_state()
        
        # Pattern definitions for clinical mapping
        self.patterns = {
            1: "Unhappiness culture",
            2: "Power struggles", 
            3: "Systematic mistrust",
            4: "Separation and division",
            5: "Doing versus being",
            6: "Compartmentalized authenticity",
            7: "Self sacrifice and care avoidance",
            8: "Inherited missions",
            9: "Context dependent weakness"
        }
        
        # Core questions (everyone gets these)
        self.core_questions = self._get_core_questions()
        
        # Adaptive question pools
        self.adaptive_pools = self._get_adaptive_question_pools()
        
        # Risk assessment questions
        self.safety_questions = self._get_safety_questions()
        
    def _init_session_state(self):
        """Initialize session state variables"""
        if 'assessment_responses' not in st.session_state:
            st.session_state.assessment_responses = {}
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 1
        if 'question_sequence' not in st.session_state:
            st.session_state.question_sequence = []
        if 'adaptive_triggered' not in st.session_state:
            st.session_state.adaptive_triggered = []
        if 'assessment_completed' not in st.session_state:
            st.session_state.assessment_completed = False
        if 'contact_provided' not in st.session_state:
            st.session_state.contact_provided = False
        if 'assessment_results' not in st.session_state:
            st.session_state.assessment_results = {}
        if 'pattern_scores' not in st.session_state:
            st.session_state.pattern_scores = {}
        if 'risk_flags' not in st.session_state:
            st.session_state.risk_flags = []
            
    def _get_core_questions(self):
        """Core 25 questions everyone receives"""
        return {
            1: {
                "text": "When something genuinely wonderful happens to you, your first thought is usually:",
                "type": "single_choice",
                "options": [
                    "I feel genuinely happy and want to celebrate",
                    "This won't last long or something bad will balance it out", 
                    "I don't really deserve this good thing",
                    "I need to downplay it so others don't feel bad",
                    "Not applicable to my experience"
                ],
                "patterns": [None, 1, 1, 1, None],
                "weights": [0, 3, 3, 2, 0],
                "adaptive_triggers": ["unhappiness_deep", "perfectionism_anxiety"]
            },
            
            2: {
                "text": "In disagreements, your body typically:",
                "type": "single_choice", 
                "options": [
                    "Stays calm while I listen to understand their view",
                    "Tenses up immediately, ready to defend my position",
                    "Goes numb and I want to escape the situation",
                    "Gets hot with racing heart and adrenaline",
                    "Not applicable - I avoid disagreements"
                ],
                "patterns": [None, 2, 3, 2, 3],
                "weights": [0, 3, 2, 3, 2],
                "adaptive_triggers": ["conflict_trauma", "avoidance_pattern"]
            },

            3: {
                "text": "Your default assumption about new people's intentions:",
                "type": "single_choice",
                "options": [
                    "Most people are generally well-meaning until proven otherwise",
                    "They're probably judging me in some way",
                    "They want something from me or will try to use me",
                    "They'll reject me once they see my flaws",
                    "I need to figure out their hidden agenda"
                ],
                "patterns": [None, 3, 3, 3, 3],
                "weights": [0, 2, 3, 2, 3],
                "adaptive_triggers": ["trust_trauma", "social_anxiety"]
            },

            4: {
                "text": "When facing important life choices, you typically:",
                "type": "single_choice",
                "options": [
                    "Look for creative solutions that honor multiple values",
                    "Feel trapped between impossible either-or options", 
                    "See only two extreme alternatives",
                    "Get paralyzed by black and white thinking",
                    "Feel like I can't have what I really want"
                ],
                "patterns": [None, 4, 4, 4, 4],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["binary_thinking", "decision_paralysis"]
            },

            5: {
                "text": "Complete this honestly: 'I feel valuable when I...'",
                "type": "single_choice",
                "options": [
                    "Simply exist as I am",
                    "Accomplish something important",
                    "Help or please other people", 
                    "Prove my worth through performance",
                    "Stay busy and productive"
                ],
                "patterns": [None, 5, 7, 5, 5],
                "weights": [0, 2, 2, 3, 3],
                "adaptive_triggers": ["performance_anxiety", "people_pleasing"]
            },

            6: {
                "text": "Your personality or behavior significantly changes based on:",
                "type": "single_choice",
                "options": [
                    "It stays pretty consistent across all contexts",
                    "Which group of people I'm with",
                    "Professional versus personal settings",
                    "Whether I'm in control or following others",
                    "If I'm the expert or the newcomer"
                ],
                "patterns": [None, 6, 6, 6, 6],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["identity_fragmentation", "context_switching"]
            },

            7: {
                "text": "When it comes to your own health, fitness, or wellbeing:",
                "type": "single_choice",
                "options": [
                    "I naturally prioritize my wellbeing alongside others'",
                    "I know what to do but can't make myself do it",
                    "I care for everyone else first, then there's no energy left",
                    "I feel selfish focusing on my own needs",
                    "I'm great at advising others but terrible at following my own advice"
                ],
                "patterns": [None, 7, 7, 7, 7],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["self_neglect", "caretaker_pattern"]
            },

            8: {
                "text": "Your major life goals (career, lifestyle, achievements) are primarily:",
                "type": "single_choice",
                "options": [
                    "Genuinely what I desire for my own life",
                    "What my family expected or dreamed for me",
                    "Honoring someone who died or sacrificed for me",
                    "Proving I'm worthy of someone's love or sacrifice",
                    "What I think I 'should' want based on my background"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["family_loyalty", "inherited_guilt"]
            },

            9: {
                "text": "With certain people or in specific situations, you:",
                "type": "single_choice",
                "options": [
                    "Stay true to my values and boundaries",
                    "Become someone I don't respect or recognize",
                    "Lose all my usual boundaries and standards",
                    "Act against my stated values and beliefs",
                    "Can't say no even when I desperately want to"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 3, 2, 3],
                "adaptive_triggers": ["boundary_collapse", "people_pleasing"]
            },

            10: {
                "text": "When you enter a room of strangers, you automatically think:",
                "type": "single_choice",
                "options": [
                    "These seem like interesting people to meet",
                    "They're probably thinking something critical about me",
                    "I don't belong here",
                    "I need to figure out the social dynamics quickly",
                    "I hope I can get through this without embarrassing myself"
                ],
                "patterns": [None, 3, 4, 3, 3],
                "weights": [0, 2, 2, 2, 2],
                "adaptive_triggers": ["social_anxiety", "belonging_issues"]
            },

            11: {
                "text": "During a disagreement, you're most likely to:",
                "type": "single_choice",
                "options": [
                    "Listen to understand their perspective",
                    "Attack their position aggressively",
                    "Withdraw and shut down emotionally",
                    "Submit externally but feel resentful internally",
                    "Try to manage their emotions to avoid conflict"
                ],
                "patterns": [None, 2, 2, 2, 7],
                "weights": [0, 3, 2, 2, 2],
                "adaptive_triggers": ["conflict_trauma", "emotional_management"]
            },

            12: {
                "text": "Complete this sentence: 'In life, I have to choose between security _____ freedom'",
                "type": "single_choice",
                "options": [
                    "AND (I can have both)",
                    "OR (I must choose one)",
                    "This sentence doesn't resonate with me",
                    "Both seem impossible to achieve",
                    "I've never thought about it this way"
                ],
                "patterns": [None, 4, None, 4, None],
                "weights": [0, 3, 0, 2, 0],
                "adaptive_triggers": ["binary_thinking", "scarcity_mindset"]
            },

            13: {
                "text": "There are areas of your life where you feel completely capable, and others where you feel powerless:",
                "type": "single_choice",
                "options": [
                    "No, I feel consistently myself everywhere",
                    "Yes - I'm like two completely different people",
                    "I'm strong professionally but weak personally",
                    "I'm confident socially but insecure privately",
                    "I lead some groups but follow others completely"
                ],
                "patterns": [None, 6, 6, 6, 6],
                "weights": [0, 3, 2, 2, 2],
                "adaptive_triggers": ["compartmentalization", "context_switching"]
            },

            14: {
                "text": "You consistently have energy and motivation for:",
                "type": "single_choice",
                "options": [
                    "Both personal and external responsibilities equally",
                    "Other people's goals but not my own",
                    "Work projects but not personal care",
                    "Helping others but not helping myself",
                    "Everything except what my body needs"
                ],
                "patterns": [None, 7, 7, 7, 7],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["self_neglect", "energy_imbalance"]
            },

            15: {
                "text": "When you think about what YOU actually want (separate from all expectations):",
                "type": "single_choice",
                "options": [
                    "I can access it clearly and confidently",
                    "I honestly don't know anymore",
                    "I feel guilty for wanting something different",
                    "I feel like I'd be betraying someone important",
                    "I'm afraid it's not worthy or important enough"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["authentic_self", "guilt_loyalty"]
            },

            16: {
                "text": "Growing up, which phrase did you hear most often?",
                "type": "single_choice",
                "options": [
                    "You can achieve anything you set your mind to",
                    "Life is tough, get used to it",
                    "Don't get your hopes up",
                    "We're not here to have fun",
                    "Good things happen to other people, not us"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 2, 3, 2, 3],
                "adaptive_triggers": ["family_messages", "early_programming"]
            },

            17: {
                "text": "What scares you most about completely solving your main problem?",
                "type": "single_choice",
                "options": [
                    "Nothing really scares me about solving it",
                    "I wouldn't know who I am anymore",
                    "People might expect too much from me",
                    "I might lose connections with others who struggle similarly",
                    "I'd have to take full responsibility for my life and happiness"
                ],
                "patterns": [None, 8, 5, 4, 5],
                "weights": [0, 2, 2, 2, 3],
                "adaptive_triggers": ["change_resistance", "identity_threat"]
            },

            18: {
                "text": "Complete this: 'People like me don't get to have...'",
                "type": "text_completion",
                "placeholder": "Complete with what first comes to mind...",
                "patterns": "limiting_belief",
                "adaptive_triggers": ["core_belief", "scarcity_pattern"]
            },

            19: {
                "text": "When someone offers you genuine help or shows you kindness:",
                "type": "single_choice",
                "options": [
                    "I can receive it gracefully",
                    "I immediately wonder what they want in return",
                    "I feel uncomfortable and try to reciprocate immediately",
                    "I assume they pity me or see me as weak",
                    "I worry about owing them something"
                ],
                "patterns": [None, 3, 3, 3, 3],
                "weights": [0, 2, 2, 2, 2],
                "adaptive_triggers": ["trust_issues", "receiving_blocks"]
            },

            20: {
                "text": "In situations where there's social pressure to do something you don't want to do:",
                "type": "single_choice",
                "options": [
                    "I can say no clearly and maintain my boundaries",
                    "I go along to avoid conflict or rejection",
                    "I feel paralyzed and unable to speak up",
                    "I do it but feel resentful and angry afterward",
                    "I convince myself I actually want to do it"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["boundary_issues", "social_pressure"]
            },

            21: {
                "text": "Your current life path feels:",
                "type": "single_choice",
                "options": [
                    "Like it genuinely reflects who I am",
                    "Like fulfilling someone else's dreams",
                    "Like honoring a debt I owe",
                    "Like the 'right' thing but not the authentic thing",
                    "Like I'm afraid to choose differently"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 3, 2, 2],
                "adaptive_triggers": ["authenticity_gap", "family_pressure"]
            },

            22: {
                "text": "When you're on the verge of achieving something important, you often:",
                "type": "single_choice",
                "options": [
                    "Feel excited and push through to completion",
                    "Find ways to sabotage or delay it",
                    "Become overwhelmed and want to quit",
                    "Start focusing on everything that could go wrong",
                    "Feel like I don't deserve to succeed"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 3, 2, 2, 3],
                "adaptive_triggers": ["success_sabotage", "unworthiness"]
            },

            23: {
                "text": "There are specific people around whom you consistently make choices you later regret:",
                "type": "single_choice",
                "options": [
                    "No, I make similar choices regardless of who's around",
                    "Yes, and I know who they are but can't seem to stop",
                    "I become weak-willed around certain personality types",
                    "I desperately want their approval and will do anything for it",
                    "I'm afraid of conflict so I go along with things I hate"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["context_weakness", "approval_seeking"]
            },

            24: {
                "text": "When your efforts go completely unnoticed or unappreciated:",
                "type": "single_choice",
                "options": [
                    "I know my worth isn't dependent on external recognition",
                    "I feel invisible and unimportant",
                    "I work even harder to get attention",
                    "I question whether what I did actually mattered",
                    "I feel resentful and want to stop trying"
                ],
                "patterns": [None, 5, 5, 5, 5],
                "weights": [0, 2, 2, 2, 2],
                "adaptive_triggers": ["recognition_needs", "validation_seeking"]
            },

            25: {
                "text": "How urgently do you need to resolve your main concern?",
                "type": "single_choice",
                "options": [
                    "Extremely urgent - affecting my daily life significantly",
                    "Very urgent - I need change within the next few months",
                    "Moderately urgent - would like change within 6 months",
                    "Somewhat urgent - exploring options for gradual change",
                    "Not urgent - just curious about possibilities"
                ],
                "patterns": "readiness",
                "weights": [5, 4, 3, 2, 1],
                "adaptive_triggers": ["urgency_high", "exploration_phase"]
            }
        }

    def _get_adaptive_question_pools(self):
        """Adaptive question pools triggered by patterns"""
        return {
            "unhappiness_deep": {
                26: {
                    "text": "When good things happen to others, you typically:",
                    "type": "single_choice",
                    "options": [
                        "Feel genuinely happy for them",
                        "Wonder why good things don't happen to me",
                        "Feel like it proves I'm not worthy of good things",
                        "Get suspicious about what bad thing will balance it out",
                        "Feel guilty for not being happier for them"
                    ],
                    "patterns": [None, 1, 1, 1, 1],
                    "weights": [0, 2, 3, 2, 2]
                },
                27: {
                    "text": "The thought 'I don't deserve this' most often comes up when:",
                    "type": "single_choice",
                    "options": [
                        "It rarely comes up for me",
                        "I'm receiving love or affection",
                        "I'm achieving success or recognition",
                        "Someone is being kind or generous to me",
                        "I'm experiencing joy or happiness"
                    ],
                    "patterns": [None, 1, 1, 1, 1],
                    "weights": [0, 3, 3, 2, 3]
                }
            },

            "conflict_trauma": {
                28: {
                    "text": "When you were growing up, family conflicts usually ended with:",
                    "type": "single_choice",
                    "options": [
                        "Everyone talking it through until resolved",
                        "Someone getting very angry and others going silent",
                        "Long periods of tension and not speaking",
                        "Someone always having to apologize to keep peace",
                        "Pretending nothing happened and moving on"
                    ],
                    "patterns": [None, 2, 2, 7, 3],
                    "weights": [0, 3, 2, 2, 2]
                },
                29: {
                    "text": "Your body's alarm system seems to be:",
                    "type": "single_choice",
                    "options": [
                        "Appropriately calibrated to actual threats",
                        "Constantly scanning for potential problems",
                        "Overreactive to minor relationship tensions",
                        "Numb - I don't notice danger until it's too late",
                        "Exhausted from being on high alert"
                    ],
                    "patterns": [None, 3, 2, 3, 3],
                    "weights": [0, 2, 3, 2, 3]
                }
            },

            "family_loyalty": {
                30: {
                    "text": "If you lived your most authentic life, which relationship would be most threatened:",
                    "type": "single_choice",
                    "options": [
                        "None - my relationships would likely improve",
                        "With parents who sacrificed for specific dreams",
                        "With the memory or legacy of someone who died",
                        "With family members who define success differently",
                        "With a community that has certain expectations"
                    ],
                    "patterns": [None, 8, 8, 8, 8],
                    "weights": [0, 2, 3, 2, 2]
                },
                31: {
                    "text": "The family member whose approval matters most to you would say your biggest problem is:",
                    "type": "text_completion",
                    "placeholder": "What would they say your problem is?",
                    "patterns": "family_perspective"
                }
            },

            "self_neglect": {
                32: {
                    "text": "When you think about taking time for yourself, you typically:",
                    "type": "single_choice",
                    "options": [
                        "See it as necessary and plan for it",
                        "Feel guilty like I should be doing something productive",
                        "Think of all the people who need me more",
                        "Feel selfish and undeserving",
                        "Can't even imagine what that would look like"
                    ],
                    "patterns": [None, 7, 7, 7, 7],
                    "weights": [0, 2, 3, 3, 2]
                },
                33: {
                    "text": "Your energy typically gets distributed:",
                    "type": "single_choice",
                    "options": [
                        "Balanced between self-care and caring for others",
                        "80% for others, 20% for self",
                        "90% for others, 10% for self",
                        "100% for others until I collapse",
                        "I honestly don't know how to give energy to myself"
                    ],
                    "patterns": [None, 7, 7, 7, 7],
                    "weights": [0, 2, 3, 3, 3]
                }
            },

            "trust_trauma": {
                34: {
                    "text": "In your early years, the people who were supposed to protect you:",
                    "type": "single_choice",
                    "options": [
                        "Generally did protect me and I felt safe",
                        "Sometimes protected me but were unpredictable",
                        "Were often the source of threat themselves",
                        "Were absent when I needed protection most",
                        "I had to protect myself and others"
                    ],
                    "patterns": [None, 3, 3, 3, 7],
                    "weights": [0, 2, 3, 2, 2],
                    "risk_flags": ["early_trauma", "caretaker_dysfunction"]
                },
                35: {
                    "text": "Your default assumption is that people will:",
                    "type": "single_choice",
                    "options": [
                        "Generally be trustworthy unless proven otherwise",
                        "Let me down when I need them most",
                        "Use my vulnerabilities against me",
                        "Leave when things get difficult",
                        "Judge me harshly if they really know me"
                    ],
                    "patterns": [None, 3, 3, 3, 3],
                    "weights": [0, 2, 3, 2, 2]
                }
            }
        }

    def _get_safety_questions(self):
        """Safety assessment questions triggered by risk flags"""
        return {
            "current_support": {
                50: {
                    "text": "Right now, if you were in crisis, you have:",
                    "type": "single_choice",
                    "options": [
                        "Multiple people I could reach out to for support",
                        "One or two people I might feel comfortable contacting",
                        "People in my life but I wouldn't want to burden them",
                        "No one I would feel comfortable reaching out to",
                        "Professional support (therapist, counselor, etc.)"
                    ],
                    "risk_assessment": True
                }
            },
            
            "coping_strategies": {
                51: {
                    "text": "When you're overwhelmed, you're most likely to:",
                    "type": "single_choice",
                    "options": [
                        "Use healthy coping strategies like exercise, meditation, or talking",
                        "Isolate myself until the feeling passes",
                        "Distract myself with work, TV, or other activities",
                        "Use substances to numb or escape the feelings",
                        "Engage in self-destructive behaviors"
                    ],
                    "risk_assessment": True,
                    "risk_flags": {
                        3: ["substance_use"],
                        4: ["self_harm_risk"]
                    }
                }
            }
        }

    def render(self):
        """Render the complete assessment"""
        self._render_header()
        
        if not st.session_state.contact_provided:
            if not st.session_state.assessment_completed:
                self._render_current_question()
            else:
                self._render_contact_form()
        else:
            self._render_results()

    def _render_header(self):
        """Render assessment header"""
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0 2rem 0;">
            <h1>Behavioral pattern assessment</h1>
            <p style="color: #556D7A; font-size: 1.1rem;">
                Advanced assessment to identify your unique patterns for personalized transformation
            </p>
        </div>
        """, unsafe_allow_html=True)

    def _render_current_question(self):
        """Render current question with mobile-optimized card design"""
        # Determine current question to show
        current_q_id = self._get_current_question_id()
        
        if current_q_id is None:
            # Assessment complete
            st.session_state.assessment_completed = True
            self._calculate_final_results()
            st.rerun()
            return

        # Get question data
        question = self._get_question_by_id(current_q_id)
        if not question:
            st.error("Question not found")
            return

        # Calculate progress
        total_questions = self._estimate_total_questions()
        completed = len(st.session_state.assessment_responses)
        progress = completed / total_questions if total_questions > 0 else 0

        # Mobile-optimized card layout
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 2rem; margin: 1rem 0; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <span style="color: #556D7A; font-size: 0.9rem;">Question {completed + 1} of ~{total_questions}</span>
                <span style="color: #4CA1A3; font-size: 0.9rem;">{int(progress * 100)}% complete</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar
        st.progress(progress)

        # Question content
        st.markdown(f"### {question['text']}")

        # Handle different question types
        if question['type'] == 'single_choice':
            self._render_single_choice(current_q_id, question)
        elif question['type'] == 'text_completion':
            self._render_text_completion(current_q_id, question)

        # Navigation buttons
        self._render_navigation(current_q_id)

    def _render_single_choice(self, q_id, question):
        """Render single choice question with large mobile-friendly buttons"""
        response_key = f"q_{q_id}_response"
        
        # Create unique key for this question
        for i, option in enumerate(question['options']):
            if st.button(
                option, 
                key=f"q_{q_id}_option_{i}",
                use_container_width=True,
                type="secondary"
            ):
                self._save_response(q_id, option, question)
                self._advance_question()
                st.rerun()

    def _render_text_completion(self, q_id, question):
        """Render text completion question"""
        response = st.text_area(
            "Your response:",
            placeholder=question.get('placeholder', 'Enter your response...'),
            key=f"q_{q_id}_text",
            height=100
        )
        
        if response.strip() and st.button("Continue", key=f"q_{q_id}_continue", type="primary"):
            self._save_response(q_id, response.strip(), question)
            self._advance_question()
            st.rerun()
        elif not response.strip():
            st.info("Please provide your response to continue.")

    def _render_navigation(self, current_q_id):
        """Render navigation buttons"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if len(st.session_state.assessment_responses) > 0:
                if st.button("← Back", key="nav_back"):
                    self._go_back()
                    st.rerun()
        
        with col2:
            if st.button("Skip Question", key="nav_skip", help="Skip if not applicable"):
                self._save_response(current_q_id, "Not applicable", {"patterns": None, "weights": [0]})
                self._advance_question()
                st.rerun()
        
        with col3:
            st.markdown(f"**{len(st.session_state.assessment_responses)}** answered")

    def _get_current_question_id(self):
        """Get the ID of the current question to display"""
        answered_questions = set(st.session_state.assessment_responses.keys())
        
        # Check core questions first
        for q_id in range(1, 26):
            if q_id not in answered_questions:
                return q_id
        
        # Check adaptive questions
        for pool_name in st.session_state.adaptive_triggered:
            if pool_name in self.adaptive_pools:
                for q_id in self.adaptive_pools[pool_name]:
                    if q_id not in answered_questions:
                        return q_id
        
        # Check safety questions if risk flags triggered
        if st.session_state.risk_flags:
            for pool_name in ["current_support", "coping_strategies"]:
                if pool_name in self.safety_questions:
                    for q_id in self.safety_questions[pool_name]:
                        if q_id not in answered_questions:
                            return q_id
        
        return None  # Assessment complete

    def _get_question_by_id(self, q_id):
        """Get question data by ID from any pool"""
        # Check core questions
        if q_id in self.core_questions:
            return self.core_questions[q_id]
        
        # Check adaptive pools
        for pool in self.adaptive_pools.values():
            if q_id in pool:
                return pool[q_id]
        
        # Check safety questions
        for pool in self.safety_questions.values():
            if q_id in pool:
                return pool[q_id]
        
        return None

    def _save_response(self, q_id, response, question):
        """Save response and trigger adaptive logic"""
        # Save response
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Update pattern scores
        self._update_pattern_scores(q_id, response, question)
        
        # Check for adaptive triggers
        self._check_adaptive_triggers(q_id, response, question)
        
        # Check for risk flags
        self._check_risk_flags(q_id, response, question)

    def _update_pattern_scores(self, q_id, response, question):
        """Update pattern scores based on response"""
        if 'patterns' not in question or question['patterns'] is None:
            return
        
        if question['type'] == 'single_choice':
            patterns = question.get('patterns', [])
            weights = question.get('weights', [])
            
            if isinstance(patterns, list) and isinstance(weights, list):
                # Find selected option index
                options = question.get('options', [])
                try:
                    option_index = options.index(response)
                    if option_index < len(patterns) and patterns[option_index] is not None:
                        pattern_id = patterns[option_index]
                        weight = weights[option_index] if option_index < len(weights) else 1
                        
                        if pattern_id not in st.session_state.pattern_scores:
                            st.session_state.pattern_scores[pattern_id] = 0
                        st.session_state.pattern_scores[pattern_id] += weight
                except ValueError:
                    pass  # Response not in options

    def _check_adaptive_triggers(self, q_id, response, question):
        """Check if response triggers adaptive question pools"""
        adaptive_triggers = question.get('adaptive_triggers', [])
        
        if question['type'] == 'single_choice':
            options = question.get('options', [])
            try:
                option_index = options.index(response)
                
                # Check specific option triggers
                for trigger in adaptive_triggers:
                    if trigger not in st.session_state.adaptive_triggered:
                        # Add trigger logic based on response patterns
                        if self._should_trigger_adaptive_pool(trigger, option_index, response):
                            st.session_state.adaptive_triggered.append(trigger)
                            
            except ValueError:
                pass

    def _should_trigger_adaptive_pool(self, trigger, option_index, response):
        """Determine if adaptive pool should be triggered"""
        trigger_conditions = {
            "unhappiness_deep": option_index in [1, 2, 3],
            "conflict_trauma": option_index in [1, 2, 3],
            "family_loyalty": option_index in [1, 2, 3, 4],
            "self_neglect": option_index in [1, 2, 3, 4],
            "trust_trauma": option_index in [1, 2, 3, 4],
            "perfectionism_anxiety": option_index in [1, 2],
            "avoidance_pattern": option_index == 4,
            "social_anxiety": option_index in [1, 2, 4],
            "boundary_issues": option_index in [1, 2, 3],
            "people_pleasing": option_index in [1, 2, 3]
        }
        
        return trigger_conditions.get(trigger, False)

    def _check_risk_flags(self, q_id, response, question):
        """Check for risk indicators that require safety assessment"""
        risk_flags = question.get('risk_flags', {})
        
        if question['type'] == 'single_choice':
            options = question.get('options', [])
            try:
                option_index = options.index(response)
                if option_index in risk_flags:
                    for flag in risk_flags[option_index]:
                        if flag not in st.session_state.risk_flags:
                            st.session_state.risk_flags.append(flag)
            except ValueError:
                pass

    def _advance_question(self):
        """Advance to next question in sequence"""
        st.session_state.current_question += 1

    def _go_back(self):
        """Go back to previous question"""
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            # Remove last response
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]

    def _estimate_total_questions(self):
        """Estimate total questions based on current triggers"""
        base_questions = 25
        adaptive_questions = len(st.session_state.adaptive_triggered) * 2  # Average 2 per pool
        safety_questions = len(st.session_state.risk_flags) * 1  # 1 per risk flag
        
        return base_questions + adaptive_questions + safety_questions

    def _calculate_final_results(self):
        """Calculate final assessment results"""
        # Calculate pattern dominance
        sorted_patterns = sorted(
            st.session_state.pattern_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Extract clinical insights from text responses
        clinical_insights = self._extract_clinical_insights()
        
        # Calculate readiness metrics
        readiness_metrics = self._calculate_readiness_metrics()
        
        # Generate resistance predictions
        resistance_predictions = self._predict_resistance_points()
        
        # Store comprehensive results
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': sorted_patterns[0] if sorted_patterns else (None, 0),
            'secondary_patterns': sorted_patterns[1:3] if len(sorted_patterns) > 1 else [],
            'clinical_insights': clinical_insights,
            'readiness_metrics': readiness_metrics,
            'resistance_predictions': resistance_predictions,
            'risk_flags': st.session_state.risk_flags,
            'adaptive_triggered': st.session_state.adaptive_triggered,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses)
        }

    def _extract_clinical_insights(self):
        """Extract insights from text responses and patterns"""
        insights = {}
        
        # Extract from text completion responses
        for q_id, response_data in st.session_state.assessment_responses.items():
            if response_data.get('question_type') == 'text_completion':
                question = self._get_question_by_id(q_id)
                if question and 'patterns' in question:
                    pattern_type = question['patterns']
                    insights[pattern_type] = response_data['response']
        
        return insights

    def _calculate_readiness_metrics(self):
        """Calculate transformation readiness metrics"""
        readiness_score = 5  # Default
        
        # Extract readiness from question 25
        for response_data in st.session_state.assessment_responses.values():
            if 'Extremely urgent' in response_data.get('response', ''):
                readiness_score = 10
            elif 'Very urgent' in response_data.get('response', ''):
                readiness_score = 8
            elif 'Moderately urgent' in response_data.get('response', ''):
                readiness_score = 6
            elif 'Somewhat urgent' in response_data.get('response', ''):
                readiness_score = 4
            elif 'Not urgent' in response_data.get('response', ''):
                readiness_score = 2
        
        return {
            'urgency_level': readiness_score,
            'risk_level': 'High' if st.session_state.risk_flags else 'Low',
            'complexity': 'High' if len(st.session_state.adaptive_triggered) > 3 else 'Medium'
        }

    def _predict_resistance_points(self):
        """Predict specific resistance points based on patterns"""
        predictions = []
        
        # Pattern-based resistance predictions
        pattern_scores = st.session_state.pattern_scores
        
        if pattern_scores.get(1, 0) > 5:  # Unhappiness culture
            predictions.append("Will resist positive suggestions as 'fake' or 'temporary'")
        
        if pattern_scores.get(3, 0) > 5:  # Systematic mistrust
            predictions.append("May be skeptical of therapist intentions and process effectiveness")
        
        if pattern_scores.get(8, 0) > 5:  # Inherited missions
            predictions.append("Change may feel like betraying family expectations or values")
        
        if pattern_scores.get(2, 0) > 5:  # Power struggles
            predictions.append("May resist directives and need collaborative approach")
        
        return predictions[:3]  # Top 3 predictions

    def _render_contact_form(self):
        """Render contact form after assessment completion"""
        st.markdown("### Assessment complete - Get your analysis")
        st.write("Provide your contact details to receive your comprehensive behavioral pattern analysis.")
        
        with st.form("assessment_contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full name*", placeholder="Your full name")
                email = st.text_input("Email address*", placeholder="your@email.com")
            
            with col2:
                phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
                urgency = st.selectbox(
                    "How urgent is your main concern?",
                    ["Select urgency level...", "Extremely urgent", "Very urgent", "Moderately urgent", "Not urgent"]
                )
            
            primary_concern = st.text_area(
                "Primary concern*",
                placeholder="What specific issue brought you to this assessment?",
                height=100
            )
            
            next_step = st.selectbox(
                "Preferred next step:",
                ["Select preference...", "Schedule discovery call", "Book transformation package", "Request detailed analysis first"]
            )
            
            submitted = st.form_submit_button("Get my analysis", type="primary")
            
            if submitted:
                if self._validate_contact_form(name, email, primary_concern, urgency, next_step):
                    self._save_contact_info(name, email, phone, urgency, primary_concern, next_step)
                    self._send_assessment_results()
                    st.session_state.contact_provided = True
                    st.rerun()

    def _validate_contact_form(self, name, email, concern, urgency, next_step):
        """Validate contact form inputs"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        
        if not email.strip():
            errors.append("Email is required")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append("Please enter a valid email address")
        
        if not concern.strip():
            errors.append("Primary concern is required")
        
        if urgency == "Select urgency level...":
            errors.append("Please select urgency level")
        
        if next_step == "Select preference...":
            errors.append("Please select preferred next step")
        
        for error in errors:
            st.error(f"❌ {error}")
        
        return len(errors) == 0

    def _save_contact_info(self, name, email, phone, urgency, concern, next_step):
        """Save contact information"""
        st.session_state.contact_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'urgency': urgency,
            'primary_concern': concern,
            'next_step': next_step,
            'timestamp': datetime.now().isoformat()
        }

    def _send_assessment_results(self):
        """Send comprehensive assessment results via email"""
        try:
            from utils.email_handler import send_assessment_results_email
            
            # Prepare comprehensive data package
            assessment_data = {
                'name': st.session_state.contact_info['name'],
                'email': st.session_state.contact_info['email'],
                'phone': st.session_state.contact_info.get('phone', 'Not provided'),
                'urgency': st.session_state.contact_info['urgency'],
                'primary_concern': st.session_state.contact_info['primary_concern'],
                'next_step': st.session_state.contact_info['next_step'],
                'form_type': 'Advanced Behavioral Pattern Assessment',
                'assessment_results': st.session_state.assessment_results,
                'raw_responses': st.session_state.assessment_responses,
                'clinical_template': self._generate_clinical_template(),
                'response_transcript': self._generate_response_transcript(),
                'total_questions': len(st.session_state.assessment_responses),
                'completion_rate': '100%',
                'timestamp': datetime.now().isoformat()
            }
            
            success = send_assessment_results_email(assessment_data)
            
            if success:
                st.success("✅ Assessment results sent successfully!")
            else:
                st.warning("⚠️ Assessment completed, but email notification failed.")
                
        except Exception as e:
            st.error(f"Error sending results: {str(e)}")

    def _generate_clinical_template(self):
        """Generate comprehensive clinical template"""
        results = st.session_state.assessment_results
        contact = st.session_state.contact_info
        
        # Get top patterns
        pattern_scores = results.get('pattern_scores', {})
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
        secondary = sorted_patterns[1] if len(sorted_patterns) > 1 else (None, 0)
        tertiary = sorted_patterns[2] if len(sorted_patterns) > 2 else (None, 0)
        
        template = f"""
**RAPID CLINICAL ANALYSIS REPORT**
Client: {contact['name']} | Assessment Date: {datetime.now().strftime('%Y-%m-%d')}
Total Questions: {results['total_questions_answered']} | Quality Score: High

═══ DOMINANT PATTERN CONSTELLATION ═══
🔴 PRIMARY: {self.patterns.get(dominant[0], 'None detected')} (Severity: {dominant[1]}/8)
🟡 SECONDARY: {self.patterns.get(secondary[0], 'None detected')} (Severity: {secondary[1]}/8)  
🟢 TERTIARY: {self.patterns.get(tertiary[0], 'None detected')} (Severity: {tertiary[1]}/8)

═══ THERAPEUTIC INTELLIGENCE ═══
🎯 SESSION 1 PRIORITY: Map {self.patterns.get(dominant[0], 'primary')} and {self.patterns.get(secondary[0], 'secondary')} patterns
⚡ SESSION 2 TARGET: Neural rewiring targeting {self.patterns.get(dominant[0], 'primary pattern')}
🔄 SESSION 3 CONTINGENCY: Reinforcement if {self.patterns.get(dominant[0], 'primary pattern')} shows resistance

🚫 PREDICTED RESISTANCE POINTS:
"""
        
        for i, prediction in enumerate(results.get('resistance_predictions', []), 1):
            template += f"{i}. {prediction}\n"
        
        template += f"""
⚠️  CLINICAL ALERTS:
   Risk Level: {results.get('readiness_metrics', {}).get('risk_level', 'Low')}
   Complexity: {results.get('readiness_metrics', {}).get('complexity', 'Medium')}
   Adaptive Pools Triggered: {len(results.get('adaptive_triggered', []))}
   
═══ CHANGE READINESS MATRIX ═══
Urgency Level: {results.get('readiness_metrics', {}).get('urgency_level', 5)}/10
Overall Prognosis: {'Excellent' if results.get('readiness_metrics', {}).get('urgency_level', 5) > 7 else 'Good'}

═══ PRECISE INTERVENTION BLUEPRINT ═══
Communication Style: {self._determine_communication_style()}
Recommended Approach: {self._determine_therapeutic_approach()}
Avoid Language: {self._determine_avoid_language()}
"""
        
        return template

    def _determine_communication_style(self):
        """Determine optimal communication style based on patterns"""
        pattern_scores = st.session_state.pattern_scores
        
        if pattern_scores.get(3, 0) > 5:  # High mistrust
            return "Gentle, transparent, evidence-based"
        elif pattern_scores.get(2, 0) > 5:  # High power struggles
            return "Collaborative, non-directive"
        elif pattern_scores.get(5, 0) > 5:  # High doing vs being
            return "Analytical, process-focused"
        else:
            return "Direct, supportive"

    def _determine_therapeutic_approach(self):
        """Determine optimal therapeutic approach"""
        dominant_pattern = st.session_state.assessment_results.get('dominant_pattern', (None, 0))[0]
        
        approaches = {
            1: "Focus on permission for happiness and positive expectation installation",
            2: "Collaborative power-sharing, avoid control language",
            3: "Build safety and trust gradually, use evidence-based explanations", 
            4: "Integration work, both/and thinking, expand possibility frameworks",
            5: "Value intrinsic worth, separate being from doing",
            6: "Authentic self integration across contexts",
            7: "Self-care as strength, boundary setting skills",
            8: "Differentiate personal desires from inherited expectations",
            9: "Context-independent strength building"
        }
        
        return approaches.get(dominant_pattern, "Standard rapid transformation approach")

    def _determine_avoid_language(self):
        """Determine language to avoid based on patterns"""
        pattern_scores = st.session_state.pattern_scores
        avoid_terms = []
        
        if pattern_scores.get(1, 0) > 5:
            avoid_terms.append("'positive thinking', 'just be happy'")
        if pattern_scores.get(2, 0) > 5:
            avoid_terms.append("'you must', 'you should'")
        if pattern_scores.get(3, 0) > 5:
            avoid_terms.append("'trust me', 'don't worry'")
        
        return ", ".join(avoid_terms) if avoid_terms else "Standard therapeutic language appropriate"

    def _generate_response_transcript(self):
        """Generate complete response transcript"""
        transcript = []
        
        for q_id in sorted(st.session_state.assessment_responses.keys()):
            response_data = st.session_state.assessment_responses[q_id]
            question = self._get_question_by_id(q_id)
            
            transcript.append({
                'question_id': q_id,
                'question_text': response_data['question_text'],
                'response': response_data['response'],
                'question_type': response_data['question_type'],
                'timestamp': response_data['timestamp'],
                'clinical_relevance': self._get_clinical_relevance(q_id, question)
            })
        
        return transcript

    def _get_clinical_relevance(self, q_id, question):
        """Get clinical relevance of question response"""
        if not question:
            return "Unknown relevance"
        
        patterns = question.get('patterns')
        if isinstance(patterns, list):
            pattern_names = [self.patterns.get(p) for p in patterns if p is not None]
            return f"Indicates: {', '.join(filter(None, pattern_names))}"
        elif isinstance(patterns, str):
            return f"Measures: {patterns.replace('_', ' ').title()}"
        else:
            return "General assessment item"

    def _render_results(self):
        """Render assessment results with paywall for clinical analysis"""
        st.markdown("## Assessment analysis complete")
        st.success("Your comprehensive behavioral pattern analysis has been sent to our clinical team.")
        
        # Show basic summary
        self._render_basic_summary()
        
        # Clinical analysis with paywall
        self._render_clinical_analysis_section()
        
        # Next steps
        self._render_next_steps()

    def _render_basic_summary(self):
        """Render basic assessment summary"""
        results = st.session_state.assessment_results
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Questions completed", results['total_questions_answered'], "Comprehensive analysis")
        
        with col2:
            urgency = results.get('readiness_metrics', {}).get('urgency_level', 5)
            st.metric("Readiness level", f"{urgency}/10", "For transformation")
        
        with col3:
            complexity = results.get('readiness_metrics', {}).get('complexity', 'Medium')
            st.metric("Pattern complexity", complexity, "Clinical assessment")

    def _render_clinical_analysis_section(self):
        """Render clinical analysis with paywall protection"""
        st.markdown("### Clinical pattern analysis")
        
        if PAYWALL_AVAILABLE:
            try:
                paywall = create_clinical_paywall()
                
                assessment_data = {
                    'assessment_results': st.session_state.assessment_results,
                    'assessment_responses': st.session_state.assessment_responses,
                }
                
                contact_info = st.session_state.get('contact_info', {})
                assessment_data.update(contact_info)
                
                if paywall.check_payment_status():
                    paywall.render_premium_analysis(assessment_data)
                else:
                    self._render_analysis_preview()
                    with st.expander("Unlock complete clinical analysis", expanded=False):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading clinical analysis: {str(e)}")
                self._render_analysis_preview()
        else:
            self._render_analysis_preview()

    def _render_analysis_preview(self):
        """Render preview of clinical analysis"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            st.markdown("**Preview - Your dominant patterns:**")
            for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
                pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
                st.write(f"• {pattern_name}: High activation detected")
            
            if len(sorted_patterns) > 2:
                remaining = len(sorted_patterns) - 2
                st.write(f"• Plus {remaining} additional patterns analyzed...")
        
        st.info("Unlock complete analysis for detailed insights, therapeutic priorities, and personalized transformation roadmap.")

    def _render_next_steps(self):
        """Render next steps based on assessment"""
        st.markdown("### Your personalized next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        next_step = contact_info.get('next_step', '')
        
        if 'discovery call' in next_step.lower():
            st.info("We'll contact you to schedule a discovery call to discuss your results.")
        elif 'package' in next_step.lower():
            st.success("You've indicated readiness for transformation. We'll contact you with scheduling options.")
        else:
            st.info("We'll review your assessment and contact you with personalized recommendations.")
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical review** (Within 24 hours): Your responses analyzed for optimal treatment approach
        2. **Personalized contact** (Within 48 hours): Specific recommendations based on your assessment  
        3. **Discovery call** (Optional): Discuss results and answer questions
        4. **Transformation sessions**: Begin your personalized pattern rewiring program
        """)


class AssessPage:
    """Main assessment page component"""
    
    def __init__(self):
        self.assessment = AdaptiveBehavioralAssessment()
    
    def render(self):
        """Render the complete assessment page"""
        self.assessment.render()


def create_assess_page():
    """Factory function to create AssessPage instance"""
    return AssessPage()
