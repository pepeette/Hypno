# """
# Enhanced Clinical Email Handler for Hypnotherapy Assessment
# Comprehensive therapeutic analysis with actionable treatment recommendations
# """
# import smtplib
# import os
# import streamlit as st
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime


# class ClinicalEmailHandler:
#     """Enhanced email handler for comprehensive clinical assessment results"""

#     def __init__(self):
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587

#         try:
#             self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
#             self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
#             self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
#         except Exception as e:
#             print(f"[DEBUG] Error accessing secrets: {e}")
#             self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = os.environ.get("GMAIL_APP_PASSWORD")

#     def send_clinical_assessment_results(self, clinical_data):
#         """Send comprehensive clinical assessment with therapeutic analysis"""
#         try:
#             print("[DEBUG] Sending clinical assessment results email")
            
#             # Determine clinical priority for subject line
#             urgency = clinical_data.get('urgency', 'Medium priority')
#             safety_flags = clinical_data.get('assessment_results', {}).get('clinical_flags', [])
#             priority_flag = self._get_clinical_priority_flag(urgency, safety_flags)
            
#             msg = self._build_email(
#                 subject=f"{priority_flag} Clinical Behavioral Assessment - {clinical_data.get('name', 'Unknown Client')}",
#                 body=self._format_clinical_assessment_body(clinical_data)
#             )
            
#             return self._dispatch(msg, clinical_data, "Clinical Assessment Results")
            
#         except Exception as e:
#             print(f"[ERROR] Exception in send_clinical_assessment_results: {e}")
#             import traceback
#             traceback.print_exc()
#             return False

#     def _get_clinical_priority_flag(self, urgency, safety_flags):
#         """Get clinical priority flag for email subject"""
#         if 'suicide_risk' in safety_flags:
#             return "🔴 CRISIS"
#         elif 'high_risk_client' in safety_flags:
#             return "🟠 HIGH RISK"
#         elif 'extremely urgent' in urgency.lower():
#             return "🔴 URGENT"
#         elif 'very urgent' in urgency.lower():
#             return "🟡 HIGH PRIORITY"
#         elif 'moderately urgent' in urgency.lower():
#             return "🟢 PRIORITY"
#         else:
#             return "📋 STANDARD"

#     def _format_clinical_assessment_body(self, data):
#         """Format comprehensive clinical email with therapeutic precision"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Extract core data
#             name = data.get('name', 'Unknown client')
#             email = data.get('email', 'Unknown email')
#             phone = data.get('phone', 'Not provided')
#             urgency = data.get('urgency', 'Not specified')
#             availability = ', '.join(data.get('availability', [])) or 'Not specified'
#             previous_therapy = data.get('previous_therapy', 'Not specified')
#             additional_info = data.get('additional_info', 'None provided')
            
#             # Get assessment results
#             assessment_results = data.get('assessment_results', {})
#             presenting_problem = assessment_results.get('presenting_problem', {})
#             pattern_constellation = assessment_results.get('pattern_constellation', {})
#             behavioral_chain = assessment_results.get('behavioral_chain', {})
#             resistance_analysis = assessment_results.get('resistance_analysis', {})
#             hypnotic_profile = assessment_results.get('hypnotic_profile', {})
#             safety_assessment = assessment_results.get('safety_assessment', {})
#             treatment_recommendations = assessment_results.get('treatment_recommendations', {})
#             outcome_predictions = assessment_results.get('outcome_predictions', {})
            
#             # Get clinical flags
#             clinical_flags = assessment_results.get('clinical_flags', [])
            
#             # Get script guidance
#             script_guide = data.get('hypnotherapy_script_guide', {})
            
#             # Build comprehensive clinical email
#             body = f"""
# 🧠 CLINICAL BEHAVIORAL ASSESSMENT - THERAPEUTIC ANALYSIS
# Assessment Completed: {timestamp}
# Assessment Type: Comprehensive Clinical Analysis for Hypnotherapy Intervention

# ═══════════════════════════════════════════════════════════

# 👤 CLIENT PROFILE & INTAKE
# Name: {name}
# Email: {email}
# Phone: {phone}
# Urgency Level: {urgency}
# Preferred Availability: {availability}
# Previous Therapy: {previous_therapy}
# Additional Context: {additional_info}

# Clinical Priority: {presenting_problem.get('clinical_priority', 'Standard')}
# Assessment Completion: {data.get('completion_rate', '100%')}
# Total Questions Answered: {data.get('total_questions', 'Unknown')}

# ═══════════════════════════════════════════════════════════

# 🎯 PRESENTING PROBLEM ANALYSIS

# TARGET BEHAVIOR FOR ELIMINATION:
# Primary Complaint: {presenting_problem.get('presenting_problem', 'Not specified')}
# Specific Unwanted Behavior: {presenting_problem.get('target_behavior', 'Not specified')}
# Duration: {presenting_problem.get('duration', 'Not specified')}
# Life Interference Level: {presenting_problem.get('impact_level', 'Not specified')}

# IMMEDIATE ACTION REQUIRED: {self._get_action_timeline(urgency, clinical_flags)}

# ═══════════════════════════════════════════════════════════

# 🔗 BEHAVIORAL CHAIN MAPPING (Situation-Emotion-Reaction)

# TRIGGERING SITUATION:
# {behavioral_chain.get('triggering_situation', 'Not provided')}

# PRE-BEHAVIOR THOUGHTS:
# {behavioral_chain.get('pre_behavior_thoughts', 'Not provided')}

# PHYSICAL SENSATIONS:
# {behavioral_chain.get('physical_sensations', 'Not provided')}

# PRIMARY EMOTION:
# {behavioral_chain.get('primary_emotion', 'Not provided')}

# BEHAVIORAL RESPONSE:
# {behavioral_chain.get('behavioral_response', 'Not provided')}

# INTERVENTION POINT: {self._identify_intervention_point(behavioral_chain)}

# ═══════════════════════════════════════════════════════════

# 📊 DOMINANT PATTERN CONSTELLATION
# """
            
#             # Add pattern analysis
#             dominant = pattern_constellation.get('dominant')
#             secondary = pattern_constellation.get('secondary', [])
#             tertiary = pattern_constellation.get('tertiary', [])
            
#             if dominant:
#                 body += f"""
# 🔴 PRIMARY PATTERN: {dominant['pattern_name']}
#    ├─ Activation Score: {dominant['score']}/12 ({dominant['severity']} intensity)
#    ├─ Clinical Manifestation: {self._get_clinical_manifestation(dominant['pattern_id'], dominant['score'])}
#    ├─ Therapeutic Approach: {self._get_therapeutic_approach(dominant['pattern_id'])}
#    └─ Session 1 Priority: {treatment_recommendations.get('session_1_focus', 'Assessment and rapport building')}
# """
            
#             if secondary:
#                 for i, pattern in enumerate(secondary[:2]):
#                     indicator = "🟡" if i == 0 else "🟢"
#                     level = ["SECONDARY", "TERTIARY"][i]
#                     body += f"""
# {indicator} {level} PATTERN: {pattern['pattern_name']}
#    ├─ Activation Score: {pattern['score']}/12 ({pattern['severity']} intensity)
#    ├─ Interaction Effect: {self._get_pattern_interaction(dominant['pattern_id'] if dominant else 0, pattern['pattern_id'])}
#    └─ Treatment Integration: {self._get_integration_strategy(pattern['pattern_id'])}
# """
            
#             # Additional patterns summary
#             if tertiary:
#                 body += f"\nADDITIONAL PATTERNS DETECTED: {len(tertiary)}\n"
#                 for pattern in tertiary:
#                     body += f"   • {pattern['pattern_name']}: {pattern['score']}/12\n"

#             body += f"""
# ═══════════════════════════════════════════════════════════

# ⚡ HYPNOTHERAPY SCRIPT DEVELOPMENT GUIDE

# INDUCTION STRATEGY:
# Recommended Approach: {hypnotic_profile.get('hypnotic_approach', 'Standard approach')}
# Therapeutic Style: {hypnotic_profile.get('therapeutic_style', 'Collaborative')}
# Trance Capacity: {hypnotic_profile.get('trance_capacity', 'Unknown')}

# SUGGESTION FRAMEWORK:
# Primary Suggestions: {self._format_primary_suggestions(dominant, behavioral_chain)}
# Secondary Suggestions: {self._format_secondary_suggestions(secondary)}
# Language Style: {script_guide.get('suggestion_style', 'Direct positive suggestions')}

# THERAPEUTIC LANGUAGE OPTIMIZATION:
# ✅ POWER WORDS TO USE: {', '.join(script_guide.get('therapeutic_language', {}).get('power_words', ['strength', 'natural', 'capable']))}
# ❌ LANGUAGE TO AVOID: {', '.join(script_guide.get('therapeutic_language', {}).get('avoid_language', ['Standard cautions apply']))}
# 🎯 CLIENT'S OWN LANGUAGE: {self._extract_client_language(script_guide)}

# SPECIFIC HYPNOTIC COMMANDS:
# • "When {behavioral_chain.get('triggering_situation', '[trigger]')} occurs, you naturally {self._get_desired_response(behavioral_chain)}"
# • "The old pattern of {presenting_problem.get('target_behavior', '[behavior]')} simply dissolves"  
# • "You find yourself responding with {self._get_new_response_pattern(dominant)}"

# ═══════════════════════════════════════════════════════════

# 🚫 RESISTANCE ANALYSIS & MANAGEMENT

# SECONDARY GAIN IDENTIFICATION:
# {resistance_analysis.get('secondary_gains', 'Not identified')}

# CHANGE FEARS:
# {resistance_analysis.get('change_fears', 'Not identified')}

# RELATIONSHIP IMPACT CONCERNS:
# {resistance_analysis.get('relationship_impact', 'Not identified')}

# PREDICTED RESISTANCE POINTS:
# """
            
#             # Add resistance predictions
#             resistance_predictions = resistance_analysis.get('predictions', [])
#             if resistance_predictions:
#                 for i, prediction in enumerate(resistance_predictions, 1):
#                     body += f"   {i}. {prediction}\n"
#                     body += f"      └─ Management Strategy: {self._get_resistance_management_strategy(prediction)}\n"
#             else:
#                 body += "   • Low resistance predicted based on assessment responses\n"

#             body += f"""
# RESISTANCE MANAGEMENT PROTOCOL:
# {self._generate_resistance_protocol(resistance_analysis, dominant)}

# ═══════════════════════════════════════════════════════════

# ⚠️  CLINICAL SAFETY ASSESSMENT

# RISK LEVEL: {safety_assessment.get('risk_level', 'Low')}
# """
            
