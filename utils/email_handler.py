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
Improved clinical email handler for hypnotherapy assessment
Streamlined, practical, and data-driven approach
"""
import smtplib
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class ImprovedClinicalEmailHandler:
    """Streamlined email handler focusing on actionable clinical insights"""

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        try:
            self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
            self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
        except Exception as e:
            print(f"[DEBUG] error accessing secrets: {e}")
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD")

        # pattern definitions for clinical analysis
        self.patterns = {
            1: "unhappiness culture", 2: "power struggles", 3: "systematic mistrust", 4: "separation and division",
            5: "doing versus being", 6: "compartmentalized authenticity", 7: "self sacrifice and care avoidance",
            8: "inherited missions", 9: "context dependent weakness"
        }

    def send_clinical_assessment_results(self, clinical_data):
        """Send streamlined clinical assessment with practical insights"""
        try:
            print("[DEBUG] sending clinical assessment results email")
            
            # extract urgency for subject priority
            urgency = clinical_data.get('urgency', 'standard priority')
            risk_flags = clinical_data.get('assessment_results', {}).get('risk_flags', [])
            priority_flag = self._get_priority_flag(urgency, risk_flags)
            
            msg = self._build_email(
                subject=f"{priority_flag} behavioral pattern assessment - {clinical_data.get('name', 'new client')}",
                body=self._format_clinical_email(clinical_data)
            )
            
            return self._dispatch(msg, clinical_data, "clinical assessment")
            
        except Exception as e:
            print(f"[ERROR] exception in send_clinical_assessment_results: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _get_priority_flag(self, urgency, risk_flags):
        """get priority flag for email subject"""
        if len(risk_flags) >= 3:
            return "🔴 HIGH RISK"
        elif 'extremely urgent' in urgency.lower():
            return "🔴 URGENT" 
        elif 'very urgent' in urgency.lower():
            return "🟡 PRIORITY"
        else:
            return "📋 STANDARD"

    def _format_clinical_email(self, data):
        """format practical clinical email focused on actionable insights"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # extract basic client data
            name = data.get('name', 'unknown client')
            email = data.get('email', 'not provided')
            phone = data.get('phone', 'not provided')
            urgency = data.get('urgency', 'not specified')
            primary_concern = data.get('primary_concern', 'not provided')
            next_step = data.get('next_step', 'not specified')
            
            # extract assessment results
            assessment_results = data.get('assessment_results', {})
            pattern_scores = assessment_results.get('pattern_scores', {})
            risk_flags = assessment_results.get('risk_flags', [])
            total_questions = assessment_results.get('total_questions_answered', 0)
            completion_rate = assessment_results.get('completion_rate', 1.0)
            adaptive_triggered = assessment_results.get('adaptive_paths_triggered', [])
            intensity_data = assessment_results.get('intensity_data', {})
            
            # extract key responses for clinical insights
            responses = data.get('assessment_responses', {})
            presenting_problem = self._extract_presenting_problem(responses)
            triggers = self._extract_triggers(responses)
            physical_response = self._extract_physical_response(responses)
            emotions = self._extract_emotions(responses)
            inner_voice = self._extract_inner_voice(responses)
            behavioral_response = self._extract_behavioral_response(responses)
            secondary_gains = self._extract_secondary_gains(responses)
            
            # analyze dominant patterns
            dominant_patterns = self._analyze_dominant_patterns(pattern_scores)
            
            # build email body
            body = f"""
BEHAVIORAL PATTERN ASSESSMENT RESULTS
assessment completed: {timestamp}

CLIENT INFORMATION
name: {name}
email: {email}
phone: {phone}
urgency: {urgency}
primary concern: {primary_concern}
preferred next step: {next_step}

ASSESSMENT OVERVIEW
questions completed: {total_questions}
completion rate: {completion_rate*100:.0f}%
risk factors identified: {len(risk_flags)}
adaptive modules triggered: {len(adaptive_triggered)}
average intensity rating: {self._calculate_average_intensity(intensity_data)}

═══════════════════════════════════════════════════════

PRESENTING PROBLEM ANALYSIS

target behavior for transformation:
{presenting_problem}

typical triggering situation:
{triggers}

physical response pattern:
{physical_response}

emotional response pattern:
{emotions}

automatic thoughts:
{inner_voice}

behavioral response:
{behavioral_response}

secondary gains (what they might lose):
{secondary_gains}

INTERVENTION STRATEGY:
{self._generate_intervention_strategy(presenting_problem, triggers, physical_response)}

═══════════════════════════════════════════════════════

DOMINANT BEHAVIORAL PATTERNS

{self._format_pattern_analysis(dominant_patterns)}

THERAPEUTIC APPROACH:
{self._recommend_therapeutic_approach(dominant_patterns)}

SESSION 1 FOCUS:
{self._recommend_session_1_focus(dominant_patterns, risk_flags)}

═══════════════════════════════════════════════════════

HYPNOTHERAPY SCRIPT GUIDANCE

INDUCTION APPROACH:
{self._recommend_induction_approach(responses, dominant_patterns)}

PRIMARY SUGGESTIONS:
{self._generate_primary_suggestions(dominant_patterns, presenting_problem)}

THERAPEUTIC LANGUAGE TO USE:
{self._recommend_therapeutic_language(dominant_patterns)}

LANGUAGE TO AVOID:
{self._identify_language_to_avoid(dominant_patterns)}

═══════════════════════════════════════════════════════

CLINICAL CONSIDERATIONS

{self._format_clinical_considerations(risk_flags, urgency)}

RESISTANCE FACTORS:
{self._identify_resistance_factors(secondary_gains, dominant_patterns)}

SAFETY PROTOCOLS:
{self._recommend_safety_protocols(risk_flags)}

═══════════════════════════════════════════════════════

TREATMENT RECOMMENDATIONS

ESTIMATED SESSIONS: {self._estimate_session_count(dominant_patterns, risk_flags)}
RECOMMENDED FREQUENCY: {self._recommend_frequency(urgency, risk_flags)}
PROGNOSIS: {self._assess_prognosis(dominant_patterns, completion_rate, risk_flags)}

SESSION STRUCTURE:
1. rapport building using {self._get_rapport_approach(dominant_patterns)}
2. pattern interruption at: {self._identify_intervention_point(physical_response, emotions)}
3. root cause transformation: {self._identify_root_focus(dominant_patterns)}
4. new pattern installation and future pacing

HOMEWORK PROTOCOL:
{self._recommend_homework(dominant_patterns, responses)}

═══════════════════════════════════════════════════════

NEXT ACTIONS

CONTACT TIMELINE: {self._get_contact_timeline(urgency, risk_flags)}

IMMEDIATE PRIORITIES:
{self._generate_action_priorities(urgency, risk_flags, next_step)}

PREPARATION NOTES:
- review complete assessment responses before session
- prepare {self._get_induction_type(responses)} induction approach
- plan for potential resistance around {self._get_main_resistance_area(secondary_gains)}
- have {self._get_safety_preparations(risk_flags)} ready

═══════════════════════════════════════════════════════

RAW ASSESSMENT DATA SUMMARY
total responses: {len(responses)}
text responses: {sum(1 for r in responses.values() if r.get('question_type') == 'text_completion')}
intensity ratings: {len(intensity_data)}
adaptive paths: {', '.join(adaptive_triggered) if adaptive_triggered else 'none'}
risk indicators: {', '.join(risk_flags) if risk_flags else 'none'}

bangkok hypnotherapy clinic - clinical assessment system
generated: {timestamp}
clinical review required within: {self._get_review_timeline(urgency, risk_flags)}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] error formatting clinical email: {e}")
            import traceback
            traceback.print_exc()
            return f"""
