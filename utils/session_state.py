# Add to utils/config.py

class QuizConfig:
    """Enhanced 4-question quiz configuration"""
    
    QUESTIONS = {
        1: {
            "title": "What unwanted pattern would you most like to eliminate?",
            "options": [
                ("🚭", "Quit smoking\nBreak nicotine addiction permanently"),
                ("😰", "Reduce anxiety\nStop panic attacks and overthinking"), 
                ("😴", "Improve sleep\nEnd insomnia and sleep anxiety"),
                ("🍷", "Control drinking\nHealthy relationship with alcohol"),
                ("🍕", "Stop overeating\nBreak emotional eating patterns"),
                ("📱", "Break bad habits\nEliminate destructive behaviors")
            ]
        },
        2: {
            "title": "How long have you been dealing with this pattern?",
            "options": [
                ("🆕", "Less than 6 months\nRecent development"),
                ("📅", "6 months to 2 years\nEstablished pattern"),
                ("⏳", "More than 2 years\nDeep-rooted habit")
            ]
        },
        3: {
            "title": "Which internal pattern most blocks your progress?",
            "options": [
                ("⚔️", "Force and control\n'I must push through resistance'"),
                ("🔒", "Mistrust and defensiveness\n'I can't let my guard down'"),
                ("⚖️", "All-or-nothing thinking\n'It's either perfect or failure'"),
                ("🏃", "Doing addiction\n'My worth depends on productivity'")
            ]
        },
        4: {
            "title": "How ready are you to transform this pattern?",
            "options": [
                ("🤔", "Curious but cautious\nWant to understand the approach first"),
                ("🎯", "Ready to commit\nPrepared to do the inner work"),
                ("🔥", "Desperate for change\nThis pattern must end now"),
                ("🛡️", "Prefer gradual approach\nWant to try other methods first")
            ]
        }
    }
    
    SCORING = {
        1: {  # Unwanted patterns
            "Quit smoking": 30,
            "Reduce anxiety": 25,
            "Improve sleep": 20,
            "Control drinking": 25,
            "Stop overeating": 20,
            "Break bad habits": 25
        },
        2: {  # Duration
            "Less than 6 months": 15,
            "6 months to 2 years": 20,
            "More than 2 years": 25
        },
        3: {  # Blocking mechanisms
            "Force and control": 20,
            "Mistrust and defensiveness": 15,
            "All-or-nothing thinking": 25,
            "Doing addiction": 30
        },
        4: {  # Readiness levels
            "Curious but cautious": 15,
            "Ready to commit": 30,
            "Desperate for change": 25,
            "Prefer gradual approach": 5
        }
    }