#             # Safety considerations
#             if clinical_flags:
#                 body += "CLINICAL FLAGS DETECTED:\n"
#                 for flag in clinical_flags:
#                     body += f"   🔺 {flag.replace('_', ' ').title()}\n"
#                     body += f"      └─ Protocol: {self._get_safety_protocol(flag)}\n"
            
#             contraindications = safety_assessment.get('contraindications', [])
#             if contraindications:
#                 body += "\nCONTRAINDICATIONS:\n"
#                 for contraindication in contraindications:
#                     body += f"   ❌ {contraindication}\n"
            
#             special_considerations = safety_assessment.get('special_considerations', [])
#             if special_considerations:
#                 body += "\nSPECIAL CONSIDERATIONS:\n"
#                 for consideration in special_considerations:
#                     body += f"   ⚠️  {consideration}\n"
            
#             referral_needed = safety_assessment.get('referral_needed', False)
#             if referral_needed:
#                 body += "\n🏥 REFERRAL REQUIRED: Coordinate with medical/psychiatric care before hypnotherapy\n"

#             body += f"""
# ═══════════════════════════════════════════════════════════

# 📋 SESSION-BY-SESSION TREATMENT PROTOCOL

# SESSION 1 - ASSESSMENT & PATTERN INTERRUPTION:
# Focus: {treatment_recommendations.get('session_1_focus', 'Rapport building and initial intervention')}
# Techniques: {', '.join(treatment_recommendations.get('technique_recommendations', [])[:3])}
# Goals: 
# ├─ Establish therapeutic rapport using {hypnotic_profile.get('therapeutic_style', 'collaborative approach')}
# ├─ Map client's internal experience of the problem
# ├─ Install initial pattern interruption at: {self._identify_intervention_point(behavioral_chain)}
# └─ Test hypnotic responsiveness and adjust approach

# SESSION 2 - ROOT TRANSFORMATION:
# Focus: {self._get_session_2_focus(dominant, resistance_analysis)}
# Techniques: {self._get_session_2_techniques(dominant, clinical_flags)}
# Goals:
# ├─ Address root cause: {self._get_root_cause_focus(dominant)}
# ├─ Transform core limiting belief: {self._extract_core_belief(behavioral_chain)}
# ├─ Install new identity: {self._get_new_identity_installation(dominant)}
# └─ Strengthen new response pattern

# SESSION 3 - INTEGRATION & FUTURE-PACING:
# Focus: Consolidation and real-world application
# Techniques: Future pacing, anchor strengthening, relapse prevention
# Goals:
# ├─ Test integration across life contexts
# ├─ Strengthen new automatic responses
# ├─ Address any remaining resistance
# └─ Establish maintenance protocol

# HOMEWORK & INTEGRATION:
# {self._generate_homework_protocol(dominant, hypnotic_profile)}

# ═══════════════════════════════════════════════════════════

# 📈 THERAPEUTIC OUTCOME PREDICTIONS

# RAPID CHANGE PROBABILITY: {outcome_predictions.get('rapid_change_probability', 'Unknown')}
# ESTIMATED TREATMENT DURATION: {outcome_predictions.get('estimated_sessions', 'Unknown')}
# OVERALL PROGNOSIS: {outcome_predictions.get('prognosis', 'Fair')}

# SUCCESS PREDICTORS:
# """
            
#             # Success factors
#             success_factors = outcome_predictions.get('success_factors', [])
#             if success_factors:
#                 for factor in success_factors:
#                     body += f"   ✅ {factor}\n"
#             else:
#                 body += "   ✅ Assessment completed thoroughly\n"
#                 body += f"   ✅ {urgency} indicates motivation\n"
#                 if not clinical_flags:
#                     body += "   ✅ No significant safety concerns\n"
            
#             # Challenge factors
#             challenge_factors = outcome_predictions.get('challenge_factors', [])
#             if challenge_factors:
#                 body += "\nCHALLENGE FACTORS:\n"
#                 for factor in challenge_factors:
#                     body += f"   ⚠️  {factor}\n"
            
#             if clinical_flags:
#                 body += "\nCLINICAL COMPLEXITY:\n"
#                 for flag in clinical_flags:
#                     body += f"   ⚠️  {flag.replace('_', ' ').title()} requires specialized approach\n"

#             body += f"""
# EXPECTED TIMELINE:
# Week 1: {self._get_week_1_prediction(outcome_predictions)}
# Week 2-4: {self._get_month_1_prediction(outcome_predictions)}
# 3 Months: {self._get_3month_prediction(outcome_predictions)}

# ═══════════════════════════════════════════════════════════

# 💬 THERAPEUTIC RELATIONSHIP OPTIMIZATION

# RAPPORT BUILDING STRATEGY:
# {self._get_rapport_strategy(dominant, hypnotic_profile)}

# COMMUNICATION STYLE:
# Preferred Approach: {hypnotic_profile.get('therapeutic_style', 'Collaborative')}
# Client Guidance Preference: {hypnotic_profile.get('guidance_preference', 'Not specified')}
# Therapeutic Pace: {self._determine_therapeutic_pace(urgency, clinical_flags)}

# EXPECTED CLIENT BEHAVIOR IN SESSION:
# Authority Response: {self._predict_authority_response(pattern_constellation)}
# Emotional Regulation: {self._predict_emotional_regulation(pattern_constellation, clinical_flags)}
# Change Pace Tolerance: {self._predict_change_tolerance(resistance_analysis)}
# Feedback Style Needed: {self._recommend_feedback_style(pattern_constellation)}

# ═══════════════════════════════════════════════════════════

# 📞 IMMEDIATE ACTION PROTOCOL

# CONTACT TIMELINE: {self._get_contact_timeline(urgency, clinical_flags)}
# PRIORITY LEVEL: {presenting_problem.get('clinical_priority', 'Standard')}

# RECOMMENDED IMMEDIATE ACTIONS:
# {self._generate_immediate_action_plan(urgency, clinical_flags, pattern_constellation)}

# PRE-SESSION PREPARATION:
# 1. Review complete clinical template (attached data)
# 2. Prepare induction style: {script_guide.get('induction_recommendations', 'Standard relaxation')}
# 3. Plan resistance management for: {self._get_primary_resistance_focus(resistance_analysis)}
# 4. Set up safety protocols if needed: {self._get_safety_prep(clinical_flags)}

# ═══════════════════════════════════════════════════════════

# 📊 COMPLETE CLINICAL DATA SUMMARY

# ASSESSMENT QUALITY: {self._assess_data_quality(data)}
# THERAPEUTIC CONFIDENCE: {self._assess_therapeutic_confidence(assessment_results)}
# INTERVENTION READINESS: {self._assess_intervention_readiness(clinical_flags, resistance_analysis)}

# KEY SUCCESS FACTORS:
# 1. Strong assessment completion indicating client engagement
# 2. Clear behavioral target identified for intervention
# 3. Specific triggering situation mapped for pattern interruption
# 4. {len(pattern_constellation.get('secondary', []))} supporting patterns identified for comprehensive treatment

# CLINICAL TEMPLATE SUMMARY:
# {data.get('clinical_template', 'Template generation error - see raw data below')}

# ═══════════════════════════════════════════════════════════

# 🔧 ASSESSMENT TECHNICAL METADATA
# Algorithm Version: Clinical Assessment v2.0
# Adaptive Logic: {len(assessment_results.get('adaptive_triggered', []))} specialized modules activated
# Pattern Detection: Advanced constellation mapping with therapeutic precision
# Data Quality: {self._assess_overall_data_quality(data)}
# Clinical Confidence: {self._assess_clinical_confidence(assessment_results)}

# ⚠️  CONFIDENTIAL: Contains sensitive psychological assessment data
# Clinical use only - Licensed therapist review required
# Client consent obtained for therapeutic purposes

# ═══════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Clinical Assessment System
# Therapeutic Analysis Generated: {timestamp}
# Next Clinical Review: {self._get_next_review_timeline(urgency, clinical_flags)}
# Therapist Assignment: {self._recommend_therapist_type(assessment_results)}
#             """
            
#             return body
            
#         except Exception as e:
#             print(f"[ERROR] Error formatting clinical assessment email: {e}")
#             import traceback
#             traceback.print_exc()
#             return f"""
# 🧠 CLINICAL ASSESSMENT RESULTS - FORMATTING ERROR

# Basic Information:
# Name: {data.get('name', 'Unknown')}
# Email: {data.get('email', 'Unknown')}
# Phone: {data.get('phone', 'Unknown')}
# Urgency: {data.get('urgency', 'Unknown')}
# Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Error Details: {str(e)}

# Raw Clinical Data Available - Manual Review Required
# Complete assessment responses and analysis data preserved
# Please contact technical support for data recovery and manual clinical review.

# Bangkok Hypnotherapy Clinic - Clinical Assessment System
#             """

#     def _get_action_timeline(self, urgency, clinical_flags):
#         """Get immediate action timeline based on risk and urgency"""
#         if 'suicide_risk' in clinical_flags:
#             return "IMMEDIATE - Crisis intervention within 4 hours"
#         elif 'high_risk_client' in clinical_flags:
#             return "URGENT - Contact within 12 hours for safety assessment"
#         elif 'extremely urgent' in urgency.lower():
#             return "HIGH PRIORITY - Contact within 24 hours"
#         elif 'very urgent' in urgency.lower():
#             return "PRIORITY - Contact within 48 hours"
#         else:
#             return "STANDARD - Contact within 72 hours"

#     def _identify_intervention_point(self, behavioral_chain):
#         """Identify optimal intervention point in behavioral chain"""
#         if behavioral_chain.get('pre_behavior_thoughts'):
#             return "Thought pattern interruption before behavioral activation"
#         elif behavioral_chain.get('physical_sensations'):
#             return "Somatic awareness and response modification"
#         elif behavioral_chain.get('triggering_situation'):
#             return "Environmental trigger response retraining"
#         else:
#             return "General pattern interruption and response modification"

#     def _get_clinical_manifestation(self, pattern_id, score):
#         """Get clinical manifestation description"""
#         manifestations = {
#             1: f"Automatic rejection of positive experiences, success sabotage behaviors, guilt about happiness (Score: {score}/12)",
#             2: f"Conflict escalation patterns, need to control or win, defensive responses (Score: {score}/12)",
#             3: f"Hypervigilance in relationships, assumption of negative intent, difficulty receiving help (Score: {score}/12)",
#             4: f"Binary thinking patterns, feeling trapped between extremes, isolation tendencies (Score: {score}/12)",
#             5: f"Self-worth tied to productivity, difficulty with being vs doing, burnout patterns (Score: {score}/12)",
#             6: f"Context-dependent identity shifts, authenticity struggles, compartmentalization (Score: {score}/12)",
#             7: f"Chronic self-neglect, others-first orientation, boundary difficulties (Score: {score}/12)",
#             8: f"Living inherited dreams/expectations, guilt about personal desires, family loyalty conflicts (Score: {score}/12)",
#             9: f"Context-dependent boundary collapse, inconsistent values expression (Score: {score}/12)"
#         }
#         return manifestations.get(pattern_id, f"Pattern-specific behavioral manifestations (Score: {score}/12)")