CLINICAL ASSESSMENT RESULTS - FORMATTING ERROR

basic client information:
name: {data.get('name', 'unknown')}
email: {data.get('email', 'unknown')}
urgency: {data.get('urgency', 'unknown')}
timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

error: {str(e)}

raw data preserved for manual review
contact technical support for data recovery

bangkok hypnotherapy clinic
            """

    def _extract_presenting_problem(self, responses):
        """extract presenting problem from responses"""
        for response_data in responses.values():
            if 'transform' in response_data.get('question_text', '').lower():
                return response_data.get('response', 'not specified')
        return 'not provided in assessment'

    def _extract_triggers(self, responses):
        """extract triggering situations"""
        for response_data in responses.values():
            if 'typical situation that triggers' in response_data.get('question_text', '').lower():
                return response_data.get('response', 'not specified')
        return 'not identified in assessment'

    def _extract_physical_response(self, responses):
        """extract physical response patterns"""
        for response_data in responses.values():
            if 'first physical sensation' in response_data.get('question_text', '').lower():
                response = response_data.get('response', 'not specified')
                intensity = response_data.get('intensity', '')
                if intensity:
                    return f"{response} (intensity: {intensity}/7)"
                return response
        return 'not identified'

    def _extract_emotions(self, responses):
        """extract emotional response patterns"""
        for response_data in responses.values():
            if 'emotions surface' in response_data.get('question_text', '').lower():
                response = response_data.get('response')
                if isinstance(response, dict):
                    # weighted multi-select response
                    emotions = []
                    for emotion, intensity in response.items():
                        emotions.append(f"{emotion} ({intensity}/7)")
                    return '; '.join(emotions)
                elif isinstance(response, str):
                    return response
        return 'not identified'

    def _extract_inner_voice(self, responses):
        """extract automatic thoughts/inner voice"""
        for response_data in responses.values():
            if 'inner voice typically says' in response_data.get('question_text', '').lower():
                response = response_data.get('response', 'not specified')
                intensity = response_data.get('intensity', '')
                if intensity:
                    return f"{response} (intensity: {intensity}/7)"
                return response
        return 'not identified'

    def _extract_behavioral_response(self, responses):
        """extract behavioral response patterns"""
        for response_data in responses.values():
            if 'typical behavioral response' in response_data.get('question_text', '').lower():
                return response_data.get('response', 'not specified')
        return 'not identified'

    def _extract_secondary_gains(self, responses):
        """extract secondary gains"""
        for response_data in responses.values():
            if 'what would you lose if this pattern' in response_data.get('question_text', '').lower():
                return response_data.get('response', 'not identified')
        return 'not explored in assessment'

    def _analyze_dominant_patterns(self, pattern_scores):
        """analyze and return dominant patterns with scores"""
        if not pattern_scores:
            return []
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant_patterns = []
        for pattern_id, score in sorted_patterns:
            pattern_name = self.patterns.get(pattern_id, f'pattern {pattern_id}')
            intensity = 'high' if score >= 5 else 'moderate' if score >= 3 else 'mild'
            dominant_patterns.append({
                'id': pattern_id,
                'name': pattern_name,
                'score': score,
                'intensity': intensity
            })
        
        return dominant_patterns

    def _format_pattern_analysis(self, dominant_patterns):
        """format pattern analysis for email"""
        if not dominant_patterns:
            return "no clear dominant patterns identified - general therapeutic approach recommended"
        
        analysis = []
        for i, pattern in enumerate(dominant_patterns[:3]):  # top 3 patterns
            level = ['PRIMARY', 'SECONDARY', 'TERTIARY'][i]
            analysis.append(f"{level} PATTERN: {pattern['name']} (score: {pattern['score']:.1f} - {pattern['intensity']} intensity)")
            analysis.append(f"  clinical focus: {self._get_pattern_focus(pattern['id'])}")
            analysis.append("")
        
        if len(dominant_patterns) > 3:
            analysis.append(f"additional patterns detected: {len(dominant_patterns) - 3}")
            for pattern in dominant_patterns[3:]:
                analysis.append(f"  • {pattern['name']}: {pattern['score']:.1f}")
        
        return '\n'.join(analysis)

    def _get_pattern_focus(self, pattern_id):
        """get clinical focus for each pattern"""
        focuses = {
            1: "permission for happiness and positive experiences",
            2: "collaborative empowerment vs control needs", 
            3: "trust building with evidence-based transparency",
            4: "expanding either/or thinking to multiple possibilities",
            5: "separating worth from achievement - being vs doing",
            6: "authentic self expression across all contexts",
            7: "healthy boundaries and balanced self-care",
            8: "personal authenticity while honoring family values",
            9: "consistent strength and boundaries across contexts"
        }
        return focuses.get(pattern_id, "pattern-specific identity transformation")

    def _recommend_therapeutic_approach(self, dominant_patterns):
        """recommend overall therapeutic approach"""
        if not dominant_patterns:
            return "standard collaborative hypnotherapy with pattern awareness"
        
        primary = dominant_patterns[0]
        approaches = {
            1: "permission-focused therapy - validate struggles before introducing positivity",
            2: "collaborative non-directive approach - avoid authoritarian language",
            3: "transparency-based trust building - explain all techniques clearly",
            4: "integration-focused therapy - expand binary thinking to multiple options",
            5: "being-centered approach - emphasize intrinsic worth over achievement",
            6: "authenticity integration - consistent identity across contexts",
            7: "balanced care approach - self-care as strength for service",
            8: "family-honoring individuation - respect values while expanding choice",
            9: "consistency training - maintaining boundaries across all situations"
        }
        
        base_approach = approaches.get(primary['id'], "individualized pattern-specific approach")
        
        # modify based on secondary patterns
        if len(dominant_patterns) > 1:
            secondary = dominant_patterns[1]
            if secondary['score'] >= 4:  # significant secondary pattern
                base_approach += f" with attention to {self.patterns[secondary['id']]} patterns"
        
        return base_approach

    def _recommend_session_1_focus(self, dominant_patterns, risk_flags):
        """recommend focus for first session"""
        if risk_flags:
            return "rapport building with safety assessment and risk management protocols"
        
        if not dominant_patterns:
            return "general assessment, rapport building, and initial pattern interruption"
        
        primary = dominant_patterns[0]
        session_1_focuses = {
            1: "validate current struggles, build permission for small positive experiences",
            2: "establish collaborative therapeutic relationship, shared control of session",
            3: "build trust through transparency, explain therapeutic rationale clearly",
            4: "explore current either/or thinking, introduce possibility of multiple options",
            5: "separate worth from performance, appreciate client for who they are",
            6: "encourage authentic expression in session, model consistency",
            7: "model balanced care, encourage attention to own needs during session",
            8: "honor their values while gently exploring personal desires",
            9: "establish consistent therapeutic boundaries as foundation"
        }
        
        return session_1_focuses.get(primary['id'], "pattern assessment and initial intervention point identification")

    def _recommend_induction_approach(self, responses, dominant_patterns):
        """recommend induction approach based on trance capacity and patterns"""
        # find trance capacity response
        trance_capacity = "standard"
        for response_data in responses.values():
            if 'absorbed in movies' in response_data.get('question_text', '').lower():
                response = response_data.get('response', '')
                if 'very easily' in response.lower():
                    trance_capacity = "high"
                elif 'never' in response.lower():
                    trance_capacity = "low"
                break
        
        # adjust for patterns
        if dominant_patterns:
            primary = dominant_patterns[0]
            if primary['id'] == 2:  # power struggles
                return "permissive induction with client choice and control"
            elif primary['id'] == 3:  # mistrust
                return "transparent explained induction with clear rationale"
        
        if trance_capacity == "high":
            return "standard progressive relaxation - client likely very responsive"
        elif trance_capacity == "low":
            return "conversational induction or mindfulness-based approach"
        else:
            return "standard progressive relaxation with responsiveness testing"

    def _generate_primary_suggestions(self, dominant_patterns, presenting_problem):
        """generate primary hypnotic suggestions"""
        if not dominant_patterns:
            return f"when [triggering situation] occurs, you naturally respond with strength and wisdom instead of {presenting_problem}"
        
        primary = dominant_patterns[0]
        suggestions = {
            1: "you give yourself full permission to experience happiness and positive emotions naturally",
            2: "you find collaboration more satisfying than control, choosing cooperation naturally",
            3: "you trust your ability to assess situations while remaining open to connection",
            4: "you see multiple possibilities in every situation, finding creative solutions easily",
            5: "your worth exists simply because you are - independent of any achievement",
            6: "you express your authentic self consistently and confidently in every context",
            7: "you care for yourself with the same love you show others, naturally and easily",
            8: "you honor your family while confidently following your own authentic path",
            9: "you maintain your strength and boundaries consistently in every situation"
        }
        
        return suggestions.get(primary['id'], "you respond to challenging situations with natural confidence and wisdom")

    def _recommend_therapeutic_language(self, dominant_patterns):
        """recommend therapeutic language to use"""
        if not dominant_patterns:
            return "positive, supportive language focused on strength and capability"
        
        primary = dominant_patterns[0]
        language_recommendations = {
            1: "permission language: 'you can allow yourself...', 'it's safe to experience...'",
            2: "invitation language: 'you might discover...', 'perhaps you'll find...'", 
            3: "evidence-based language: 'as you notice...', 'you can see how...'",
            4: "both/and language: 'you can have both...', 'multiple possibilities exist...'",
            5: "being language: 'simply by being yourself...', 'your natural worth...'",
            6: "consistency language: 'your authentic self...', 'naturally expressing...'",
            7: "balanced language: 'caring for yourself strengthens...', 'healthy boundaries...'",
            8: "honoring language: 'respecting your family while...', 'your authentic path...'",
            9: "strength language: 'your consistent strength...', 'maintaining your values...'"
        }
        
        return language_recommendations.get(primary['id'], "supportive, strength-based language")

    def _identify_language_to_avoid(self, dominant_patterns):
        """identify language to avoid based on patterns"""
        if not dominant_patterns:
            return "avoid negative language, focus on what they will do rather than what they won't"
        
        primary = dominant_patterns[0]
        avoid_language = {
            1: "avoid forced positivity: 'you should be happy', 'just think positive'",
            2: "avoid commands: 'you will...', 'you must...', any directive language",
            3: "avoid vague promises: 'trust me', 'just believe', unexplained techniques",
            4: "avoid either/or language: 'you must choose', 'it's this or that'",
            5: "avoid achievement pressure: 'you need to accomplish', 'prove yourself'",
            6: "avoid role-based language: 'as a [role]', context-specific identities",
            7: "avoid guilt language: 'you should care for others', 'selfishness'",
            8: "avoid family guilt: 'disappoint your family', loyalty vs personal choice",
            9: "avoid inconsistency: changing therapeutic approach or boundaries"
        }
        
        return avoid_language.get(primary['id'], "avoid negative language and limiting statements")

    def _format_clinical_considerations(self, risk_flags, urgency):
        """format clinical considerations section"""
        considerations = []
        
        if risk_flags:
            considerations.append(f"RISK FACTORS IDENTIFIED: {len(risk_flags)}")
            for flag in risk_flags:
                considerations.append(f"  • {flag}")
                considerations.append(f"    protocol: {self._get_risk_protocol(flag)}")
        else:
            considerations.append("no significant risk factors identified - standard protocols apply")
        
        if 'extremely urgent' in urgency.lower():
            considerations.append("URGENCY: extremely urgent - prioritize immediate scheduling")
        elif 'very urgent' in urgency.lower():
            considerations.append("URGENCY: very urgent - expedite response and scheduling")
        
        return '\n'.join(considerations)

    def _get_risk_protocol(self, flag):
        """get protocol for specific risk flag"""
        protocols = {
            'risk_q_11': "monitor emotional regulation during session",
            'risk_q_12': "use grounding techniques, avoid regression work",
            'risk_q_13': "coordinate with medical care if needed"
        }
        return protocols.get(flag, "standard clinical precautions")

    def _identify_resistance_factors(self, secondary_gains, dominant_patterns):
        """identify potential resistance factors"""
        factors = []
        
        if secondary_gains and 'not' not in secondary_gains.lower():
            factors.append(f"secondary gains present: {secondary_gains[:100]}...")
        
        if dominant_patterns:
            primary = dominant_patterns[0]
            pattern_resistance = {
                1: "may resist positive suggestions initially",
                2: "likely to challenge therapeutic authority",
                3: "will evaluate therapist trustworthiness carefully",
                4: "may feel trapped by limited options",
                5: "might try to 'perform' as good client",
                6: "may present differently than in real life",
                7: "may focus on therapist needs over own",
                8: "could worry about disappointing therapist",
                9: "may become compliant in session but not outside"
            }
            factors.append(pattern_resistance.get(primary['id'], "standard resistance patterns possible"))
        
        return '\n'.join(factors) if factors else "low resistance anticipated"

    def _recommend_safety_protocols(self, risk_flags):
        """recommend safety protocols"""
        if not risk_flags:
            return "standard clinical safety protocols sufficient"
        
        protocols = []
        for flag in risk_flags:
            if 'q_12' in flag:  # dissociation/panic/self-harm question
                protocols.append("use grounding techniques, shorter sessions initially")
            elif 'q_11' in flag:  # emotional intensity question
                protocols.append("monitor emotional regulation, have calming techniques ready")
        
        return '; '.join(protocols) if protocols else "monitor closely, standard precautions"

    def _calculate_average_intensity(self, intensity_data):
        """calculate average intensity rating"""
        if not intensity_data:
            return "not measured"
        
        values = list(intensity_data.values())
        if values:
            avg = sum(values) / len(values)
            return f"{avg:.1f}/7"
        return "not available"

    def _generate_intervention_strategy(self, presenting_problem, triggers, physical_response):
        """generate intervention strategy based on behavioral chain"""
        if 'not' in physical_response.lower():
            return "cognitive intervention - focus on thought pattern interruption"
        elif physical_response != 'not identified':
            return f"somatic intervention - use physical awareness to interrupt pattern before {presenting_problem}"
        elif triggers != 'not identified':
            return "environmental intervention - modify response to triggering situations"
        else:
            return "general pattern interruption and response modification"

    def _estimate_session_count(self, dominant_patterns, risk_flags):
        """estimate number of sessions needed"""
        base_sessions = 3  # standard rapid transformation
        
        if risk_flags:
            base_sessions += 1  # additional session for safety
        
        if dominant_patterns and len(dominant_patterns) >= 2:
            if dominant_patterns[1]['score'] >= 4:
                base_sessions += 1  # significant secondary pattern
        
        return f"{base_sessions}-{base_sessions + 2} sessions"

    def _recommend_frequency(self, urgency, risk_flags):
        """recommend session frequency"""
        if 'extremely urgent' in urgency.lower():
            return "weekly initially, then bi-weekly"
        elif risk_flags:
            return "weekly with close monitoring"
        else:
            return "weekly for 3 sessions, then monthly maintenance"

    def _assess_prognosis(self, dominant_patterns, completion_rate, risk_flags):
        """assess treatment prognosis"""
        prognosis_score = 0
        
        if completion_rate >= 0.9:
            prognosis_score += 2
        elif completion_rate >= 0.7:
            prognosis_score += 1
        
        if not risk_flags:
            prognosis_score += 1
        
        if dominant_patterns and len(dominant_patterns) <= 2:
            prognosis_score += 1
        
        if prognosis_score >= 4:
            return "excellent - expect rapid transformation"
        elif prognosis_score >= 2:
            return "good - expect steady progress"
        else:
            return "fair - may require longer treatment"

    def _get_rapport_approach(self, dominant_patterns):
        """get rapport building approach"""
        if not dominant_patterns:
            return "standard collaborative approach"
        
        primary = dominant_patterns[0]
        approaches = {
            1: "validate struggles genuinely",
            2: "collaborative equal partnership",
            3: "transparent trustworthy approach",
            4: "flexible with multiple options",
            5: "appreciate for who they are",
            6: "authentic consistent presence",
            7: "balanced professional boundaries",
            8: "respectful of their values",
            9: "reliable consistent approach"
        }
        
        return approaches.get(primary['id'], "client-specific approach")

    def _identify_intervention_point(self, physical_response, emotions):
        """identify optimal intervention point"""
        if physical_response and 'not identified' not in physical_response:
            return "somatic awareness point - physical sensation"
        elif emotions and 'not identified' not in emotions:
            return "emotional awareness point - feeling state"
        else:
            return "cognitive level - thought patterns"

    def _identify_root_focus(self, dominant_patterns):
        """identify root cause focus"""
        if not dominant_patterns:
            return "general limiting belief transformation"
        
        primary = dominant_patterns[0]
        root_focuses = {
            1: "early messages about happiness being dangerous",
            2: "early powerlessness leading to control needs",
            3: "early trust violations or inconsistency",
            4: "early forced either/or family dynamics",
            5: "early conditional love based on performance",
            6: "early need to be different for acceptance",
            7: "early caretaker role beyond age capacity",
            8: "early family expectations vs personal desires",
            9: "early contexts where strength led to problems"
        }
        
        return root_focuses.get(primary['id'], "core identity and belief system")

    def _recommend_homework(self, dominant_patterns, responses):
        """recommend homework based on patterns and trance capacity"""
        if not dominant_patterns:
            return "daily pattern awareness and basic self-hypnosis practice"
        
        primary = dominant_patterns[0]
        homework = {
            1: "daily happiness permission practice - notice positive moments without guilt",
            2: "daily collaboration practice - choose cooperation over control once daily",
            3: "daily trust calibration - practice appropriate trust with evidence",
            4: "daily both/and thinking - expand either/or thoughts to possibilities",
            5: "daily being practice - moments of worth not tied to doing",
            6: "daily authenticity practice - consistent self across contexts",
            7: "daily self-care practice - care for self as you would a friend",
            8: "daily authentic desire check-in - separate from family expectations",
            9: "daily boundary practice - consistent values across all contexts"
        }
        
        base_homework = homework.get(primary['id'], "daily pattern awareness practice")
        
        # add self-hypnosis based on capacity
        trance_capacity = "standard"
        for response_data in responses.values():
            if 'absorbed in movies' in response_data.get('question_text', '').lower():
                response = response_data.get('response', '')
                if 'very easily' in response.lower():
                    trance_capacity = "high"
                elif 'never' in response.lower():
                    trance_capacity = "low"
                break
        
        if trance_capacity == "high":
            base_homework += "\nself-hypnosis: 15-20 minute daily practice with recorded session"
        elif trance_capacity == "low":
            base_homework += "\nmindfulness: 5-10 minute daily awareness practice"
        else:
            base_homework += "\nself-hypnosis: 10-15 minute daily practice with simple relaxation"
        
        return base_homework

    def _get_contact_timeline(self, urgency, risk_flags):
        """get contact timeline based on urgency and risk"""
        if len(risk_flags) >= 3:
            return "within 24 hours - multiple risk factors present"
        elif 'extremely urgent' in urgency.lower():
            return "within 24 hours - client urgency level"
        elif 'very urgent' in urgency.lower():
            return "within 48 hours - priority response"
        else:
            return "within 72 hours - standard response time"

    def _generate_action_priorities(self, urgency, risk_flags, next_step):
        """generate immediate action priorities"""
    def _generate_action_priorities(self, urgency, risk_flags, next_step):
        """generate immediate action priorities"""
        priorities = []
        
        if risk_flags:
            priorities.append("1. review risk factors and prepare safety protocols")
        
        if 'extremely urgent' in urgency.lower():
            priorities.append("2. prioritize immediate scheduling - offer within 48-72 hours")
        
        if 'consultation' in next_step.lower():
            priorities.append("3. schedule discovery call first per client preference")
        elif 'analysis' in next_step.lower():
            priorities.append("3. send analysis summary before scheduling session")
        
        priorities.append("4. prepare session materials based on dominant patterns")
        priorities.append("5. review complete assessment data before contact")
        
        return '\n'.join(priorities)

    def _get_induction_type(self, responses):
        """get recommended induction type"""
        for response_data in responses.values():
            if 'absorbed in movies' in response_data.get('question_text', '').lower():
                response = response_data.get('response', '')
                if 'very easily' in response.lower():
                    return "progressive relaxation"
                elif 'never' in response.lower():
                    return "conversational"
                break
        return "standard progressive relaxation"

    def _get_main_resistance_area(self, secondary_gains):
        """get main area of potential resistance"""
        if secondary_gains and 'not' not in secondary_gains.lower():
            if len(secondary_gains) > 50:
                return "secondary gains from current pattern"
            else:
                return "change process in general"
        return "minimal resistance expected"

    def _get_safety_preparations(self, risk_flags):
        """get safety preparations needed"""
        if not risk_flags:
            return "standard safety protocols"
        
        preparations = []
        for flag in risk_flags:
            if 'q_12' in flag:
                preparations.append("grounding techniques")
            elif 'q_11' in flag:
                preparations.append("emotional regulation support")
        
        return ', '.join(preparations) if preparations else "standard precautions"

    def _get_review_timeline(self, urgency, risk_flags):
        """get clinical review timeline"""
        if risk_flags:
            return "24 hours for safety assessment"
        elif 'extremely urgent' in urgency.lower():
            return "24-48 hours for priority response"
        else:
            return "48-72 hours standard review"

    def _build_email(self, subject, body):
        """build email message"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            return msg
        except Exception as e:
            print(f"[ERROR] error building email: {e}")
            raise

    def _dispatch(self, msg, data, email_type):
        """dispatch email with error handling"""
        try:
            print(f"[DEBUG] dispatching {email_type} email")
            
            if not self.password:
                print(f"[DEBUG] {email_type} email would be sent (no password configured)")
                return True
            
            if not self.sender_email or not self.recipient_email:
                print(f"[ERROR] missing email configuration for {email_type}")
                return False
                
            return self._send_email(msg)
            
        except Exception as e:
            print(f"[ERROR] exception in _dispatch: {e}")
            return False

    def _send_email(self, msg):
        """send email via gmail smtp"""
        try:
            print("[DEBUG] attempting to send email via smtp")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            
            print(f"[SUCCESS] email sent from {self.sender_email} to {self.recipient_email}")
            return True
            
        except Exception as e:
            print(f"[ERROR] error sending email: {e}")
            return False


# global instance and helper functions
clinical_email_handler = ImprovedClinicalEmailHandler()

def send_clinical_assessment_results(data):
    """send clinical assessment results email - main function called by assess.py"""
    try:
        print("[DEBUG] improved clinical email handler - send_clinical_assessment_results called")
        return clinical_email_handler.send_clinical_assessment_results(data)
    except Exception as e:
        print(f"[ERROR] exception in global send_clinical_assessment_results: {e}")
        import traceback
        traceback.print_exc()
        return False

# backward compatibility functions
def send_assessment_results_email(data):
    """backward compatibility for assessment results"""
    return send_clinical_assessment_results(data)

def send_discovery_call_email(data):
    """backward compatibility for discovery calls"""  
    return send_clinical_assessment_results(data)

def send_contact_form_email(data):
    """backward compatibility for contact forms"""
    return send_clinical_assessment_results(data)

def send_booking_confirmation_email(data):
    """backward compatibility for booking confirmations"""
    return send_clinical_assessment_results(data)