#     def _get_therapeutic_approach(self, pattern_id):
#         """Get specific therapeutic approach for pattern"""
#         approaches = {
#             1: "Permission installation therapy, positive expectation programming, success tolerance building",
#             2: "Collaborative empowerment approach, shared control frameworks, non-directive techniques",
#             3: "Safety-first trust building, transparent process explanation, evidence-based interventions",
#             4: "Integration-focused therapy, both/and thinking expansion, possibility framework development",
#             5: "Being-centered identity work, intrinsic worth installation, doing/being separation",
#             6: "Authentic self integration, consistent identity development across contexts",
#             7: "Self-care strength reframing, healthy boundary establishment, self-worth building",
#             8: "Personal desire differentiation, respectful family loyalty reframing, authentic vision development",
#             9: "Context-independent strength building, consistent value expression training"
#         }
#         return approaches.get(pattern_id, "Individualized pattern-specific intervention")

#     def _get_pattern_interaction(self, primary_pattern, secondary_pattern):
#         """Analyze interaction between patterns"""
#         interactions = {
#             (1, 3): "Unhappiness culture reinforced by mistrust - expect resistance to positive suggestions",
#             (2, 3): "Power struggles amplified by mistrust - use extra collaborative approach",
#             (1, 7): "Unhappiness culture with self-sacrifice - address guilt about self-care",
#             (5, 7): "Doing/being confusion with self-neglect - focus on inherent worth",
#             (8, 7): "Inherited missions with self-sacrifice - explore family loyalty vs. self-care"
#         }
        
#         key = (primary_pattern, secondary_pattern)
#         return interactions.get(key, f"Monitor interaction between Pattern {primary_pattern} and Pattern {secondary_pattern}")

#     def _get_integration_strategy(self, pattern_id):
#         """Get integration strategy for secondary patterns"""
#         strategies = {
#             1: "Address alongside primary pattern - unhappiness patterns often co-occur",
#             2: "Monitor for power struggles during therapy - use invitation language",
#             3: "Build trust gradually - explain each intervention rationally",
#             4: "Expand either/or thinking - show multiple possibilities",
#             5: "Separate worth from achievement - reinforce being value",
#             6: "Support authentic expression - consistency across contexts",
#             7: "Reframe self-care as strength - necessary for helping others",
#             8: "Honor family while expanding personal choice",
#             9: "Strengthen boundaries across all contexts"
#         }
#         return strategies.get(pattern_id, "Standard integration approach")

#     def _format_primary_suggestions(self, dominant, behavioral_chain):
#         """Format primary hypnotic suggestions"""
#         if not dominant:
#             return "Standard positive programming based on target behavior"
        
#         pattern_id = dominant['pattern_id']
#         target_behavior = behavioral_chain.get('behavioral_response', 'unwanted behavior')
        
#         suggestions = {
#             1: f"You give yourself full permission to experience happiness and success naturally",
#             2: f"You find collaboration more satisfying than control, naturally choosing cooperation",
#             3: f"You trust your ability to assess situations accurately while remaining open to others",
#             4: f"You see multiple possibilities in every situation, finding creative both/and solutions",
#             5: f"Your worth exists independent of what you do, allowing you to simply be",
#             6: f"You express your authentic self consistently across all areas of life",
#             7: f"You care for yourself with the same love you show others, naturally and easily",
#             8: f"You honor your family while following your own authentic path with confidence",
#             9: f"You maintain your strength and boundaries in every context, naturally and consistently"
#         }
        
#         return suggestions.get(pattern_id, f"You naturally respond differently when {behavioral_chain.get('triggering_situation', 'the situation')} occurs")

#     def _format_secondary_suggestions(self, secondary_patterns):
#         """Format secondary supporting suggestions"""
#         if not secondary_patterns:
#             return "Supporting suggestions based on assessment responses"
        
#         suggestions = []
#         for pattern in secondary_patterns[:2]:
#             pattern_id = pattern['pattern_id']
#             secondary_suggestions = {
#                 1: "Positive experiences feel natural and deserved",
#                 2: "Collaboration brings deeper satisfaction than control",
#                 3: "You trust your inner wisdom while staying open to others",
#                 4: "Multiple possibilities exist in every situation",
#                 5: "Your value exists simply because you are",
#                 6: "Authenticity flows naturally in every context",
#                 7: "Self-care strengthens your ability to help others",
#                 8: "Personal dreams honor your family in new ways",
#                 9: "Your strength remains consistent everywhere"
#             }
#             suggestion = secondary_suggestions.get(pattern_id, f"Pattern {pattern_id} positive programming")
#             suggestions.append(suggestion)
        
#         return "; ".join(suggestions)

#     def _extract_client_language(self, script_guide):
#         """Extract client's own language for suggestions"""
#         client_language = script_guide.get('therapeutic_language', {}).get('client_language', [])
#         if client_language:
#             return f"Use client's own words: {', '.join(client_language[:3])}"
#         else:
#             return "Use client's emotional vocabulary from text responses"

#     def _get_desired_response(self, behavioral_chain):
#         """Get desired response pattern"""
#         unwanted = behavioral_chain.get('behavioral_response', '')
#         if 'angry' in unwanted.lower() or 'yell' in unwanted.lower():
#             return "remain calm and respond thoughtfully"
#         elif 'avoid' in unwanted.lower() or 'withdraw' in unwanted.lower():
#             return "stay present and engage constructively"
#         elif 'worry' in unwanted.lower() or 'anxious' in unwanted.lower():
#             return "feel calm and confident"
#         else:
#             return "respond with your natural strength and wisdom"

#     def _get_new_response_pattern(self, dominant):
#         """Get new response pattern based on dominant pattern"""
#         if not dominant:
#             return "strength and confidence"
        
#         pattern_id = dominant['pattern_id']
#         responses = {
#             1: "natural happiness and confidence",
#             2: "collaborative strength and mutual respect",
#             3: "grounded trust and open communication",
#             4: "creative flexibility and integrated solutions",
#             5: "peaceful presence and inherent worth",
#             6: "authentic consistency and genuine expression",
#             7: "balanced self-care and loving boundaries",
#             8: "personal authenticity while honoring family",
#             9: "consistent strength and clear boundaries"
#         }
#         return responses.get(pattern_id, "natural strength and wisdom")

#     def _get_resistance_management_strategy(self, prediction):
#         """Get specific resistance management strategy"""
#         if "unconsciously resist" in prediction:
#             return "Address secondary gains directly - 'Part of you might miss...' exploration"
#         elif "skepticism" in prediction:
#             return "Provide evidence-based explanations, use client's own logic system"
#         elif "directive approaches" in prediction:
#             return "Use invitation language: 'You might find...' rather than 'You will...'"
#         elif "positive suggestions" in prediction:
#             return "Start with permission to be skeptical, validate current feelings first"
#         else:
#             return "Monitor closely and adapt approach based on client response"

#     def _generate_resistance_protocol(self, resistance_analysis, dominant):
#         """Generate comprehensive resistance management protocol"""
#         if not dominant:
#             return "Standard resistance management - collaborative approach with ongoing calibration"
        
#         pattern_id = dominant['pattern_id']
        
#         protocols = {
#             1: "Unhappiness Culture Protocol: Start with permission to be unhappy, validate struggles, gradually introduce possibility of happiness",
#             2: "Power Struggle Protocol: Avoid all directive language, use collaborative discovery, let client lead insights",
#             3: "Mistrust Protocol: Transparent explanation of every technique, evidence-based rationale, client choice at each step",
#             4: "Binary Thinking Protocol: Introduce both/and language, explore nuance, expand possibility thinking",
#             5: "Achievement Pressure Protocol: Separate worth from performance, emphasize being over doing",
#             6: "Authenticity Protocol: Support real self expression, consistency across contexts",
#             7: "Self-Sacrifice Protocol: Reframe self-care as strength that enables helping others",
#             8: "Family Loyalty Protocol: Honor family values while expanding personal choice",
#             9: "Boundary Protocol: Strengthen consistent values expression across all contexts"
#         }
        
#         base_protocol = protocols.get(pattern_id, "Standard resistance management")
        
#         # Add secondary gain considerations
#         secondary_gains = resistance_analysis.get('secondary_gains', '')
#         if secondary_gains and 'not' not in secondary_gains.lower():
#             base_protocol += f"\nSecondary Gain Management: Address benefits client receives from current pattern - explore in session 1"
        
#         return base_protocol

#     def _get_safety_protocol(self, flag):
#         """Get specific safety protocol for clinical flag"""
#         protocols = {
#             'suicide_risk': "IMMEDIATE crisis intervention, safety plan, emergency contacts, do not proceed with hypnotherapy until stabilized",
#             'high_risk_client': "Specialized assessment, possible referral, modified hypnotherapy approach with safety monitoring",
#             'dissociation_risk': "Grounding techniques, avoid regression, maintain present-moment awareness, shorter sessions",
#             'medication_considerations': "Coordinate with prescribing physician, understand medication effects on hypnotic response",
#             'substance_considerations': "Address substance use patterns, possible delay of hypnotherapy until stabilized"
#         }
#         return protocols.get(flag, "Standard clinical precautions apply")

#     def _get_session_2_focus(self, dominant, resistance_analysis):
#         """Get session 2 focus based on patterns and resistance"""
#         if not dominant:
#             return "Core belief transformation and new identity installation"
        
#         pattern_id = dominant['pattern_id']
        
#         # Check for secondary gains that need addressing
#         secondary_gains = resistance_analysis.get('secondary_gains', '')
#         if secondary_gains and 'not' not in secondary_gains.lower():
#             return f"Address secondary gains first, then {self._get_core_transformation(pattern_id)}"
#         else:
#             return self._get_core_transformation(pattern_id)

#     def _get_core_transformation(self, pattern_id):
#         """Get core transformation focus for pattern"""
#         transformations = {
#             1: "Transform core belief about deserving happiness, install positive expectation as natural state",
#             2: "Transform need for control into preference for collaboration, install shared power as strength",
#             3: "Transform hypervigilance into grounded discernment, install basic trust with wisdom",
#             4: "Transform binary thinking into integration, install both/and possibility consciousness",
#             5: "Transform worth-achievement connection, install intrinsic value and being consciousness",
#             6: "Transform fragmented identity into integrated authenticity across all contexts",
#             7: "Transform self-sacrifice into balanced care, install self-care as strength for service",
#             8: "Transform inherited dreams into personal authentic vision while honoring family",
#             9: "Transform context-dependent weakness into consistent strength and boundary integrity"
#         }
#         return transformations.get(pattern_id, "Core limiting belief transformation and new identity installation")

#     def _get_session_2_techniques(self, dominant, clinical_flags):
#         """Get specific techniques for session 2"""
#         if not dominant:
#             return "Standard regression and reframe techniques"
        
#         pattern_id = dominant['pattern_id']
        
#         # Modify techniques based on safety flags
#         if 'dissociation_risk' in clinical_flags:
#             base_techniques = "Present-moment techniques, cognitive reframing, avoid regression"
#         else:
#             base_techniques = {
#                 1: "Age regression to install early permission for happiness, positive memory installation",
#                 2: "Parts therapy for control vs. collaboration, inner negotiation techniques",
#                 3: "Trust-building visualization, evidence installation, safety anchor strengthening",
#                 4: "Integration imagery, both/and visualization, possibility expansion techniques",
#                 5: "Identity regression, inherent worth installation, being state anchoring",
#                 6: "Identity integration work, authentic self visualization across contexts",
#                 7: "Self-care strength installation, boundary visualization, balanced care modeling",
#                 8: "Family honor visualization while following personal path, loyalty reframe",
#                 9: "Strength consistency installation, boundary integrity across all contexts"
#             }.get(pattern_id, "Standard transformation techniques")
        
#         return base_techniques

#     def _get_root_cause_focus(self, dominant):
#         """Get root cause focus for session 2"""
#         if not dominant:
#             return "Core limiting belief system"
        
#         pattern_id = dominant['pattern_id']
#         focuses = {
#             1: "Early messages about happiness being dangerous or temporary",
#             2: "Early powerlessness leading to need for control",
#             3: "Early trust violations or betrayals",
#             4: "Early forced either/or choices, black/white family dynamics",
#             5: "Early conditional love based on performance/achievement",
#             6: "Early need to be different people for safety or acceptance",
#             7: "Early role as family caretaker or emotional support",
#             8: "Early pressure to fulfill family dreams or honor sacrifices",
#             9: "Early contexts where strength led to harm or rejection"
#         }
#         return focuses.get(pattern_id, "Core belief formation and early conditioning")

#     def _extract_core_belief(self, behavioral_chain):
#         """Extract core limiting belief from behavioral chain"""
#         thoughts = behavioral_chain.get('pre_behavior_thoughts', '')
#         if thoughts:
#             # Extract potential limiting belief from thoughts
#             if 'not' in thoughts.lower() and ('good' in thoughts.lower() or 'enough' in thoughts.lower()):
#                 return f"Core belief: '{thoughts[:50]}...'"
#             else:
#                 return f"Explore belief behind: '{thoughts[:50]}...'"
#         else:
#             return "Identify core limiting belief driving the behavioral pattern"

#     def _get_new_identity_installation(self, dominant):
#         """Get new identity to install"""
#         if not dominant:
#             return "Confident, capable person who handles challenges naturally"
        
#         pattern_id = dominant['pattern_id']
#         identities = {
#             1: "Someone who naturally deserves and enjoys happiness",
#             2: "Someone who finds strength in collaboration and mutual respect",
#             3: "Someone who trusts wisely while remaining open and connected",
#             4: "Someone who sees multiple possibilities and finds creative solutions",
#             5: "Someone whose worth exists independent of achievements",
#             6: "Someone who expresses authenticity consistently across all contexts",
#             7: "Someone who cares for self and others with balanced love",
#             8: "Someone who honors family while living their authentic truth",
#             9: "Someone who maintains strength and boundaries in every situation"
#         }
#         return identities.get(pattern_id, "Someone who responds to challenges with natural strength and wisdom")

#     def _generate_homework_protocol(self, dominant, hypnotic_profile):
#         """Generate homework and integration protocol"""
#         if not dominant:
#             return "Standard self-hypnosis practice and pattern awareness exercises"
        
#         pattern_id = dominant['pattern_id']
#         trance_capacity = hypnotic_profile.get('trance_capacity', '')
        
#         # Base homework by pattern
#         homework = {
#             1: "Daily happiness permission practice: Notice and allow positive moments without guilt",
#             2: "Collaboration practice: One daily situation where you choose cooperation over control",
#             3: "Trust calibration: Daily practice of appropriate trust with evidence-based assessment",
#             4: "Both/and thinking: Daily identification of either/or thoughts and expansion to possibilities",
#             5: "Being practice: Daily moments of worth not tied to doing or achieving",
#             6: "Authenticity practice: Consistent self-expression across different contexts daily",
#             7: "Self-care strength: Daily practice of caring for yourself as you would a loved one",
#             8: "Personal truth: Daily check-in with your authentic desires separate from family expectations",
#             9: "Boundary consistency: Daily practice of maintaining values and boundaries across contexts"
#         }.get(pattern_id, "Pattern-specific daily awareness and practice")
        
#         # Add self-hypnosis based on trance capacity
#         if 'very easily' in trance_capacity.lower():
#             homework += "\nSelf-hypnosis: 15-20 minute daily practice with recorded session"
#         elif 'never' in trance_capacity.lower():
#             homework += "\nMindful awareness: 5-10 minute daily mindfulness practice"
#         else:
#             homework += "\nSelf-hypnosis: 10-15 minute daily practice with simple relaxation"
        
#         return homework

#     def _get_week_1_prediction(self, outcome_predictions):
#         """Predict week 1 outcomes"""
#         probability = outcome_predictions.get('rapid_change_probability', '')
#         if 'High' in probability:
#             return "Noticeable shift in automatic responses, reduced pattern frequency"
#         elif 'Good' in probability:
#             return "Initial changes in awareness, some pattern interruption"
#         else:
#             return "Increased awareness of patterns, beginning of change process"

#     def _get_month_1_prediction(self, outcome_predictions):
#         """Predict month 1 outcomes"""
#         probability = outcome_predictions.get('rapid_change_probability', '')
#         if 'High' in probability:
#             return "Significant pattern transformation, new responses becoming automatic"
#         elif 'Good' in probability:
#             return "Consistent pattern interruption, new responses developing"
#         else:
#             return "Gradual pattern modification, increased conscious choice"

#     def _get_3month_prediction(self, outcome_predictions):
#         """Predict 3 month outcomes"""
#         probability = outcome_predictions.get('rapid_change_probability', '')
#         if 'High' in probability:
#             return "Full integration of new patterns, unconscious competence achieved"
#         elif 'Good' in probability:
#             return "Strong integration, occasional conscious reinforcement needed"
#         else:
#             return "Solid progress, continued practice for full integration"

#     def _get_rapport_strategy(self, dominant, hypnotic_profile):
#         """Get rapport building strategy"""
#         if not dominant:
#             return "Standard rapport building with client's preferred communication style"
        
#         pattern_id = dominant['pattern_id']
#         therapeutic_style = hypnotic_profile.get('therapeutic_style', '')
        
#         strategies = {
#             1: "Validate their struggles genuinely, avoid premature positivity",
#             2: "Collaborative approach, ask permission, share control of session",
#             3: "Transparent explanation of all techniques, evidence-based rationale",
#             4: "Explore options together, avoid either/or language",
#             5: "Appreciate them for who they are, not what they do",
#             6: "Consistent authentic presence, no therapeutic 'persona'",
#             7: "Model balanced care - caring for them while maintaining boundaries",
#             8: "Honor their family values while supporting their individual path",
#             9: "Consistent therapeutic boundaries and reliability"
#         }
        
#         base_strategy = strategies.get(pattern_id, "Standard rapport building")
        
#         if 'analytical' in therapeutic_style.lower():
#             base_strategy += " - Provide clear explanations and logical frameworks"
#         elif 'receptive' in therapeutic_style.lower():
#             base_strategy += " - Can be more directive while maintaining warmth"
        
#         return base_strategy

#     def _predict_authority_response(self, pattern_constellation):
#         """Predict how client will respond to therapist authority"""
#         dominant = pattern_constellation.get('dominant')
#         if not dominant:
#             return "Standard therapeutic relationship dynamics"
        
#         pattern_id = dominant['pattern_id']
#         responses = {
#             1: "May be suspicious of therapist's positive regard or suggestions",
#             2: "Likely to challenge or test therapist authority, need collaborative approach",
#             3: "Will be evaluating therapist trustworthiness, need transparency",
#             4: "May feel trapped if given only limited options, need multiple choices",
#             5: "May try to 'perform' as good client, remind them they're valuable as-is",
#             6: "May present differently than in real life, encourage authenticity",
#             7: "May focus on therapist needs over own, redirect to self-care",
#             8: "May worry about disappointing therapist like family, address directly",
#             9: "May become compliant in session but not outside, check for consistency"
#         }
#         return responses.get(pattern_id, "Standard authority response patterns")

#     def _predict_emotional_regulation(self, pattern_constellation, clinical_flags):
#         """Predict emotional regulation during sessions"""
#         if 'dissociation_risk' in clinical_flags:
#             return "High risk of dissociation - use grounding techniques, shorter sessions"
        
#         dominant = pattern_constellation.get('dominant')
#         if not dominant:
#             return "Standard emotional processing capacity"
        
#         pattern_id = dominant['pattern_id']
#         regulations = {
#             1: "May resist positive emotions, allow gradual happiness tolerance building",
#             2: "May become activated during authority topics, use de-escalation",
#             3: "May become hypervigilant, provide safety and predictability",
#             4: "May become overwhelmed by possibilities, provide structure",
#             5: "May become anxious about being vs doing, provide reassurance",
#             6: "May struggle with authentic emotional expression, encourage genuineness",
#             7: "May minimize own emotions while focusing on others, redirect attention",
#             8: "May become guilty about personal emotions, validate feelings",
#             9: "May shut down emotions in vulnerable contexts, create safety"
#         }
#         return regulations.get(pattern_id, "Standard emotional regulation patterns")

#     def _predict_change_tolerance(self, resistance_analysis):
#         """Predict how fast client can tolerate change"""
#         secondary_gains = resistance_analysis.get('secondary_gains', '')
#         change_fears = resistance_analysis.get('change_fears', '')
        
#         if secondary_gains and 'not' not in secondary_gains.lower():
#             return "Slower pace needed - secondary gains present"
#         elif change_fears and len(change_fears) > 50:
#             return "Moderate pace - address fears first"
#         else:
#             return "Can likely tolerate rapid change"

#     def _recommend_feedback_style(self, pattern_constellation):
#         """Recommend feedback style for client"""
#         dominant = pattern_constellation.get('dominant')
#         if not dominant:
#             return "Direct, supportive feedback with specific examples"
        
#         pattern_id = dominant['pattern_id']
#         styles = {
#             1: "Gentle feedback, validate progress, avoid overwhelming positivity",
#             2: "Collaborative feedback, ask their opinion first",
#             3: "Clear, evidence-based feedback with transparent reasoning",
#             4: "Offer multiple perspectives, avoid absolute statements",
#             5: "Separate feedback from worth, focus on being not doing",
#             6: "Authentic, consistent feedback across all topics",
#             7: "Balanced feedback, encourage receiving as well as giving",
#             8: "Honor their values while supporting personal growth",
#             9: "Consistent feedback regardless of context or their presentation"
#         }
#         return styles.get(pattern_id, "Supportive, direct feedback with empathy")

#     def _get_contact_timeline(self, urgency, clinical_flags):
#         """Get contact timeline"""
#         if 'suicide_risk' in clinical_flags:
#             return "IMMEDIATE - Within 4 hours for crisis intervention"
#         elif 'high_risk_client' in clinical_flags:
#             return "Within 12 hours for safety assessment"
#         elif 'extremely urgent' in urgency.lower():
#             return "Within 24 hours for priority scheduling"
#         elif 'very urgent' in urgency.lower():
#             return "Within 48 hours for expedited response"
#         else:
#             return "Within 72 hours for standard response"

#     def _generate_immediate_action_plan(self, urgency, clinical_flags, pattern_constellation):
#         """Generate immediate action plan"""
#         actions = []
        
#         # Safety first
#         if 'suicide_risk' in clinical_flags:
#             actions.append("1. CRISIS RESPONSE: Immediate safety assessment required")
#             actions.append("2. EMERGENCY PROTOCOL: Have crisis resources ready")
#         elif 'high_risk_client' in clinical_flags:
#             actions.append("1. PRIORITY CONTACT: Safety-focused initial call")
#             actions.append("2. SPECIALIZED APPROACH: Review contraindications")
        
#         # Urgency-based actions
#         if 'extremely urgent' in urgency.lower():
#             actions.append("3. RAPID SCHEDULING: Offer session within 48-72 hours")
#             actions.append("4. MOTIVATION OPTIMIZATION: Contact while motivation is peak")
#         elif 'very urgent' in urgency.lower():
#             actions.append("3. PRIORITY SCHEDULING: Accommodate urgent timeline")
#             actions.append("4. EXPEDITED RESPONSE: Show responsiveness to their urgency")
        
#         # Pattern-based approach
#         dominant = pattern_constellation.get('dominant')
#         if dominant:
#             pattern_id = dominant['pattern_id']
#             approach_actions = {
#                 1: "5. APPROACH: Validate struggles, avoid premature optimism",
#                 2: "5. APPROACH: Use collaborative language, avoid directive commands",
#                 3: "5. APPROACH: Provide clear explanations, build trust gradually",
#                 4: "5. APPROACH: Offer multiple options, avoid either/or language",
#                 5: "5. APPROACH: Value them for who they are, not achievements",
#                 6: "5. APPROACH: Be authentic and consistent",
#                 7: "5. APPROACH: Model balanced care and boundaries",
#                 8: "5. APPROACH: Honor family while supporting personal growth",
#                 9: "5. APPROACH: Maintain consistent boundaries and reliability"
#             }
#             actions.append(approach_actions.get(pattern_id, "5. APPROACH: Use pattern-specific therapeutic style"))
        
#         # Preparation actions
#         actions.append("6. PREPARATION: Review complete clinical analysis before contact")
#         actions.append("7. SESSION SETUP: Prepare pattern-specific intervention strategy")
        
#         return "\n".join(actions)

#     def _get_safety_prep(self, clinical_flags):
#         """Get safety preparation requirements"""
#         if not clinical_flags:
#             return "Standard safety protocols"
        
#         prep_items = []
#         for flag in clinical_flags:
#             if flag == 'suicide_risk':
#                 prep_items.append("Crisis intervention resources")
#             elif flag == 'dissociation_risk':
#                 prep_items.append("Grounding techniques ready")
#             elif flag == 'medication_considerations':
#                 prep_items.append("Medication interaction review")
        
#         return ", ".join(prep_items) if prep_items else "Standard safety protocols"

#     def _get_primary_resistance_focus(self, resistance_analysis):
#         """Get primary resistance focus for preparation"""
#         secondary_gains = resistance_analysis.get('secondary_gains', '')
#         predictions = resistance_analysis.get('predictions', [])
        
#         if secondary_gains and 'not' not in secondary_gains.lower():
#             return "Secondary gains from current problem"
#         elif predictions:
#             return predictions[0]
#         else:
#             return "General resistance to change"

#     def _assess_data_quality(self, data):
#         """Assess overall data quality"""
#         total_questions = data.get('total_questions', 0)
#         completion_rate = data.get('completion_rate', '0%')
        
#         if total_questions >= 25 and '100%' in completion_rate:
#             return "Excellent - Complete assessment with comprehensive data"
#         elif total_questions >= 20:
#             return "Good - Adequate data for clinical planning"
#         else:
#             return "Fair - May need supplemental assessment"

#     def _assess_therapeutic_confidence(self, assessment_results):
#         """Assess confidence in therapeutic recommendations"""
#         pattern_constellation = assessment_results.get('pattern_constellation', {})
#         behavioral_chain = assessment_results.get('behavioral_chain', {})
        
#         dominant = pattern_constellation.get('dominant')
#         chain_complete = len([v for v in behavioral_chain.values() if v and v != 'Not provided']) >= 3
        
#         if dominant and chain_complete:
#             return "High - Clear patterns and behavioral chain identified"
#         elif dominant or chain_complete:
#             return "Moderate - Some key data points identified"
#         else:
#             return "Lower - May need additional assessment"

#     def _assess_intervention_readiness(self, clinical_flags, resistance_analysis):
#         """Assess readiness for intervention"""
#         if 'suicide_risk' in clinical_flags:
#             return "Crisis intervention required first"
#         elif clinical_flags:
#             return "Modified approach needed due to clinical considerations"
#         elif resistance_analysis.get('secondary_gains'):
#             return "Address resistance factors in session 1"
#         else:
#             return "Ready for standard hypnotherapy intervention"

#     def _assess_overall_data_quality(self, data):
#         """Assess overall data quality for clinical use"""
#         assessment_results = data.get('assessment_results', {})
        
#         # Check data completeness
#         presenting_problem = assessment_results.get('presenting_problem', {})
#         pattern_constellation = assessment_results.get('pattern_constellation', {})
#         behavioral_chain = assessment_results.get('behavioral_chain', {})
        
#         quality_score = 0
        
#         if presenting_problem.get('target_behavior') and presenting_problem.get('target_behavior') != 'Not specified':
#             quality_score += 2
        
#         if pattern_constellation.get('dominant'):
#             quality_score += 2
        
#         chain_completeness = len([v for v in behavioral_chain.values() if v and v != 'Not provided'])
#         if chain_completeness >= 3:
#             quality_score += 2
        
#         if quality_score >= 5:
#             return "High quality - Complete data for therapeutic planning"
#         elif quality_score >= 3:
#             return "Good quality - Adequate for clinical intervention"
#         else:
#             return "Moderate quality - May need supplemental data"

#     def _assess_clinical_confidence(self, assessment_results):
#         """Assess clinical confidence in recommendations"""
#         # Multiple factors contribute to confidence
#         confidence_factors = 0
        
#         if assessment_results.get('presenting_problem', {}).get('target_behavior') != 'Not specified':
#             confidence_factors += 1
        
#         if assessment_results.get('pattern_constellation', {}).get('dominant'):
#             confidence_factors += 1
        
#         if len(assessment_results.get('behavioral_chain', {})) >= 3:
#             confidence_factors += 1
        
#         if not assessment_results.get('clinical_flags'):
#             confidence_factors += 1
        
#         if confidence_factors >= 3:
#             return "High confidence in therapeutic recommendations"
#         elif confidence_factors >= 2:
#             return "Moderate confidence with ongoing calibration needed"
#         else:
#             return "Lower confidence - recommend additional assessment"

#     def _get_next_review_timeline(self, urgency, clinical_flags):
#         """Get next review timeline"""
#         if 'suicide_risk' in clinical_flags:
#             return "Immediate review after crisis intervention"
#         elif 'extremely urgent' in urgency.lower():
#             return "24-48 hours post initial contact"
#         else:
#             return "1 week post initial session"

#     def _recommend_therapist_type(self, assessment_results):
#         """Recommend type of therapist needed"""
#         clinical_flags = assessment_results.get('clinical_flags', [])
#         safety_assessment = assessment_results.get('safety_assessment', {})
        
#         if 'suicide_risk' in clinical_flags:
#             return "Crisis intervention specialist, then licensed clinical hypnotherapist"
#         elif safety_assessment.get('referral_needed'):
#             return "Licensed clinical psychologist with hypnotherapy specialization"
#         elif clinical_flags:
#             return "Licensed clinical hypnotherapist with trauma experience"
#         else:
#             return "Certified hypnotherapist with rapid transformation specialization"

#     def _determine_therapeutic_pace(self, urgency, clinical_flags):
#         """Determine appropriate therapeutic pace"""
#         if clinical_flags:
#             return "Cautious pace with safety monitoring"
#         elif 'extremely urgent' in urgency.lower():
#             return "Accelerated pace matching client urgency"
#         elif 'very urgent' in urgency.lower():
#             return "Moderately accelerated pace"
#         else:
#             return "Standard therapeutic pace"

#     def _build_email(self, subject, body):
#         """Build email message"""
#         try:
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = subject
#             msg.attach(MIMEText(body, 'plain'))
#             return msg
#         except Exception as e:
#             print(f"[ERROR] Error building email: {e}")
#             raise

#     def _dispatch(self, msg, data, email_type):
#         """Dispatch email with proper error handling"""
#         try:
#             print(f"[DEBUG] Dispatching {email_type} email")
            
#             if not self.password:
#                 print(f"[DEBUG] {email_type} email would be sent (no password configured)")
#                 return True
            
#             if not self.sender_email or not self.recipient_email:
#                 print(f"[ERROR] Missing email configuration for {email_type}")
#                 return False
                
#             return self._send_email(msg)
            
#         except Exception as e:
#             print(f"[ERROR] Exception in _dispatch: {e}")
#             return False

#     def _send_email(self, msg):
#         """Send email via Gmail SMTP"""
#         try:
#             print("[DEBUG] Attempting to send email via SMTP")
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
#             server.starttls()
#             server.login(self.sender_email, self.password)
#             server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
#             server.quit()
            
#             print(f"[SUCCESS] Email sent from {self.sender_email} to {self.recipient_email}")
#             return True
            
#         except Exception as e:
#             print(f"[ERROR] Error sending email: {e}")
#             return False


# # Global instance and helper functions
# clinical_email_handler = ClinicalEmailHandler()

# def send_clinical_assessment_results(data):
#     """Send clinical assessment results email - MAIN FUNCTION CALLED BY ASSESS.PY"""
#     try:
#         print("[DEBUG] Clinical email handler - send_clinical_assessment_results called")
#         return clinical_email_handler.send_clinical_assessment_results(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_clinical_assessment_results: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# # Backward compatibility functions
# def send_assessment_results_email(data):
#     """Backward compatibility for assessment results"""
#     return send_clinical_assessment_results(data)

# def send_discovery_call_email(data):
#     """Backward compatibility for discovery calls"""
#     return send_clinical_assessment_results(data)

# def send_contact_form_email(data):
#     """Backward compatibility for contact forms"""
#     return send_clinical_assessment_results(data)

# def send_booking_confirmation_email(data):
#     """Backward compatibility for booking confirmations"""
#     return send_clinical_assessment_results(data)





"""
Complete Email Handler for Hypnotherapy Website
Supports both clinical assessment analysis and standard booking workflows
Integrates with all website pages and maintains backward compatibility
"""
import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class ComprehensiveEmailHandler:
    """Complete email handler for all website email needs"""
    
    def __init__(self):
        # Gmail SMTP configuration
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
        # Try to get credentials from Streamlit secrets, then environment
        try:
            import streamlit as st
            self.sender_email = st.secrets.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        except:
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD", "")
        
        # Pattern descriptions for clinical analysis
        self.pattern_descriptions = {
            1: "Unhappiness Culture - Difficulty accepting or maintaining positive states",
            2: "Power Struggles - Recurring conflicts and control issues",
            3: "Systematic Mistrust - Default skepticism and trust difficulties",
            4: "Separation/Division - Black-and-white thinking patterns",
            5: "Doing vs Being - Self-worth tied to achievement",
            6: "Compartmentalized Authenticity - Inconsistent identity",
            7: "Self-Sacrifice - Prioritizing others while neglecting self",
            8: "Inherited Missions - Life choices driven by family expectations",
            9: "Context Dependent Weakness - Situational boundary loss"
        }
    
    # ================== CLINICAL ASSESSMENT EMAILS ==================
    
    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment with therapeutic analysis"""
        try:
            print("[DEBUG] Starting clinical assessment email process")
            print(f"[DEBUG] Assessment data keys: {list(assessment_data.keys())}")
            
            # Extract key information
            contact_info = assessment_data.get('contact_info', {})
            results = assessment_data.get('assessment_results', {})
            
            if not contact_info:
                print("[ERROR] No contact_info found in assessment_data")
                return False
            
            if not results and not assessment_data.get('pattern_scores'):
                print("[ERROR] No assessment_results or pattern_scores found")
                return False
            
            urgency = contact_info.get('urgency', 'Standard priority')
            risk_flags = results.get('risk_flags', []) or assessment_data.get('risk_flags', [])
            
            print(f"[DEBUG] Found {len(risk_flags)} risk flags")
            print(f"[DEBUG] Urgency level: {urgency}")
            
            # Determine priority flag
            priority_flag = self._get_priority_flag(urgency, risk_flags)
            
            subject = f"{priority_flag} Clinical Assessment - {contact_info.get('name', 'Client')}"
            print(f"[DEBUG] Email subject: {subject}")
            
            body = self._format_clinical_email_body(assessment_data)
            
            if not body or len(body) < 100:
                print("[ERROR] Email body generation failed or too short")
                return False
            
            print(f"[DEBUG] Email body length: {len(body)} characters")
            return self._send_email(subject, body, "Clinical Assessment")
            
        except Exception as e:
            print(f"[ERROR] Clinical assessment email error: {e}")
            import traceback
            print(f"[ERROR] Traceback: {traceback.format_exc()}")
            return False
    
    def _format_clinical_email_body(self, data):
        """Format comprehensive clinical assessment email"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract data components
            contact_info = data.get('contact_info', {})
            results = data.get('assessment_results', {})
            responses = data.get('assessment_responses', {})
            intensity_data = data.get('intensity_responses', {})
            
            # Basic info
            name = contact_info.get('name', 'Unknown')
            email = contact_info.get('email', 'Unknown')
            phone = contact_info.get('phone', 'Not provided')
            urgency = contact_info.get('urgency', 'Not specified')
            primary_concern = contact_info.get('primary_concern', 'Not provided')
            next_step = contact_info.get('next_step', 'Not specified')
            
            # Clinical data
            pattern_scores = results.get('pattern_scores', {})
            risk_flags = results.get('risk_flags', [])
            dominant_pattern = results.get('dominant_pattern')
            completion_rate = results.get('completion_rate', 0) * 100
            total_questions = results.get('total_questions_answered', 0)
            adaptive_paths = results.get('adaptive_paths_triggered', [])
            
            body = f"""
🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT
Assessment Completed: {timestamp}
Clinical Priority: {self._get_clinical_priority(urgency, risk_flags)}

═══════════════════════════════════════════════════════════

👤 CLIENT PROFILE & CONTACT INFORMATION

Name: {name}
Email: {email}
Phone: {phone}
Urgency Level: {urgency}
Primary Concern: {primary_concern}
Preferred Next Step: {next_step}

Assessment Quality: {completion_rate:.0f}% completion rate
Total Questions Answered: {total_questions}
Adaptive Pathways Triggered: {len(adaptive_paths)}

═══════════════════════════════════════════════════════════

🎯 BEHAVIORAL PATTERN ANALYSIS

PRIMARY PATTERNS IDENTIFIED:
"""
            
            # Add pattern analysis
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
                for i, (pattern_id, score) in enumerate(sorted_patterns[:5]):
                    pattern_name = self.pattern_descriptions.get(pattern_id, f"Pattern {pattern_id}")
                    intensity = self._get_intensity_level(score)
                    rank = "🔴 DOMINANT" if i == 0 else f"{i+1}. SECONDARY"
                    
                    body += f"""
{rank} PATTERN: {pattern_name}
├─ Activation Score: {score:.1f}/12 ({intensity} intensity)
├─ Clinical Significance: {self._get_clinical_significance(pattern_id, score)}
├─ Therapeutic Approach: {self._get_therapeutic_approach(pattern_id)}
└─ Session Priority: {self._get_session_priority(pattern_id, i == 0)}
"""
                
                if len(sorted_patterns) > 5:
                    body += f"\nADDITIONAL PATTERNS: {len(sorted_patterns) - 5} lower-intensity patterns detected\n"
            else:
                body += "\nNo significant patterns above threshold - exploratory approach recommended\n"
            
            body += f"""
═══════════════════════════════════════════════════════════

⚠️ CLINICAL RISK ASSESSMENT

Risk Level: {self._assess_overall_risk_level(risk_flags)}
Risk Factors Identified: {len(risk_flags)}
"""
            
            # Risk factor details
            if risk_flags:
                body += "\nSPECIFIC RISK CONSIDERATIONS:\n"
                for i, flag in enumerate(risk_flags, 1):
                    risk_description = self._get_risk_description(flag)
                    management = self._get_risk_management(flag)
                    body += f"{i}. {risk_description}\n   └─ Management: {management}\n"
            else:
                body += "\n✅ No significant risk factors identified - standard approach suitable\n"
            
            body += f"""
═══════════════════════════════════════════════════════════

🎯 THERAPEUTIC RECOMMENDATIONS

RECOMMENDED APPROACH: {self._get_recommended_approach(dominant_pattern, risk_flags)}
ESTIMATED SESSIONS: {self._estimate_session_count(pattern_scores, risk_flags)}
SUCCESS PROBABILITY: {self._estimate_success_probability(completion_rate, len(risk_flags))}

SESSION 1 FOCUS:
{self._get_session_1_focus(dominant_pattern, primary_concern)}

SESSION 2 FOCUS:
{self._get_session_2_focus(dominant_pattern, pattern_scores)}

POTENTIAL RESISTANCE POINTS:
{self._identify_resistance_points(pattern_scores, responses)}

HYPNOTHERAPY PROTOCOL:
{self._generate_hypnotherapy_protocol(dominant_pattern, intensity_data)}

═══════════════════════════════════════════════════════════

📊 DETAILED RESPONSE ANALYSIS

ASSESSMENT COMPLETION DATA:
"""
            
            # Add key responses analysis
            key_responses = self._extract_key_responses(responses)
            if key_responses:
                body += "\nKEY CLIENT RESPONSES:\n"
                for question, response in key_responses.items():
                    body += f"• {question}: {response}\n"
            
            # Intensity data
            if intensity_data:
                body += f"\nINTENSITY RATINGS PROVIDED: {len(intensity_data)} questions\n"
                high_intensity = {k: v for k, v in intensity_data.items() if v >= 6}
                if high_intensity:
                    body += f"HIGH INTENSITY RESPONSES: {len(high_intensity)} items rated 6-7/7\n"
            
            body += f"""
ADAPTIVE QUESTIONING TRIGGERED: {', '.join(adaptive_paths) if adaptive_paths else 'None'}

═══════════════════════════════════════════════════════════

📞 IMMEDIATE ACTION PROTOCOL

CONTACT TIMELINE: {self._get_contact_timeline(urgency, risk_flags)}
RECOMMENDED RESPONSE: {self._get_recommended_response(next_step)}

PREPARATION CHECKLIST:
1. Review complete client responses (attached below)
2. Prepare pattern-specific approach for {self.pattern_descriptions.get(dominant_pattern, 'identified patterns')}
3. {self._get_specific_preparation(dominant_pattern, risk_flags)}
4. Set up appropriate session environment and materials

═══════════════════════════════════════════════════════════

💬 COMPLETE CLIENT RESPONSES TRANSCRIPT

FULL ASSESSMENT RESPONSES:
"""
            
            # Add complete response transcript
            if responses:
                for q_id in sorted(responses.keys()):
                    response_data = responses[q_id]
                    question_text = response_data.get('question_text', f'Question {q_id}')
                    response = response_data.get('response', 'No response')
                    intensity = intensity_data.get(q_id)
                    
                    body += f"\n{q_id}. {question_text}\n"
                    body += f"   Response: {response}\n"
                    if intensity:
                        body += f"   Intensity: {intensity}/7\n"
                    body += f"   Timestamp: {response_data.get('timestamp', 'Unknown')}\n"
            
            body += f"""

═══════════════════════════════════════════════════════════

🔧 TECHNICAL ASSESSMENT METADATA

Assessment Algorithm: Comprehensive Behavioral Pattern Analysis v2.0
Completion Quality: {completion_rate:.0f}% ({total_questions} questions answered)
Clinical Confidence: {self._assess_clinical_confidence(completion_rate, len(pattern_scores))}
Data Integrity: {self._assess_data_integrity(responses)}

Therapist Assignment Recommendation: {self._recommend_therapist_type(risk_flags, urgency)}
Next Clinical Review: {self._get_next_review_date(urgency, risk_flags)}

⚠️ CONFIDENTIAL CLINICAL DOCUMENT
Contains sensitive psychological assessment data
Licensed therapist review required before client contact

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Clinical Assessment System
Generated: {timestamp}
Client Reference: {name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Error formatting clinical email: {e}")
            # Return basic email with error info
            return f"""
CLINICAL ASSESSMENT RESULTS - FORMATTING ERROR

Client: {data.get('contact_info', {}).get('name', 'Unknown')}
Email: {data.get('contact_info', {}).get('email', 'Unknown')}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Error Details: {str(e)}

Raw assessment data available - manual review required.
Complete responses preserved for clinical analysis.

Bangkok Hypnotherapy Clinic - Clinical Assessment System
            """
    
    # ================== STANDARD BOOKING EMAILS ==================
    
    def send_booking_email(self, name, email, concern, message, booking_type):
        """Send standard booking notification (maintains compatibility)"""
        try:
            print(f"[DEBUG] Sending {booking_type} booking email")
            
            subject = f"📞 New {booking_type} Request - {name}"
            body = self._format_booking_email_body(name, email, concern, message, booking_type)
            
            return self._send_email(subject, body, booking_type)
            
        except Exception as e:
            print(f"[ERROR] Booking email error: {e}")
            return False
    
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification"""
        try:
            name = booking_data.get('name', '')
            email = booking_data.get('email', '')
            concern = booking_data.get('concern', '')
            message = booking_data.get('concern_description', '') or booking_data.get('message', '')
            urgency = booking_data.get('urgency', '')
            experience = booking_data.get('experience', '')
            
            subject = f"📞 New Discovery Call Request - {name}"
            body = self._format_discovery_call_body(name, email, concern, message, urgency, experience)
            
            return self._send_email(subject, body, "Discovery Call")
            
        except Exception as e:
            print(f"[ERROR] Discovery call email error: {e}")
            return False
    
    def send_package_booking_email(self, booking_data):
        """Send transformation package booking notification"""
        try:
            name = booking_data.get('name', '')
            email = booking_data.get('email', '')
            concern = booking_data.get('concern', '')
            message = booking_data.get('message', '')
            package_type = booking_data.get('package_type', '')
            experience = booking_data.get('experience', '')
            
            subject = f"💰 New Transformation Package Booking - {name}"
            body = self._format_package_booking_body(name, email, concern, message, package_type, experience)
            
            return self._send_email(subject, body, "Package Booking")
            
        except Exception as e:
            print(f"[ERROR] Package booking email error: {e}")
            return False
    
    def _format_booking_email_body(self, name, email, concern, message, booking_type):
        """Format standard booking email (maintains compatibility)"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
📞 NEW {booking_type.upper()} REQUEST
Received: {timestamp}

═══════════════════════════════════════════

👤 CONTACT INFORMATION:
Name: {name}
Email: {email}

🎯 CONCERN DETAILS:
Primary Concern: {concern}
Message: {message}

📞 NEXT STEPS:
Please contact this person within 24-48 hours to schedule their {booking_type.lower()}.

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Automated Booking System
        """
    
    def _format_discovery_call_body(self, name, email, concern, message, urgency, experience):
        """Format discovery call email with enhanced details"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Determine priority based on urgency
        if 'extremely urgent' in urgency.lower():
            priority = "🔴 HIGH PRIORITY"
        elif 'very urgent' in urgency.lower():
            priority = "🟡 PRIORITY"
        else:
            priority = "📋 STANDARD"
        
        return f"""
{priority} DISCOVERY CALL REQUEST
Received: {timestamp}

═══════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}

🎯 CONCERN DETAILS:
Primary Concern: {concern}
Urgency Level: {urgency}
Previous Experience: {experience}

💬 CLIENT MESSAGE:
{message}

📞 ACTION REQUIRED:
Contact Timeline: {self._get_simple_contact_timeline(urgency)}

RECOMMENDED APPROACH:
1. {self._get_discovery_call_approach(concern, urgency)}
2. Assess suitability for rapid transformation method
3. Explain 2-session approach if appropriate
4. Schedule Session 1 if client is ready to proceed

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Discovery Call System
        """
    
    def _format_package_booking_body(self, name, email, concern, message, package_type, experience):
        """Format package booking email with enhanced details"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
💰 TRANSFORMATION PACKAGE BOOKING
Received: {timestamp}

═══════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}

📦 PACKAGE DETAILS:
Selected Package: {package_type}
Primary Concern: {concern}
Previous Experience: {experience}

💬 CLIENT MESSAGE:
{message}

📞 HIGH PRIORITY ACTION REQUIRED:
This client is ready to proceed with transformation package.

IMMEDIATE STEPS:
1. Send welcome email with package confirmation
2. Schedule Session 1 within 48-72 hours
3. Send pre-session preparation materials
4. Confirm payment method and schedule

💰 EXPECTED REVENUE: 3,000-4,000 THB

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Package Booking System
        """
    
    # ================== EMAIL SENDING INFRASTRUCTURE ==================
    
    def _send_email(self, subject, body, email_type):
        """Send email via Gmail SMTP"""
        try:
            if not self.password:
                print(f"[DEBUG] {email_type} email simulation (no password configured)")
                print(f"[DEBUG] To: {self.recipient_email}")
                print(f"[DEBUG] Subject: {subject}")
                return True
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            
            print(f"[SUCCESS] {email_type} email sent successfully")
            return True
            
        except Exception as e:
            print(f"[ERROR] SMTP error for {email_type}: {e}")
            return False
    
    # ================== CLINICAL ANALYSIS HELPER METHODS ==================
    
    def _get_priority_flag(self, urgency, risk_flags):
        """Determine clinical priority flag"""
        if len(risk_flags) >= 3:
            return "🔴 HIGH RISK"
        elif 'extremely urgent' in urgency.lower():
            return "🟠 URGENT"
        elif 'very urgent' in urgency.lower():
            return "🟡 PRIORITY"
        else:
            return "📋 ASSESSMENT"
    
    def _get_clinical_priority(self, urgency, risk_flags):
        if len(risk_flags) >= 3:
            return "HIGH RISK - Specialized approach required"
        elif 'extremely urgent' in urgency.lower():
            return "URGENT - Priority scheduling within 24 hours"
        elif 'very urgent' in urgency.lower():
            return "ELEVATED - Contact within 48 hours"
        else:
            return "STANDARD - Contact within 72 hours"
    
    def _get_intensity_level(self, score):
        if score >= 8:
            return "Very High"
        elif score >= 6:
            return "High"
        elif score >= 4:
            return "Moderate"
        elif score >= 2:
            return "Low"
        else:
            return "Minimal"
    
    def _get_clinical_significance(self, pattern_id, score):
        base_significance = {
            1: "Blocks positive therapeutic outcomes, requires permission-based approach",
            2: "May resist directive techniques, needs collaborative framework",
            3: "Trust-building essential before intervention, transparency required",
            4: "Expand thinking flexibility, address either/or cognitive patterns",
            5: "Separate self-worth from performance, emphasize being over doing",
            6: "Identity integration work needed across contexts",
            7: "Self-care resistance expected, reframe as strength for helping others",
            8: "Family loyalty conflicts may emerge, honor while expanding choice",
            9: "Context-dependent response patterns, strengthen consistent boundaries"
        }.get(pattern_id, "Pattern-specific intervention required")
        
        if score >= 8:
            return f"DOMINANT PATTERN: {base_significance}"
        elif score >= 6:
            return f"SIGNIFICANT PATTERN: {base_significance}"
        else:
            return f"SUPPORTING PATTERN: {base_significance}"
    
    def _get_therapeutic_approach(self, pattern_id):
        approaches = {
            1: "Permission installation, positive expectation building, success tolerance",
            2: "Collaborative empowerment, shared control, non-directive language",
            3: "Trust-first approach, transparent explanations, evidence-based interventions",
            4: "Integration therapy, both/and thinking, possibility expansion",
            5: "Being-centered work, inherent worth installation, performance separation",
            6: "Authentic self integration across contexts, consistency building",
            7: "Self-care strength reframing, boundary establishment, balanced care",
            8: "Personal desire differentiation, respectful family honor, authentic vision",
            9: "Context-independent strength, consistent boundary maintenance"
        }
        return approaches.get(pattern_id, "Pattern-specific individualized approach")
    
    def _get_session_priority(self, pattern_id, is_dominant):
        if is_dominant:
            priorities = {
                1: "Session 1 Priority - Address happiness resistance, install permission",
                2: "Session 1 Priority - Establish collaboration, avoid power dynamics",
                3: "Session 1 Priority - Build trust foundation, transparent process",
                4: "Session 1 Priority - Expand thinking flexibility, explore options",
                5: "Session 1 Priority - Separate worth from doing, establish being value",
                6: "Session 1 Priority - Support authentic consistency across contexts",
                7: "Session 1 Priority - Reframe self-care as strength for service",
                8: "Session 1 Priority - Honor family while supporting personal truth",
                9: "Session 1 Priority - Strengthen consistent boundaries across contexts"
            }
            return priorities.get(pattern_id, "Session 1 Priority - Address dominant pattern")
        else:
            return "Session 2 Integration - Address as supporting pattern"
    
    def _assess_overall_risk_level(self, risk_flags):
        if len(risk_flags) >= 4:
            return "HIGH - Specialized clinical approach required"
        elif len(risk_flags) >= 2:
            return "ELEVATED - Modified approach with safety protocols"
        elif len(risk_flags) >= 1:
            return "MODERATE - Standard approach with precautions"
        else:
            return "LOW - Standard hypnotherapy approach suitable"
    
    def _get_risk_description(self, flag):
        descriptions = {
            'risk_q_10': "Current medical/mental health care - coordination required",
            'risk_q_11': "Intense emotional states - emotional regulation concerns",
            'risk_q_12': "Dissociation/panic/self-harm history - safety protocols needed",
            'risk_q_13': "Substance use patterns - sobriety considerations"
        }
        return descriptions.get(flag, f"Risk factor identified - {flag}")
    
    def _get_risk_management(self, flag):
        management = {
            'risk_q_10': "Coordinate with existing care providers before sessions",
            'risk_q_11': "Use grounding techniques, shorter sessions, emotion regulation",
            'risk_q_12': "Safety assessment, crisis resources, modified approach",
            'risk_q_13': "Address substance use, consider timing of intervention"
        }
        return management.get(flag, "Standard clinical precautions")
    
    def _get_recommended_approach(self, dominant_pattern, risk_flags):
        if len(risk_flags) >= 2:
            return "Modified hypnotherapy with specialized safety protocols"
        elif dominant_pattern in [1, 2, 3]:
            return "Collaborative, permission-based hypnotherapy approach"
        elif dominant_pattern in [7, 8, 9]:
            return "Gentle, supportive hypnotherapy with boundary work"
        else:
            return "Standard clinical hypnotherapy with pattern-specific modifications"
    
    def _estimate_session_count(self, pattern_scores, risk_flags):
        if len(risk_flags) >= 2:
            return "3-4 sessions (additional support needed)"
        elif len(pattern_scores) >= 3:
            return "2-3 sessions (complex pattern integration)"
        else:
            return "2 sessions (standard rapid transformation)"
    
    def _estimate_success_probability(self, completion_rate, risk_count):
        if completion_rate >= 90 and risk_count == 0:
            return "HIGH (85%+) - Excellent assessment quality, no risk factors"
        elif completion_rate >= 75 and risk_count <= 1:
            return "GOOD (70-85%) - Good assessment quality, minimal risk"
        elif completion_rate >= 60:
            return "MODERATE (55-70%) - Fair assessment, some complexity"
        else:
            return "VARIABLE - May need additional assessment for optimization"
    
    def _get_session_1_focus(self, dominant_pattern, concern):
        if dominant_pattern:
            pattern_name = self.pattern_descriptions.get(dominant_pattern, f"Pattern {dominant_pattern}")
            return f"Address {pattern_name} - rapport building and initial pattern interruption"
        else:
            return f"Exploratory session focused on client's primary concern: {concern[:100]}"
    
    def _get_session_2_focus(self, dominant_pattern, pattern_scores):
        if dominant_pattern and len(pattern_scores) >= 2:
            return "Core transformation of dominant pattern with supporting pattern integration"
        elif dominant_pattern:
            return f"Deep transformation of {self.pattern_descriptions.get(dominant_pattern)}"
        else:
            return "Individualized transformation based on session 1 insights"
    
    def _identify_resistance_points(self, pattern_scores, responses):
        resistance_patterns = []
        
        # Check for specific resistance indicators
        if 1 in pattern_scores:  # Unhappiness culture
            resistance_patterns.append("• May resist positive suggestions or success imagery")
        if 2 in pattern_scores:  # Power struggles
            resistance_patterns.append("• May challenge therapist authority or directive language")
        if 3 in pattern_scores:  # Mistrust
            resistance_patterns.append("• May question techniques or need extensive explanations")
        
        # Check secondary gain responses
        secondary_gain_responses = [r for r in responses.values() 
                                  if 'secondary_gain' in r.get('question_text', '').lower()]
        if secondary_gain_responses:
            resistance_patterns.append("• Secondary gains identified - address benefits of current pattern")
        
        return '\n'.join(resistance_patterns) if resistance_patterns else "• Minimal resistance predicted based on assessment"
    
    def _generate_hypnotherapy_protocol(self, dominant_pattern, intensity_data):
        if not dominant_pattern:
            return "Standard protocol with individualization based on session 1 findings"
        
        protocols = {
            1: "Gentle permission-based induction, positive expectation installation, happiness tolerance",
            2: "Collaborative induction, shared control language, empowerment suggestions",
            3: "Transparent explanation of process, trust-building suggestions, evidence-based approach",
            4: "Integration-focused suggestions, both/and language, possibility expansion",
            5: "Being-centered induction, worth installation separate from doing, presence anchoring",
            6: "Consistent identity suggestions across contexts, authenticity integration",
            7: "Self-care strength installation, balanced care suggestions, boundary visualization",
            8: "Family honor with personal truth, loyalty reframe, authentic path suggestions",
            9: "Consistent strength installation, boundary integrity across all contexts"
        }
        
        base_protocol = protocols.get(dominant_pattern, "Standard individualized approach")
        
        # Modify based on intensity data
        if intensity_data and max(intensity_data.values()) >= 6:
            base_protocol += " - High intensity responses require gentle pacing and grounding"
        
        return base_protocol
    
    def _extract_key_responses(self, responses):
        """Extract the most clinically relevant responses"""
        key_responses = {}
        
        for q_id, response_data in responses.items():
            question = response_data.get('question_text', '')
            response = response_data.get('response', '')
            
            # Include key assessment questions
            if any(keyword in question.lower() for keyword in 
                   ['specific behavior', 'trigger', 'physical sensation', 'inner voice', 'behavioral response']):
                key_responses[question[:80] + "..."] = str(response)[:150]
        
        return dict(list(key_responses.items())[:5])  # Top 5 most relevant
    
    def _get_contact_timeline(self, urgency, risk_flags):
        if len(risk_flags) >= 3:
            return "IMMEDIATE - Within 12 hours for safety assessment"
        elif 'extremely urgent' in urgency.lower():
            return "PRIORITY - Within 24 hours for urgent scheduling"
        elif 'very urgent' in urgency.lower():
            return "ELEVATED - Within 48 hours for prompt response"
        else:
            return "STANDARD - Within 72 hours for routine follow-up"
    
    def _get_recommended_response(self, next_step):
        if 'consultation' in next_step.lower():
            return "Schedule free consultation call via provided contact information"
        elif 'package' in next_step.lower():
            return "Send transformation package information and pricing"
        elif 'analysis' in next_step.lower():
            return "Email detailed analysis with specific recommendations first"
        else:
            return "Contact client to discuss personalized next steps"
    
    def _get_specific_preparation(self, dominant_pattern, risk_flags):
        if len(risk_flags) >= 2:
            return "Prepare safety protocols and crisis resources"
        elif dominant_pattern == 1:
            return "Prepare permission-based language, avoid overwhelming positivity"
        elif dominant_pattern == 2:
            return "Prepare collaborative approach, avoid directive commands"
        elif dominant_pattern == 3:
            return "Prepare transparent explanations, evidence-based rationales"
        else:
            return f"Prepare pattern-specific approach for {self.pattern_descriptions.get(dominant_pattern, 'identified pattern')}"
    
    def _assess_clinical_confidence(self, completion_rate, pattern_count):
        if completion_rate >= 90 and pattern_count >= 2:
            return "HIGH - Comprehensive data for targeted intervention"
        elif completion_rate >= 75:
            return "GOOD - Adequate data for effective treatment planning"
        else:
            return "MODERATE - May benefit from supplemental assessment"
    
    def _assess_data_integrity(self, responses):
        if len(responses) >= 20:
            return "EXCELLENT - Comprehensive response set"
        elif len(responses) >= 15:
            return "GOOD - Adequate response coverage"
        else:
            return "FAIR - Limited responses, focus on quality of available data"
    
    def _recommend_therapist_type(self, risk_flags, urgency):
        if len(risk_flags) >= 3:
            return "Licensed clinical psychologist with hypnotherapy specialization"
        elif len(risk_flags) >= 1:
            return "Licensed clinical hypnotherapist with safety training"
        elif 'extremely urgent' in urgency.lower():
            return "Experienced rapid-change hypnotherapist"
        else:
            return "Certified clinical hypnotherapist"
    
    def _get_next_review_date(self, urgency, risk_flags):
        if len(risk_flags) >= 2:
            return "24-48 hours post-contact for safety monitoring"
        elif 'extremely urgent' in urgency.lower():
            return "1 week post-session for progress assessment"
        else:
            return "2 weeks post-completion for outcome tracking"
    
    # ================== BOOKING HELPER METHODS ==================
    
    def _get_simple_contact_timeline(self, urgency):
        """Get simple contact timeline for booking emails"""
        if 'extremely urgent' in urgency.lower():
            return "Within 24 hours (high priority)"
        elif 'very urgent' in urgency.lower():
            return "Within 48 hours (priority)"
        else:
            return "Within 72 hours (standard)"
    
    def _get_discovery_call_approach(self, concern, urgency):
        """Get recommended approach for discovery call"""
        if 'anxiety' in concern.lower():
            return "Use calm, reassuring approach - explain safety of hypnotherapy"
        elif 'smoking' in concern.lower():
            return "Focus on rapid cessation method - emphasize 2-session success rate"
        elif 'habit' in concern.lower():
            return "Explain pattern interruption approach - assess habit specifics"
        elif 'extremely urgent' in urgency.lower():
            return "Acknowledge urgency, assess suitability for immediate scheduling"
        else:
            return "Standard discovery call approach - assess suitability and explain method"


# ================== GLOBAL INSTANCE AND HELPER FUNCTIONS ==================

# Global instance
comprehensive_email_handler = ComprehensiveEmailHandler()

# ====== MAIN ASSESSMENT FUNCTION ======
def send_clinical_assessment_results(assessment_data):
    """Send clinical assessment results - Main function for assess.py integration"""
    try:
        print("[DEBUG] Sending clinical assessment results via comprehensive handler")
        return comprehensive_email_handler.send_clinical_assessment_results(assessment_data)
    except Exception as e:
        print(f"[ERROR] Exception in clinical assessment email: {e}")
        return False

# ====== STANDARD BOOKING FUNCTIONS ======
def send_booking_email(name, email, concern, message, booking_type):
    """Send standard booking email - Maintains existing compatibility"""
    try:
        print(f"[DEBUG] Sending {booking_type} booking email")
        return comprehensive_email_handler.send_booking_email(name, email, concern, message, booking_type)
    except Exception as e:
        print(f"[ERROR] Exception in booking email: {e}")
        return False

def send_discovery_call_email(booking_data):
    """Send discovery call booking notification"""
    try:
        print("[DEBUG] Sending discovery call email")
        return comprehensive_email_handler.send_discovery_call_email(booking_data)
    except Exception as e:
        print(f"[ERROR] Exception in discovery call email: {e}")
        return False

def send_package_booking_email(booking_data):
    """Send package booking notification"""
    try:
        print("[DEBUG] Sending package booking email")
        return comprehensive_email_handler.send_package_booking_email(booking_data)
    except Exception as e:
        print(f"[ERROR] Exception in package booking email: {e}")
        return False

# ====== BACKWARD COMPATIBILITY FUNCTIONS ======
def send_assessment_results_email(data):
    """Backward compatibility for assessment results"""
    return send_clinical_assessment_results(data)

def send_contact_form_email(data):
    """Backward compatibility for contact forms"""
    # Convert contact form data to booking format
    booking_data = {
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'concern': data.get('concern', ''),
        'message': data.get('message', ''),
        'urgency': data.get('urgency', ''),
        'experience': data.get('experience', '')
    }
    return send_discovery_call_email(booking_data)

def send_booking_confirmation_email(data):
    """Backward compatibility for booking confirmations"""
    return send_discovery_call_email(data)
