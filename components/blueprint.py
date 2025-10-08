# """
# Blueprint Component - Premium Clinical Analysis (Production Ready)
# ENHANCED VERSION - Utilizes ALL captured assessment data for personalization

# Key Improvements:
# 1. Personalized mantras from user's actual language (Q1, Q37, Q70, Q74)
# 2. Success metrics from user's visions (Q74, Q75, Q76)
# 3. Technique scripts from trigger sequence + responses
# 4. Crisis resources if indicators detected
# 5. Single primary PDF download button
# 6. Complete data utilization from master_analytics
# """

# import streamlit as st
# from typing import Dict, Optional, List, Tuple
# from datetime import datetime
# import plotly.graph_objects as go
# import re


# class BehavioralBlueprint:
#     """Renders complete clinical blueprint with full data personalization"""

#     def __init__(self):
#         self.pattern_names = {
#             1: "Unhappiness culture", 2: "Power struggles", 3: "Systematic mistrust",
#             4: "Separation and division", 5: "Doing versus being", 
#             6: "Compartmentalized authenticity", 7: "Self sacrifice and care avoidance",
#             8: "Inherited missions", 9: "Context dependent weakness", 
#             10: "Digital reality dissociation"
#         }
#         self._apply_print_friendly_styles()

#     def _apply_print_friendly_styles(self):
#         """Styles optimized for both screen and print/PDF - per color palette"""
#         st.markdown("""
#             <style>
#             @media print {
#                 .stButton, .stDownloadButton { display: none; }
#                 .insight-card { page-break-inside: avoid; }
#             }
            
#             /* Color palette compliance */
#             .insight-card {
#                 background: #FFFFFF;
#                 padding: 1.5rem;
#                 border-radius: 8px;
#                 margin: 1rem 0;
#                 border-left: 4px solid #4CA1A3;
#                 box-shadow: 0 2px 8px rgba(0,0,0,0.08);
#             }
            
#             .action-item {
#                 background: #E1F0F0;
#                 padding: 1rem;
#                 border-radius: 6px;
#                 margin: 0.5rem 0;
#                 border-left: 3px solid #22c55e;
#             }
            
#             .mantra-box {
#                 background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
#                 color: white;
#                 padding: 1.5rem;
#                 border-radius: 12px;
#                 margin: 1rem 0;
#                 font-size: 1rem;
#                 font-weight: 500;
#                 line-height: 1.6;
#             }
            
#             .metric-card {
#                 background: #F3F6F8;
#                 padding: 1rem;
#                 border-radius: 8px;
#                 text-align: center;
#                 border: 1px solid #CBD5E1;
#             }
            
#             .session-card {
#                 background: #ffffff;
#                 padding: 1.5rem;
#                 border-radius: 8px;
#                 margin: 1rem 0;
#                 border: 2px solid #4CA1A3;
#             }
            
#             .crisis-alert {
#                 background: #fee2e2;
#                 border-left: 6px solid #ef4444;
#                 padding: 1.5rem;
#                 border-radius: 8px;
#                 margin: 1rem 0;
#             }
            
#             .success-indicator {
#                 background: #dcfce7;
#                 border-left: 4px solid #22c55e;
#                 padding: 1rem;
#                 border-radius: 6px;
#                 margin: 0.5rem 0;
#             }
            
#             /* Typography per guidelines */
#             h1 { font-size: 2.2rem; color: #273548; margin-bottom: 0.5rem; }
#             h2 { font-size: 1.8rem; color: #273548; margin-top: 2rem; margin-bottom: 1rem; }
#             h3 { font-size: 1.4rem; color: #4CA1A3; margin-top: 1.5rem; }
#             h4 { font-size: 1.2rem; color: #4CA1A3; }
#             body, p, li { font-size: 1rem; color: #273548; line-height: 1.6; }
#             .caption-text { font-size: 0.9rem; color: #556D7A; }
#             </style>
#         """, unsafe_allow_html=True)
    
#     def render_complete_blueprint(self, assessment_data: Dict):
#         """Render complete premium blueprint with FULL data utilization"""
        
#         try:
#             master_analytics = assessment_data.get('master_analytics', {})
#             responses = assessment_data.get('responses', {})
            
#             if not master_analytics:
#                 st.error("Analysis data not available. Please complete assessment first.")
#                 return
            
#             # Single primary download button at top
#             self._render_primary_download_section(assessment_data)
            
#             st.markdown("---")
            
#             # Table of contents
#             self._render_table_of_contents()
            
#             # 1. Personal cover page
#             self._render_cover_page(assessment_data)
            
#             # 2. Crisis resources (if needed - PRIORITY)
#             self._render_crisis_resources_if_needed(responses, master_analytics)
            
#             # 3. Quick reference card
#             self._render_quick_reference_card(master_analytics, responses)
            
#             # 4. PERSONALIZED mantras (uses Q1, Q37, Q70, Q74)
#             self._render_personalized_mantras(master_analytics, responses)
            
#             # 5. Complete pattern analysis with visualization
#             self._render_pattern_constellation(master_analytics)
            
#             # 6. Behavioral blueprint (trigger sequence)
#             self._render_trigger_blueprint(master_analytics, responses)
            
#             # 7. PERSONALIZED immediate techniques
#             self._render_personalized_techniques(master_analytics, responses)
            
#             # 8. Session roadmap with digital integration
#             self._render_integrated_session_roadmap(master_analytics)
            
#             # 9. PERSONALIZED success tracking
#             self._render_personalized_success_tracking(master_analytics, responses)
            
#             # 10. Transformation assets
#             self._render_transformation_assets(master_analytics, responses)
            
#         except Exception as e:
#             st.error(f"Error rendering blueprint: {str(e)}")
#             st.info("Please contact support if this issue persists.")
#             print(f"Blueprint rendering error: {str(e)}")
    
#     def _render_primary_download_section(self, assessment_data: Dict):
#         """Single primary PDF download button - PRODUCTION READY"""
#         st.markdown("## Your complete transformation blueprint")
#         st.caption("Complete clinical analysis with personalized techniques and roadmap")
        
#         try:
#             # Generate PDF
#             pdf_bytes = self._generate_comprehensive_pdf(assessment_data)
            
#             if pdf_bytes:
#                 contact = assessment_data.get('contact_info', {})
#                 name_slug = contact.get('full_name', 'client').lower().replace(' ', '_')
#                 filename = f"transformation_blueprint_{name_slug}_{datetime.now().strftime('%Y%m%d')}.pdf"
                
#                 # Primary centered download button
#                 col1, col2, col3 = st.columns([1, 2, 1])
#                 with col2:
#                     st.download_button(
#                         label="📥 Download your complete blueprint (PDF)",
#                         data=pdf_bytes,
#                         file_name=filename,
#                         mime="application/pdf",
#                         type="primary",
#                         use_container_width="stretch"
#                     )
#                     st.caption("*Professional PDF report - ready to print or save*")
#             else:
#                 st.warning("PDF generation temporarily unavailable. Viewing online version below.")
                
#         except Exception as e:
#             st.error("PDF download temporarily unavailable")
#             st.info("You can view your complete blueprint below")
#             print(f"PDF generation error: {str(e)}")
    
#     def _render_crisis_resources_if_needed(self, responses: Dict, master_analytics: Dict):
#         """PRIORITY: Add crisis resources if indicators detected"""
        
#         # Check for crisis keywords in text responses
#         crisis_keywords = ['suicide', 'kill myself', 'end my life', 'no point living', 
#                           'want to die', 'better off dead']
        
#         has_crisis = False
#         for response_data in responses.values():
#             if isinstance(response_data, dict):
#                 response_text = str(response_data.get('response', '')).lower()
#             else:
#                 response_text = str(response_data).lower()
                
#             if any(keyword in response_text for keyword in crisis_keywords):
#                 has_crisis = True
#                 break
        
#         # Also check assessment quality flags
#         quality = master_analytics.get('assessment_quality', {})
#         validation_flags = quality.get('validation_flags', [])
        
#         if has_crisis or 'crisis_indicator' in str(validation_flags):
#             st.markdown("## 🚨 Immediate support resources")
            
#             st.error("""
# **If you are in immediate danger or crisis**

# Please reach out for immediate help. You are not alone, and support is available 24/7.

# **24/7 crisis hotlines:**
# - **Thailand suicide hotline:** 1323
# - **Samaritans of Thailand:** 02-713-6793
# - **International crisis line:** [befrienders.org](https://www.befrienders.org)
# - **Emergency services:** 1669

# **Important:** Your therapist will prioritize contact within 2 hours. Please check your email and phone.
#             """)
            
#             # Safety planning worksheet
#             st.markdown("### Safety planning")
            
#             st.info("""
#             **Create your safety plan now:**
            
#             1. **Warning signs I can notice:**
#             - (Write down physical, emotional, mental signs)
            
#             2. **People I can contact:**
#             - Friend/family: _______________
#             - Crisis hotline: 1323
#             - Therapist: (will be provided)
            
#             3. **Safe places I can go:**
#             - _______________
#             - _______________
            
#             4. **Things that help me feel better:**
#             - _______________
#             - _______________
            
#             5. **Reasons for living:**
#             - _______________
#             - _______________
#             """)
            
#             st.markdown("---")
    
#     def _render_personalized_mantras(self, master_analytics: Dict, responses: Dict):
#         """ENHANCED: Generate mantras from user's ACTUAL language"""
#         st.markdown("## 💪 Your personal transformation mantras")
#         st.caption("Generated from YOUR words - read these daily")
        
#         try:
#             # Extract user's actual data
#             presenting_problem = self._extract_response_text(responses, 1)  # Q1
#             automatic_thought = self._extract_response_text(responses, 37)  # Q37
#             core_belief = self._extract_response_text(responses, 70)  # Q70
#             first_action = self._extract_response_text(responses, 74)  # Q74
            
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#             dominant = pattern_hierarchy.get('dominant_pattern', {})
#             pattern_id = dominant.get('id')
            
#             mantras = []
            
#             # Mantra 1: From presenting problem (Q1)
#             if presenting_problem:
#                 behavior = self._extract_key_behavior(presenting_problem)
#                 mantra1 = f"I am worthy even when I'm not {behavior}"
#                 mantras.append(('From your presenting concern', mantra1))
            
#             # Mantra 2: From core limiting belief (Q70) - INVERT IT
#             if core_belief:
#                 inverted_belief = self._invert_limiting_belief(core_belief)
#                 mantras.append(('Your new empowering belief', inverted_belief))
            
#             # Mantra 3: From automatic thought (Q37) - REFRAME IT
#             if automatic_thought:
#                 reframed_thought = self._reframe_automatic_thought(automatic_thought)
#                 mantras.append(('When that old thought appears', reframed_thought))
            
#             # Mantra 4: From first action vision (Q74)
#             if first_action:
#                 action = self._extract_key_action(first_action)
#                 mantra4 = f"I can {action} and remain whole"
#                 mantras.append(('Your immediate possibility', mantra4))
            
#             # Mantra 5: Pattern-specific (fallback)
#             if pattern_id:
#                 pattern_mantra = self._get_pattern_mantra(pattern_id)
#                 mantras.append(('Your pattern transformation', pattern_mantra))
            
#             # Render mantras
#             if mantras:
#                 for i, (source, mantra) in enumerate(mantras[:5], 1):
#                     st.markdown(f"""
#                     <div class="mantra-box">
#                         <div style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 0.5rem;">{source}</div>
#                         <div style="font-size: 1.1rem; font-weight: 600;">"{mantra}"</div>
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 # Fallback to pattern-based mantras
#                 self._render_pattern_based_mantras(pattern_hierarchy)
                
#         except Exception as e:
#             st.warning("Personalized mantras will be refined in session 1")
#             self._render_pattern_based_mantras(master_analytics.get('pattern_hierarchy', {}))
#             print(f"Personalized mantras error: {str(e)}")
    
#     def _extract_response_text(self, responses: Dict, question_id: int) -> str:
#         """Extract text response from responses dict"""
#         response_data = responses.get(question_id)
        
#         if isinstance(response_data, dict):
#             return str(response_data.get('response', ''))
#         elif isinstance(response_data, str):
#             return response_data
#         return ''
    
#     def _extract_key_behavior(self, presenting_problem: str) -> str:
#         """Extract key behavior from presenting problem text"""
#         # Simple extraction - take first meaningful phrase
#         text = presenting_problem.lower().strip()
        
#         # Common patterns to extract
#         if 'stop' in text or 'quit' in text:
#             # Extract what they want to stop
#             words = text.split()
#             for i, word in enumerate(words):
#                 if word in ['stop', 'quit', 'avoiding', 'procrastinating']:
#                     if i + 1 < len(words):
#                         return ' '.join(words[i+1:i+4])
        
#         # Default: take first 3-5 words
#         words = text.split()
#         return ' '.join(words[:min(5, len(words))])
    
#     def _invert_limiting_belief(self, core_belief: str) -> str:
#         """Invert limiting belief to empowering belief"""
#         text = core_belief.lower().strip()
        
#         # Common patterns and their inversions
#         inversions = {
#             "can't": "can",
#             "cannot": "can",
#             "never": "can always",
#             "not good enough": "enough exactly as I am",
#             "don't deserve": "deserve",
#             "impossible": "possible",
#             "won't work": "will work",
#             "too late": "never too late",
#             "not worthy": "worthy"
#         }
        
#         # Apply inversions
#         inverted = text
#         for old, new in inversions.items():
#             if old in inverted:
#                 inverted = inverted.replace(old, new)
#                 break
        
#         # Capitalize first letter
#         if inverted and inverted != text:
#             return inverted[0].upper() + inverted[1:]
        
#         # Default inversion
#         return "I am capable of transformation and growth"
    
#     def _reframe_automatic_thought(self, automatic_thought: str) -> str:
#         """Reframe automatic negative thought to empowering response"""
#         text = automatic_thought.lower().strip()
        
#         # Pattern-based reframes
#         if 'never' in text or 'always fail' in text:
#             return "Every moment is a new opportunity to choose differently"
#         elif 'not good enough' in text or 'inadequate' in text:
#             return "I am enough exactly as I am in this moment"
#         elif 'can\'t' in text or 'impossible' in text:
#             return "I am discovering new capabilities every day"
#         elif 'should' in text or 'must' in text:
#             return "I choose my path with compassion and wisdom"
#         elif 'everyone' in text or 'nobody' in text:
#             return "I release others' opinions and trust my own knowing"
        
#         # Default reframe
#         return "I choose to respond with awareness and compassion"
    
#     def _extract_key_action(self, first_action: str) -> str:
#         """Extract key action from first action vision"""
#         text = first_action.lower().strip()
        
#         # Remove common prefixes
#         prefixes = ['i would', 'i will', 'i could', 'i can', 'i\'d']
#         for prefix in prefixes:
#             if text.startswith(prefix):
#                 text = text[len(prefix):].strip()
#                 break
        
#         # Take first meaningful phrase (up to first comma or period)
#         if ',' in text:
#             text = text.split(',')[0]
#         if '.' in text:
#             text = text.split('.')[0]
        
#         # Clean up
#         text = text.strip()
        
#         # Ensure it starts with a verb
#         return text if text else "take my first step toward freedom"
    
#     def _render_pattern_based_mantras(self, pattern_hierarchy: Dict):
#         """Fallback: Pattern-based mantras if personalization fails"""
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
#         primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        
#         mantras = []
        
#         if dominant:
#             pattern_id = dominant.get('id')
#             mantras.append(self._get_pattern_mantra(pattern_id))
        
#         for pattern in primary_patterns[:2]:
#             pattern_id = pattern.get('id')
#             mantras.append(self._get_pattern_mantra(pattern_id))
        
#         for i, mantra in enumerate(mantras, 1):
#             st.markdown(f"""
#             <div class="mantra-box">
#                 <div style="font-size: 1.1rem; font-weight: 600;">"{mantra}"</div>
#             </div>
#             """, unsafe_allow_html=True)
    
#     def _render_personalized_techniques(self, master_analytics: Dict, responses: Dict):
#         """ENHANCED: Personalized techniques from trigger sequence + responses"""
#         st.markdown("## 🛠️ Your personalized intervention techniques")
#         st.caption("Start using these today - designed for YOUR specific patterns")
        
#         try:
#             trigger_analysis = master_analytics.get('trigger_sequence', {})
#             sequence = trigger_analysis.get('trigger_sequence', {})
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#             dominant = pattern_hierarchy.get('dominant_pattern', {})
            
#             # Extract user's specific data
#             automatic_thought = self._extract_response_text(responses, 37)
#             physical_response = sequence.get('physical_response', '')
#             emotional_response = sequence.get('emotional_response', '')
#             behavioral_response = sequence.get('behavioral_response', '')
            
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.markdown("### Somatic intervention")
#                 st.markdown(f"""
#                 <div class="action-item">
#                     <strong>When you notice: "{physical_response or 'physical tension'}"</strong><br><br>
#                     <strong>Immediate response:</strong><br>
#                     1. <strong>STOP</strong> - Freeze your body exactly as it is<br>
#                     2. <strong>BREATHE</strong> - 4 counts in, 6 counts out (3 times)<br>
#                     3. <strong>SCAN</strong> - Notice sensation without judgment<br>
#                     4. <strong>RELEASE</strong> - Consciously relax that area<br>
#                     5. <strong>GROUND</strong> - Feel feet on floor, present moment<br><br>
#                     <em>This interrupts the automatic chain before thoughts cascade</em>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown("### Cognitive reframe")
                
#                 if automatic_thought:
#                     reframed = self._reframe_automatic_thought(automatic_thought)
#                     st.markdown(f"""
#                     <div class="action-item">
#                         <strong>Old automatic thought:</strong><br>
#                         "{automatic_thought[:100]}..."<br><br>
#                         <strong>Your new response:</strong><br>
#                         "{reframed}"<br><br>
#                         <strong>Practice:</strong><br>
#                         Say the new response OUT LOUD 3 times daily,<br>
#                         even when not triggered<br><br>
#                         <em>This builds new neural pathways</em>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.markdown("""
#                     <div class="action-item">
#                         <strong>The PAUSE protocol:</strong><br><br>
#                         <strong>P</strong> - Pause what you're doing<br>
#                         <strong>A</strong> - Acknowledge the pattern<br>
#                         <strong>U</strong> - Understand it's protecting you<br>
#                         <strong>S</strong> - Select a new response<br>
#                         <strong>E</strong> - Execute with compassion<br><br>
#                         <em>Practice this 2-3 times daily, even when calm</em>
#                     </div>
#                     """, unsafe_allow_html=True)
            
#             # Behavioral substitution
#             st.markdown("### Behavioral substitution")
            
#             if behavioral_response:
#                 alternative = self._generate_alternative_behavior(behavioral_response)
#                 st.markdown(f"""
#                 <div class="action-item">
#                     <strong>Old automatic behavior:</strong><br>
#                     "{behavioral_response}"<br><br>
#                     <strong>Your new alternative:</strong><br>
#                     "{alternative}"<br><br>
#                     <strong>Implementation:</strong><br>
#                     • Prepare this response in advance<br>
#                     • Visualize yourself doing it successfully<br>
#                     • Start with easiest situations first<br>
#                     • Celebrate ANY attempt, even imperfect<br><br>
#                     <em>New behaviors feel awkward at first - this is normal</em>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Pattern-specific technique
#             st.markdown("### Pattern-specific mastery technique")
#             pattern_technique = self._get_pattern_specific_technique(dominant.get('id'))
#             st.markdown(f"""
#             <div class="action-item">
#                 {pattern_technique}
#             </div>
#             """, unsafe_allow_html=True)
            
#         except Exception as e:
#             st.warning("Detailed techniques will be provided in session 1")
#             self._render_generic_techniques()
#             print(f"Personalized techniques error: {str(e)}")
    
#     def _generate_alternative_behavior(self, old_behavior: str) -> str:
#         """Generate healthier alternative to automatic behavior"""
#         text = old_behavior.lower()
        
#         # Map old behaviors to healthier alternatives
#         if 'scroll' in text or 'social media' in text or 'phone' in text:
#             return "Take a 5-minute walk outside or call a real person"
#         elif 'avoid' in text or 'withdraw' in text or 'isolate' in text:
#             return "Text one person you trust: 'I'm struggling and could use connection'"
#         elif 'argue' in text or 'defensive' in text or 'attack' in text:
#             return "Say: 'I need a moment to process this. Can we continue in 10 minutes?'"
#         elif 'numb' in text or 'zone out' in text or 'dissociate' in text:
#             return "Use the 5-4-3-2-1 grounding technique (engage all senses)"
#         elif 'busy' in text or 'work' in text or 'productive' in text:
#             return "Set timer for 10 minutes of intentional rest - no agenda"
#         elif 'please' in text or 'accommodate' in text or 'say yes' in text:
#             return "Practice: 'Let me check my capacity and get back to you'"
        
#         # Default alternative
#         return "Pause for 3 breaths, then choose a response that honors both me and others"
    
#     def _render_generic_techniques(self):
#         """Fallback generic techniques"""
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div class="action-item">
#                 <strong>The 5-4-3-2-1 grounding method:</strong><br><br>
#                 When pattern starts:<br>
#                 • Name 5 things you SEE<br>
#                 • Name 4 things you FEEL<br>
#                 • Name 3 things you HEAR<br>
#                 • Name 2 things you SMELL<br>
#                 • Name 1 thing you TASTE<br><br>
#                 <em>Returns you to present moment</em>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown("""
#             <div class="action-item">
#                 <strong>The PAUSE protocol:</strong><br><br>
#                 <strong>P</strong> - Pause what you're doing<br>
#                 <strong>A</strong> - Acknowledge the pattern<br>
#                 <strong>U</strong> - Understand it's protecting you<br>
#                 <strong>S</strong> - Select a new response<br>
#                 <strong>E</strong> - Execute with compassion<br><br>
#                 <em>Practice 2-3 times daily</em>
#             </div>
#             """, unsafe_allow_html=True)
    
#     def _render_personalized_success_tracking(self, master_analytics: Dict, responses: Dict):
#         """ENHANCED: Success metrics from user's actual visions"""
#         st.markdown("## 📊 Your personalized success metrics")
#         st.caption("Track these specific milestones from YOUR vision")
        
#         try:
#             # Extract user's visions
#             first_action = self._extract_response_text(responses, 74)  # Q74
#             future_vision = self._extract_response_text(responses, 75)  # Q75
#             impact_area = self._extract_response_text(responses, 76)  # Q76
            
#             # Success prediction from analytics
#             success_prediction = master_analytics.get('success_prediction', {})
            
#             # Week 1 milestone (from first action)
#             st.markdown("### Week 1 milestone")
#             if first_action:
#                 st.markdown(f"""
#                 <div class="success-indicator">
#                     <strong>Your immediate win:</strong><br>
#                     "{first_action[:200]}"<br><br>
#                     ✓ Track: Have you attempted this action?<br>
#                     ✓ Success = Any attempt, even imperfect
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # Month 1 goals (from future vision)
#             st.markdown("### Month 1 transformation markers")
#             if future_vision:
#                 # Extract specific markers from vision
#                 markers = self._extract_behavioral_markers(future_vision)
#                 st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
#                 st.markdown("**From your 6-month vision, watch for:**")
#                 for marker in markers[:5]:
#                     st.markdown(f"☐ {marker}")
#                 st.markdown("</div>", unsafe_allow_html=True)
            
#             # Domain-specific wins (from impact area)
#             if impact_area:
#                 st.markdown(f"### Primary impact area: {impact_area}")
#                 domain_wins = self._generate_domain_specific_wins(impact_area)
#                 st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
#                 st.markdown("**Track improvements in:**")
#                 for win in domain_wins:
#                     st.markdown(f"☐ {win}")
#                 st.markdown("</div>", unsafe_allow_html=True)
            
#             # Success probability
#             st.markdown("### Your transformation likelihood")
            
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 success_rate = success_prediction.get('overall_success_rate', 85)
#                 st.metric("Success probability", f"{success_rate}%")
            
#             with col2:
#                 timeline = success_prediction.get('timeline_estimate', '2-3 weeks')
#                 st.metric("Expected timeline", timeline)
            
#             with col3:
#                 tier = success_prediction.get('success_tier', 'High')
#                 st.metric("Confidence level", tier)
            
#             # Weekly check-in
#             st.markdown("### Weekly self-assessment")
#             st.markdown("""
#             <div class="action-item">
#                 <strong>Rate each weekly (1-10):</strong><br><br>
#                 1. Pattern awareness: How often did I catch it early? _____<br>
#                 2. New responses: How often did I choose differently? _____<br>
#                 3. Empowerment: How capable do I feel? _____<br>
#                 4. Life satisfaction: Overall quality this week? _____<br>
#                 5. Hope: Confidence in my transformation? _____<br><br>
#                 <em>Track trends, not perfection. Progress isn't linear.</em>
#             </div>
#             """, unsafe_allow_html=True)
            
#         except Exception as e:
#             st.warning("Personalized metrics will be created in session 1")
#             self._render_generic_success_metrics()
#             print(f"Personalized success tracking error: {str(e)}")
    
#     def _extract_behavioral_markers(self, future_vision: str) -> List[str]:
#         """Extract specific behavioral markers from future vision text"""
#         # Split into sentences
#         sentences = re.split(r'[.!?]+', future_vision)
        
#         markers = []
#         for sentence in sentences:
#             sentence = sentence.strip()
#             if len(sentence) > 10:  # Meaningful content
#                 # Clean up and add
#                 markers.append(sentence[:100])  # Limit length
        
#         # If none found, add generic markers
#         if len(markers) < 3:
#             markers.extend([
#                 "Reduced anxiety and increased peace",
#                 "Improved relationships and communication",
#                 "Greater confidence in decision-making"
#             ])
        
#         return markers[:5]  # Return top 5
    
#     def _generate_domain_specific_wins(self, impact_area: str) -> List[str]:
#         """Generate success metrics for specific life domain"""
#         domain = impact_area.lower()
        
#         domain_metrics = {
#             'work': [
#                 "Reduced procrastination on important tasks",
#                 "Better boundaries with colleagues/clients",
#                 "Increased focus and productivity",
#                 "More confident in meetings/presentations"
#             ],
#             'career': [
#                 "Clearer career direction and goals",
#                 "Confidence to pursue opportunities",
#                 "Better work-life balance",
#                 "Networking without anxiety"
#             ],
#             'relationship': [
#                 "Authentic communication without masks",
#                 "Comfortable setting boundaries",
#                 "Reduced defensiveness in conflicts",
#                 "Deeper emotional connections"
#             ],
#             'family': [
#                 "Reduced reactivity with family members",
#                 "Clearer boundaries maintained",
#                 "More authentic self-expression",
#                 "Reduced guilt about own choices"
#             ],
#             'health': [
#                 "Prioritizing self-care without guilt",
#                 "Reduced stress-related symptoms",
#                 "Better sleep quality",
#                 "Consistent healthy habits"
#             ],
#             'identity': [
#                 "Clearer sense of authentic self",
#                 "Reduced need for external validation",
#                 "Consistent across different contexts",
#                 "Living aligned with own values"
#             ]
#         }
        
#         # Find matching domain
#         for key, metrics in domain_metrics.items():
#             if key in domain:
#                 return metrics
        
#         # Default general wins
#         return [
#             "Increased self-awareness and pattern recognition",
#             "More conscious choices vs. automatic reactions",
#             "Greater emotional regulation",
#             "Improved overall life satisfaction"
#         ]
    
#     def _render_generic_success_metrics(self):
#         """Fallback generic success metrics"""
#         st.markdown("### Standard transformation indicators")
        
#         st.info("""
#         **Week 1-2 early wins:**
#         - Catching pattern earlier in the sequence
#         - Pausing before automatic response
#         - At least one successful intervention
#         - Increased self-awareness
        
#         **Week 3-4 transformation markers:**
#         - New responses feeling more natural
#         - Others noticing positive differences
#         - Reduced pattern frequency
#         - Increased life satisfaction
#         """)
    
#     def _render_integrated_session_roadmap(self, master_analytics: Dict):
#         """ENHANCED: Integrate digital interventions into session sequence"""
#         st.markdown("## Your transformation timeline")
#         st.caption("Session-by-session roadmap with integrated interventions")
        
#         try:
#             session_prediction = master_analytics.get('session_prediction', {})
#             digital_interplay = master_analytics.get('digital_interplay', {})
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            
#             # Check if digital interventions needed
#             has_digital = digital_interplay and digital_interplay.get('total_amplification_factor', 1.0) > 1.3
            
#             session_structure = session_prediction.get('session_structure', {})
#             detailed_planning = session_prediction.get('detailed_planning', {})
            
#             # Timeline overview
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 sessions = session_structure.get('total_sessions', '2 sessions')
#                 st.metric("Total sessions", sessions)
            
#             with col2:
#                 duration = session_structure.get('session_length', '90 minutes')
#                 st.metric("Session length", duration)
            
#             with col3:
#                 timeline = session_structure.get('timeline', '2-3 weeks')
#                 st.metric("Total timeline", timeline)
            
#             st.markdown("---")
            
#             # Session 1 - WITH digital foundation if needed
#             st.markdown("### Session 1: foundation and pattern mapping")
#             st.markdown("**Duration:** 90 minutes")
            
#             session1_plan = detailed_planning.get('session_1', '')
            
#             if has_digital:
#                 # Digital-enhanced session 1
#                 digital_priorities = digital_interplay.get('intervention_priority', [])

#                 with st.container():
#                     st.markdown("#### Digital foundation phase (30 min)")
#                     st.info(f"""
# **Why this matters:** Your patterns are amplified by digital conditioning. We address this first to create foundation for core work.

# **Priority interventions:**
# {chr(10).join([f'- {p}' for p in digital_priorities[:2]])}
#                     """)

#                     st.markdown("#### Core pattern mapping (60 min)")
#                     st.write(session1_plan)

#                     st.markdown("#### What to expect")
#                     st.markdown("""
# - Digital amplification assessment and reduction
# - Complete behavioral chain mapping
# - Subconscious pattern identification
# - Initial positive programming
# - You'll leave with clarity and immediate techniques
#                     """)
#             else:
#                 # Standard session 1
#                 with st.container():
#                     st.markdown("#### Core objectives")
#                     st.write(session1_plan)

#                     st.markdown("#### What to expect")
#                     st.markdown("""
# - Complete behavioral chain mapping
# - Subconscious pattern identification
# - Initial positive programming
# - Therapeutic alliance establishment
# - You'll leave with clarity and techniques
#                     """)
            
#             # Session 2
#             st.markdown("### Session 2: deep transformation and integration")
#             st.markdown("**Duration:** 90 minutes")
            
#             session2_plan = detailed_planning.get('session_2', '')
            
#             with st.container():
#                 st.markdown("#### Core objectives")
#                 st.write(session2_plan)

#                 st.markdown("#### What to expect")
#                 st.markdown("""
# - Deep hypnotic state for subconscious access
# - Pattern interruption at neural level
# - New response pathway installation
# - Behavioral anchoring and testing
# - You'll notice shifts within 48-72 hours
#                 """)

#                 st.markdown("#### Between sessions")
#                 st.markdown("""
# - Practice techniques from this blueprint daily
# - Track pattern occurrences and wins
# - Use intervention phrase when triggered
# - Notice shifts in automatic reactions
#                 """)
            
#             # Session 3 if needed
#             session3_plan = detailed_planning.get('session_3')
#             if session3_plan and 'unlikely' not in session3_plan.lower():
#                 st.markdown("### Session 3: integration reinforcement (if needed)")
#                 st.markdown("**Duration:** 60 minutes")
                
#                 with st.container():
#                     st.write(session3_plan)
#                     st.info("**Note:** About 15% of clients benefit from this reinforcement. Most achieve complete transformation in 2 sessions.")
            
#         except Exception as e:
#             st.warning("Detailed session planning will be provided after consultation")
#             self._render_generic_session_roadmap()
#             print(f"Session roadmap error: {str(e)}")
    
#     def _render_generic_session_roadmap(self):
#         """Fallback generic session roadmap"""
#         st.markdown("""
#         ### Standard transformation timeline
        
#         **Session 1 (90 min):** Complete pattern mapping and initial programming  
#         **Session 2 (90 min):** Deep neural rewiring and integration  
#         **Session 3 (60 min):** Optional reinforcement if needed (15% of clients)  
        
#         **Total timeline:** 2-3 weeks for complete transformation
#         """)
    
#     def _render_transformation_assets(self, master_analytics: Dict, responses: Dict):
#         """What you bring to transformation - empowerment section"""
#         st.markdown("## 💎 Your transformation assets")
#         st.caption("The strengths you already have for this journey")
        
#         try:
#             # Extract from analytics
#             quality = master_analytics.get('assessment_quality', {})
#             readiness = master_analytics.get('readiness_analysis', {})
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            
#             assets = []
            
#             # Assessment engagement
#             completion_rate = quality.get('completion_rate', 0)
#             if completion_rate >= 90:
#                 assets.append("**High commitment:** Your 90%+ assessment completion shows dedication to change")
#             elif completion_rate >= 80:
#                 assets.append("**Strong engagement:** Your thorough assessment shows readiness for transformation")
            
#             # Self-awareness
#             pattern_count = pattern_hierarchy.get('pattern_count', 0)
#             if pattern_count >= 3:
#                 assets.append("**Strong self-awareness:** You recognize multiple patterns - awareness is 60% of the work")
            
#             # Communication
#             text_responses = quality.get('text_responses', 0)
#             if text_responses >= 8:
#                 assets.append("**Excellent self-expression:** Your detailed responses show insight and reflection capacity")
            
#             # Readiness
#             readiness_stage = readiness.get('readiness_stage', '')
#             if 'Action' in readiness_stage or 'Preparation' in readiness_stage:
#                 assets.append(f"**High readiness:** You're in the {readiness_stage} stage - primed for transformation")
            
#             # Motivation
#             motivation_text = self._extract_response_text(responses, 77)
#             if motivation_text and len(motivation_text) > 20:
#                 assets.append("**Clear motivation:** You know WHY you want this change - motivation sustains action")
            
#             # Vision clarity
#             vision_text = self._extract_response_text(responses, 75)
#             if vision_text and len(vision_text) > 30:
#                 assets.append("**Vision clarity:** You can see your transformed future - this pulls you forward")
            
#             # Default assets if few identified
#             if len(assets) < 4:
#                 assets.extend([
#                     "**Courage:** You're here, seeking help - that takes strength",
#                     "**Intelligence:** You're approaching this systematically and thoughtfully",
#                     "**Neuroplasticity:** Your brain can rewire at any age"
#                 ])
            
#             # Render assets
#             st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
#             for asset in assets[:6]:
#                 st.markdown(f"✓ {asset}")
#             st.markdown("</div>", unsafe_allow_html=True)
            
#             # Empowerment message
#             st.success("""
#             **You have everything needed for transformation.**  
#             These patterns developed to protect you - they served a purpose. Now you're ready 
#             to update them consciously. Your awareness, commitment, and readiness position you 
#             for rapid, lasting change.
#             """)
            
#         except Exception as e:
#             st.info("Your transformation assets will be identified in consultation")
#             print(f"Transformation assets error: {str(e)}")

#     # Keep existing helper methods from old blueprint
#     def _render_table_of_contents(self):
#         """Table of contents"""
#         with st.expander("📋 **Table of contents**", expanded=False):
#             st.markdown("""
#             1. **Personal cover page**
#             2. **Crisis resources** (if applicable)
#             3. **Quick reference card**
#             4. **Personalized mantras** (from your words)
#             5. **Complete pattern analysis**
#             6. **Behavioral blueprint** (trigger sequence)
#             7. **Personalized techniques** (for your patterns)
#             8. **Session roadmap** (with digital integration)
#             9. **Success tracking** (your metrics)
#             10. **Transformation assets** (your strengths)
#             """)

#     def _render_cover_page(self, assessment_data: Dict):
#         """Personal cover page"""
#         contact = assessment_data.get('contact_info', {})
#         name = contact.get('full_name', 'Valued client')
        
#         master_analytics = assessment_data.get('master_analytics', {})
#         pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#         success_prediction = master_analytics.get('success_prediction', {})
        
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
        
#         st.markdown(f"""
#         # Complete transformation blueprint
        
#         **Prepared exclusively for:** {name}  
#         **Date:** {datetime.now().strftime('%B %d, %Y')}  
#         **Document ID:** BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}
        
#         ---
        
#         ### Your transformation summary
        
#         **Primary pattern:** {dominant.get('name', 'Assessment pending')}  
#         **Intensity:** {dominant.get('score', 0):.1f}/10  
#         **Success probability:** {success_prediction.get('overall_success_rate', 85)}%  
#         **Timeline:** {success_prediction.get('timeline_estimate', '2-3 weeks')}  
        
#         ---
        
#         *This personalized clinical analysis contains your unique behavioral patterns, 
#         transformation roadmap, and actionable techniques for lasting change.*
#         """)

#     def _render_quick_reference_card(self, master_analytics: Dict, responses: Dict):
#         """Quick reference card with personalization"""
#         st.markdown("## 🎯 Quick reference card")
#         st.caption("Print this section and keep it visible")
        
#         pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("### Your primary pattern")
#             if dominant:
#                 st.info(f"**{dominant.get('name', 'Unknown')}**\n\nIntensity: {dominant.get('score', 0):.1f}/10")
            
#             st.markdown("### When you notice it starting:")
#             st.success("""
#             1. **PAUSE** - Take 3 deep breaths
#             2. **NAME** - "This is my pattern"
#             3. **CHOOSE** - "I can respond differently"
#             """)
        
#         with col2:
#             st.markdown("### Your intervention phrase")
            
#             # Try to use user's language first
#             core_belief = self._extract_response_text(responses, 70)
#             if core_belief:
#                 inverted = self._invert_limiting_belief(core_belief)
#                 intervention = inverted
#             else:
#                 pattern_id = dominant.get('id')
#                 intervention = self._get_intervention_phrase(pattern_id)
            
#             st.markdown(f"""
#             <div class="mantra-box">
#                 "{intervention}"
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("### Emergency support")
#             st.markdown("""
#             - **Crisis hotline:** 1323 (24/7)
#             - **Keep this blueprint:** Review techniques daily
#             - **Track wins:** Every small victory matters
#             """)

#     def _render_pattern_constellation(self, master_analytics: Dict):
#         """Pattern constellation with radar chart"""
#         st.markdown("## Complete pattern analysis")
#         st.caption("Your unique behavioral pattern constellation")
        
#         try:
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#             pattern_scores = pattern_hierarchy.get('all_scores', {})
            
#             if not pattern_scores:
#                 st.info("Pattern analysis will be completed in session 1")
#                 return
            
#             # Radar chart
#             self._render_pattern_radar_chart(pattern_scores)
            
#             st.markdown("---")
            
#             # Pattern breakdown
#             st.markdown("### Pattern intensity breakdown")
            
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
#             for pattern_id, score in sorted_patterns:
#                 if score > 0:
#                     pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                     intensity_pct = min((score / 10) * 100, 100)
                    
#                     col1, col2 = st.columns([3, 1])
#                     with col1:
#                         st.markdown(f"**{pattern_name}**")
#                         st.progress(intensity_pct / 100)
#                     with col2:
#                         st.markdown(f"**{score:.1f}/10**")
                    
#                     st.caption(self._get_pattern_brief_description(pattern_id))
#                     st.markdown("")
            
#             # Pattern interactions
#             constellation_analysis = master_analytics.get('constellation_analysis', {})
#             active_reinforcements = constellation_analysis.get('active_reinforcements', [])
            
#             if active_reinforcements:
#                 st.markdown("### Pattern interactions")
#                 st.info("""
#                 Your patterns interact and amplify each other. Understanding these connections 
#                 is key to breaking the cycle.
#                 """)
                
#                 for reinforcement in active_reinforcements[:3]:
#                     p1_name = self.pattern_names.get(reinforcement.get('pattern_1'), 'Pattern')
#                     p2_name = self.pattern_names.get(reinforcement.get('pattern_2'), 'Pattern')
#                     amp = reinforcement.get('amplification', 1.0)
                    
#                     st.markdown(f"""
#                     <div class="insight-card">
#                         <strong>{p1_name}</strong> reinforces <strong>{p2_name}</strong> 
#                         (amplification: {amp}x)<br><br>
#                         When one pattern activates, it triggers the other, creating a reinforcing loop.
#                     </div>
#                     """, unsafe_allow_html=True)
            
#         except Exception as e:
#             st.warning("Complete pattern visualization will be available in session 1")
#             print(f"Pattern constellation error: {str(e)}")

#     def _render_pattern_radar_chart(self, pattern_scores: Dict):
#         """Render radar chart"""
#         try:
#             categories = []
#             values = []
            
#             for pattern_id in range(1, 11):  # Include pattern 10
#                 pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                 score = pattern_scores.get(pattern_id, 0)
#                 categories.append(pattern_name)
#                 values.append(score)
            
#             fig = go.Figure()
            
#             fig.add_trace(go.Scatterpolar(
#                 r=values,
#                 theta=categories,
#                 fill='toself',
#                 fillcolor='rgba(76, 161, 163, 0.3)',
#                 line=dict(color='#4CA1A3', width=2),
#                 name='Your patterns'
#             ))
            
#             fig.update_layout(
#                 polar=dict(
#                     radialaxis=dict(
#                         visible=True,
#                         range=[0, 10],
#                         tickfont=dict(size=10),
#                         gridcolor='#CBD5E1'
#                     ),
#                     angularaxis=dict(
#                         tickfont=dict(size=10)
#                     )
#                 ),
#                 showlegend=False,
#                 height=500,
#                 margin=dict(t=50, b=50, l=50, r=50),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)'
#             )
            
#             st.plotly_chart(fig, use_container_width=True)
            
#         except Exception as e:
#             st.info("Radar chart will be available after data processing")
#             print(f"Radar chart error: {str(e)}")

#     def _get_pattern_brief_description(self, pattern_id: int) -> str:
#         """Brief pattern description"""
#         descriptions = {
#             1: "Difficulty accepting and maintaining positive emotional states",
#             2: "Recurring conflicts and defensive responses in relationships",
#             3: "Default skepticism about others' intentions and motivations",
#             4: "Black-and-white thinking that limits creative solutions",
#             5: "Self-worth tied to productivity and achievement",
#             6: "Different selves in different contexts, lacking integration",
#             7: "Prioritizing others' needs while neglecting self-care",
#             8: "Life choices driven by family expectations vs personal desires",
#             9: "Boundaries and limits varying dramatically by context",
#             10: "Digital world feels more real than offline relationships"
#         }
#         return descriptions.get(pattern_id, "Pattern affects daily functioning")

#     def _render_trigger_blueprint(self, master_analytics: Dict, responses: Dict):
#         """Trigger sequence with personalization"""
#         st.markdown("## Your behavioral blueprint")
#         st.caption("This is YOUR unique sequence - memorize this pattern")
        
#         try:
#             trigger_analysis = master_analytics.get('trigger_sequence', {})
#             sequence = trigger_analysis.get('trigger_sequence', {})
#             completeness = trigger_analysis.get('sequence_completeness', 0)
            
#             st.markdown(f"**Sequence completeness:** {completeness}%")
#             st.progress(completeness / 100)
            
#             if completeness < 50:
#                 st.warning("We'll complete your trigger sequence mapping in session 1")
#                 return
            
#             st.markdown("---")
#             st.markdown("### Your automatic behavioral sequence")
            
#             sequence_steps = [
#                 ('environmental_trigger', '🎯 Trigger', 'What starts it'),
#                 ('physical_response', '💓 Physical', 'Body sensations'),
#                 ('automatic_thought', '💭 Thought', 'Mental response'),
#                 ('emotional_response', '😰 Emotion', 'Feelings activated'),
#                 ('behavioral_response', '🎬 Behavior', 'What you do'),
#                 ('immediate_consequence', '📊 Result', 'What happens next')
#             ]
            
#             for key, icon_title, description in sequence_steps:
#                 value = sequence.get(key, 'Not yet captured')
                
#                 if value != 'Not yet captured':
#                     with st.container():
#                         st.markdown(f"**{icon_title}**")
#                         st.caption(description)
#                         st.info(value)
            
#             # Intervention windows
#             intervention_windows = trigger_analysis.get('intervention_windows', [])
#             if intervention_windows:
#                 st.markdown("---")
#                 st.markdown("### 🎯 Intervention opportunities")
#                 st.success("These are the moments where you can interrupt and choose differently:")
                
#                 for window in intervention_windows:
#                     if isinstance(window, dict):
#                         st.markdown(f"✅ {window.get('point', window)}")
#                     else:
#                         st.markdown(f"✅ {window}")
            
#         except Exception as e:
#             st.warning("Complete trigger blueprint will be mapped in session 1")
#             print(f"Trigger blueprint error: {str(e)}")

#     def _get_pattern_mantra(self, pattern_id: Optional[int]) -> str:
#         """Pattern-specific mantra"""
#         if pattern_id is None or pattern_id not in range(1, 11):
#             return "I am capable of transformation and growth"
        
#         mantras = {
#             1: "I deserve happiness and it's safe for me to feel joy",
#             2: "Collaboration strengthens me more than conflict ever could",
#             3: "Discernment and openness can coexist - I am wise AND trusting",
#             4: "I embrace complexity and find creative solutions beyond either/or",
#             5: "My worth exists independent of any achievement or productivity",
#             6: "My authentic self is enough in every situation",
#             7: "Taking care of myself enables me to truly serve others",
#             8: "I honor my family AND claim my own authentic path",
#             9: "My boundaries remain consistent across all contexts and people",
#             10: "Real connection happens offline - I choose presence over performance"
#         }
#         return mantras.get(pattern_id, "I am capable of transformation and growth")

#     def _get_intervention_phrase(self, pattern_id: Optional[int]) -> str:
#         """Pattern intervention phrase"""
#         if pattern_id is None or pattern_id not in range(1, 11):
#             return "I choose a new response"
        
#         phrases = {
#             1: "This happiness is mine to keep",
#             2: "Curiosity, not combat",
#             3: "Discernment yes, cynicism no",
#             4: "Both/and, not either/or",
#             5: "I am, not I do",
#             6: "One me, all contexts",
#             7: "My needs matter too",
#             8: "My path, my choice",
#             9: "Consistent boundaries, confident self",
#             10: "Present moment, real connection"
#         }
#         return phrases.get(pattern_id, "I choose a new response")

#     def _get_pattern_specific_technique(self, pattern_id: Optional[int]) -> str:
#         """Pattern-specific technique"""
#         if pattern_id is None or pattern_id not in range(1, 11):
#             return "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it. Breathe. Choose differently."
        
#         techniques = {
#             1: "<strong>Happiness permission practice:</strong><br>When something good happens, say out loud: 'I deserve this and it's safe to enjoy it.' Repeat 3 times. Notice any resistance and breathe through it.",
#             2: "<strong>Curiosity reframe:</strong><br>When you feel defensive, say: 'I'm curious about their perspective.' Take 3 breaths. Ask: 'Tell me more about what you're thinking?'",
#             3: "<strong>Discernment check:</strong><br>When suspicion arises, ask: 'What evidence do I actually have?' Then: 'What would trust look like here?' Choose one small trust action.",
#             4: "<strong>Both/and thinking:</strong><br>When facing a decision, complete: 'Instead of choosing X OR Y, what if I could have aspects of X AND Y by...' List 3 creative options.",
#             5: "<strong>Being practice:</strong><br>Set timer for 5 minutes. Sit quietly. Every time you think 'I should be doing something', respond: 'Right now, being is enough.'",
#             6: "<strong>Authenticity anchor:</strong><br>Before entering any situation, touch your heart and say: 'Same me, every context.' Notice one authentic choice you can make.",
#             7: "<strong>Boundary affirmation:</strong><br>When asked for something, pause. Feel your body. Ask: 'Do I genuinely want to do this?' Honor the answer.",
#             8: "<strong>Path clarification:</strong><br>Daily ask: 'If no one would know, judge, or be disappointed, what would I choose?' This reveals YOUR path.",
#             9: "<strong>Consistent self practice:</strong><br>Identify your 'difficult context.' Practice saying 'no' to small requests there. Notice you remain whole and safe.",
#             10: "<strong>Digital detox micro-practice:</strong><br>Before checking phone/social media, ask: 'Am I seeking connection or avoiding feeling?' Choose real presence first."
#         }
#         return techniques.get(pattern_id, "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it. Breathe. Choose differently.")

#     def _generate_comprehensive_pdf(self, assessment_data: Dict) -> bytes:
#         """Generate PREMIUM 10-12 page clinical blueprint PDF"""
#         try:
#             from xhtml2pdf import pisa
#             from io import BytesIO
            
#             master_analytics = assessment_data.get('master_analytics', {})
#             responses = assessment_data.get('responses', {})
#             contact = assessment_data.get('contact_info', {})
#             name = contact.get('full_name', 'Valued Client')
            
#             # Extract all analytics components
#             pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
#             trigger_analysis = master_analytics.get('trigger_sequence', {})
#             digital_interplay = master_analytics.get('digital_interplay', {})
#             constellation_analysis = master_analytics.get('constellation_analysis', {})
#             session_prediction = master_analytics.get('session_prediction', {})
#             success_prediction = master_analytics.get('success_prediction', {})
#             readiness_analysis = master_analytics.get('readiness_analysis', {})
#             quality = master_analytics.get('assessment_quality', {})
            
#             dominant = pattern_hierarchy.get('dominant_pattern', {})
#             pattern_scores = pattern_hierarchy.get('all_scores', {})
#             primary_patterns = pattern_hierarchy.get('primary_patterns', [])
            
#             # Extract personalized user data
#             presenting_problem = self._extract_response_text(responses, 1)
#             automatic_thought = self._extract_response_text(responses, 37)
#             core_belief = self._extract_response_text(responses, 70)
#             first_action = self._extract_response_text(responses, 74)
#             future_vision = self._extract_response_text(responses, 75)
#             impact_area = self._extract_response_text(responses, 76)
#             motivation = self._extract_response_text(responses, 77)
            
#             # Check for crisis indicators
#             has_crisis = self._check_crisis_indicators(responses)
            
#             # Generate personalized content
#             mantras = self._generate_mantra_list(responses, pattern_hierarchy)
            
#             html_content = f"""
#             <!DOCTYPE html>
#             <html>
#             <head>
#                 <meta charset="UTF-8">
#                 <style>
#                     @page {{
#                         size: A4;
#                         margin: 2cm;
#                     }}
                    
#                     body {{
#                         font-family: Arial, sans-serif;
#                         line-height: 1.6;
#                         color: #273548;
#                         font-size: 11pt;
#                     }}
                    
#                     h1 {{
#                         color: #4CA1A3;
#                         font-size: 24pt;
#                         border-bottom: 3px solid #4CA1A3;
#                         padding-bottom: 10px;
#                         margin-top: 0;
#                         page-break-after: avoid;
#                     }}
                    
#                     h2 {{
#                         color: #4CA1A3;
#                         font-size: 18pt;
#                         margin-top: 25px;
#                         page-break-after: avoid;
#                     }}
                    
#                     h3 {{
#                         color: #273548;
#                         font-size: 14pt;
#                         margin-top: 20px;
#                         page-break-after: avoid;
#                     }}
                    
#                     h4 {{
#                         color: #4CA1A3;
#                         font-size: 12pt;
#                         margin-top: 15px;
#                     }}
                    
#                     p, li {{
#                         font-size: 11pt;
#                         color: #273548;
#                         line-height: 1.6;
#                     }}
                    
#                     .cover {{
#                         text-align: center;
#                         margin-top: 150px;
#                         page-break-after: always;
#                     }}
                    
#                     .cover h1 {{
#                         font-size: 32pt;
#                         border: none;
#                         margin-bottom: 40px;
#                     }}
                    
#                     .cover .subtitle {{
#                         font-size: 14pt;
#                         color: #556D7A;
#                         margin: 30px 0;
#                     }}
                    
#                     .metric {{
#                         background: #F3F6F8;
#                         padding: 15px;
#                         border-radius: 8px;
#                         margin: 10px 0;
#                         border-left: 4px solid #4CA1A3;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .mantra {{
#                         background: #4CA1A3;
#                         color: white;
#                         padding: 20px;
#                         border-radius: 12px;
#                         margin: 15px 0;
#                         text-align: center;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .mantra-source {{
#                         font-size: 9pt;
#                         opacity: 0.9;
#                         margin-bottom: 10px;
#                     }}
                    
#                     .mantra-text {{
#                         font-size: 13pt;
#                         font-weight: bold;
#                         line-height: 1.5;
#                     }}
                    
#                     .technique {{
#                         background: #E1F0F0;
#                         padding: 15px;
#                         border-radius: 8px;
#                         margin: 10px 0;
#                         border-left: 3px solid #22c55e;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .insight-card {{
#                         background: #ffffff;
#                         padding: 15px;
#                         border-radius: 8px;
#                         margin: 10px 0;
#                         border-left: 4px solid #4CA1A3;
#                         border: 1px solid #CBD5E1;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .crisis {{
#                         background: #fee2e2;
#                         border-left: 6px solid #ef4444;
#                         padding: 15px;
#                         margin: 15px 0;
#                         border-radius: 8px;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .crisis h3 {{
#                         color: #991b1b;
#                         margin-top: 0;
#                     }}
                    
#                     .success-indicator {{
#                         background: #dcfce7;
#                         border-left: 4px solid #22c55e;
#                         padding: 12px;
#                         margin: 8px 0;
#                         border-radius: 6px;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .session-card {{
#                         background: #ffffff;
#                         padding: 15px;
#                         border: 2px solid #4CA1A3;
#                         border-radius: 8px;
#                         margin: 15px 0;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .pattern-table {{
#                         width: 100%;
#                         border-collapse: collapse;
#                         margin: 15px 0;
#                     }}
                    
#                     .pattern-table th {{
#                         background: #4CA1A3;
#                         color: white;
#                         padding: 10px;
#                         text-align: left;
#                         font-size: 10pt;
#                     }}
                    
#                     .pattern-table td {{
#                         padding: 8px;
#                         border-bottom: 1px solid #E2E8F0;
#                         font-size: 10pt;
#                     }}
                    
#                     .pattern-table tr:nth-child(even) {{
#                         background: #F3F6F8;
#                     }}
                    
#                     .progress-bar {{
#                         width: 100%;
#                         height: 20px;
#                         background: #E2E8F0;
#                         border-radius: 10px;
#                         overflow: hidden;
#                         margin: 5px 0;
#                     }}
                    
#                     .progress-fill {{
#                         height: 100%;
#                         background: #4CA1A3;
#                     }}
                    
#                     .page-break {{
#                         page-break-before: always;
#                     }}
                    
#                     .toc {{
#                         background: #F3F6F8;
#                         padding: 20px;
#                         border-radius: 8px;
#                         margin: 20px 0;
#                     }}
                    
#                     .toc ul {{
#                         list-style: none;
#                         padding-left: 0;
#                     }}
                    
#                     .toc li {{
#                         padding: 8px 0;
#                         border-bottom: 1px solid #CBD5E1;
#                     }}
                    
#                     .highlight-box {{
#                         background: #FEF3C7;
#                         border-left: 4px solid #F59E0B;
#                         padding: 15px;
#                         margin: 15px 0;
#                         border-radius: 6px;
#                         page-break-inside: avoid;
#                     }}
                    
#                     .footer {{
#                         margin-top: 50px;
#                         padding-top: 30px;
#                         border-top: 2px solid #CBD5E1;
#                         font-size: 9pt;
#                         color: #556D7A;
#                     }}
                    
#                     ul, ol {{
#                         margin: 10px 0;
#                         padding-left: 25px;
#                     }}
                    
#                     li {{
#                         margin: 5px 0;
#                     }}
                    
#                     strong {{
#                         color: #273548;
#                     }}
                    
#                     .checkmark {{
#                         color: #22c55e;
#                         font-weight: bold;
#                     }}
#                 </style>
#             </head>
#             <body>
#             """
            
#             # ==================== PAGE 1: COVER PAGE ====================
#             html_content += f"""
#                 <div class="cover">
#                     <h1>Complete Transformation Blueprint</h1>
#                     <div class="subtitle">
#                         Personalized Clinical Analysis & Roadmap
#                     </div>
                    
#                     <div style="margin: 60px 0;">
#                         <p style="font-size: 16pt;"><strong>Prepared exclusively for:</strong></p>
#                         <p style="font-size: 18pt; color: #4CA1A3; font-weight: bold;">{name}</p>
#                     </div>
                    
#                     <div style="margin: 40px 0;">
#                         <p><strong>Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
#                         <p><strong>Document ID:</strong> BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}</p>
#                     </div>
                    
#                     <div class="metric" style="margin: 60px auto; max-width: 400px; text-align: left;">
#                         <h3 style="color: #4CA1A3; margin-top: 0;">Your Transformation Summary</h3>
#                         <p><strong>Primary pattern:</strong> {dominant.get('name', 'Assessment pending')}</p>
#                         <p><strong>Intensity:</strong> {dominant.get('score', 0):.1f}/10</p>
#                         <p><strong>Success probability:</strong> {success_prediction.get('overall_success_rate', 85)}%</p>
#                         <p><strong>Timeline:</strong> {success_prediction.get('timeline_estimate', '2-3 weeks')}</p>
#                         <p><strong>Recommended sessions:</strong> {success_prediction.get('recommended_sessions', 2)}</p>
#                     </div>
                    
#                     <div style="margin-top: 80px; font-size: 10pt; color: #556D7A; font-style: italic;">
#                         <p>This personalized clinical analysis contains your unique behavioral patterns,<br>
#                         transformation roadmap, and actionable techniques for lasting change.</p>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 2: TABLE OF CONTENTS ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Table of Contents</h1>
                    
#                     <div class="toc">
#                         <ul>
#                             <li><strong>1.</strong> Quick Reference Card</li>
#                             {"<li><strong>2.</strong> Crisis Resources & Safety Planning</li>" if has_crisis else ""}
#                             <li><strong>{3 if has_crisis else 2}.</strong> Your Personalized Mantras</li>
#                             <li><strong>{4 if has_crisis else 3}.</strong> Complete Pattern Analysis</li>
#                             <li><strong>{5 if has_crisis else 4}.</strong> Your Behavioral Blueprint</li>
#                             <li><strong>{6 if has_crisis else 5}.</strong> Personalized Intervention Techniques</li>
#                             <li><strong>{7 if has_crisis else 6}.</strong> Integrated Session Roadmap</li>
#                             <li><strong>{8 if has_crisis else 7}.</strong> Personalized Success Metrics</li>
#                             <li><strong>{9 if has_crisis else 8}.</strong> Your Transformation Assets</li>
#                             <li><strong>{10 if has_crisis else 9}.</strong> Next Steps & Resources</li>
#                         </ul>
#                     </div>
                    
#                     <div class="highlight-box" style="margin-top: 40px;">
#                         <h3 style="margin-top: 0; color: #92400E;">How to Use This Blueprint</h3>
#                         <ol>
#                             <li><strong>Read the Quick Reference Card daily</strong> - Keep it visible</li>
#                             <li><strong>Practice your personalized mantras</strong> - Say them out loud</li>
#                             <li><strong>Study your behavioral blueprint</strong> - Memorize your sequence</li>
#                             <li><strong>Use the techniques immediately</strong> - Start before session 1</li>
#                             <li><strong>Track your progress</strong> - Use the success metrics weekly</li>
#                             <li><strong>Review before sessions</strong> - Come prepared with examples</li>
#                         </ol>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 3: QUICK REFERENCE CARD ====================
#             intervention_phrase = self._invert_limiting_belief(core_belief) if core_belief else self._get_intervention_phrase(dominant.get('id'))
            
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Quick Reference Card</h1>
#                     <p style="color: #556D7A;"><em>Print this page and keep it visible - refer to it daily</em></p>
                    
#                     <div class="metric">
#                         <h2 style="margin-top: 0;">Your Primary Pattern</h2>
#                         <p style="font-size: 16pt; color: #4CA1A3; font-weight: bold;">{dominant.get('name', 'Unknown')}</p>
#                         <p><strong>Intensity:</strong> {dominant.get('score', 0):.1f}/10</p>
#                         <p style="color: #556D7A; margin-top: 10px;">{self._get_pattern_brief_description(dominant.get('id'))}</p>
#                     </div>
                    
#                     <div class="technique">
#                         <h3 style="margin-top: 0; color: #273548;">When You Notice Your Pattern Starting:</h3>
#                         <ol style="font-size: 12pt; line-height: 1.8;">
#                             <li><strong style="color: #4CA1A3;">PAUSE</strong> - Stop what you're doing, take 3 deep breaths</li>
#                             <li><strong style="color: #4CA1A3;">NAME</strong> - Say: "This is my {dominant.get('name', 'pattern')} pattern"</li>
#                             <li><strong style="color: #4CA1A3;">CHOOSE</strong> - Say: "I can respond differently"</li>
#                             <li><strong style="color: #4CA1A3;">ACT</strong> - Use one of your personalized techniques</li>
#                         </ol>
#                     </div>
                    
#                     <div class="mantra">
#                         <div class="mantra-source">Your Daily Intervention Phrase</div>
#                         <div class="mantra-text">"{intervention_phrase}"</div>
#                         <p style="font-size: 10pt; margin-top: 15px; opacity: 0.9;">
#                             Say this OUT LOUD every morning and whenever you notice your pattern activating
#                         </p>
#                     </div>
                    
#                     <div class="metric">
#                         <h3 style="margin-top: 0; color: #4CA1A3;">Emergency Support Resources</h3>
#                         <p><strong>Thailand Crisis Hotline:</strong> 1323 (24/7)</p>
#                         <p><strong>Samaritans of Thailand:</strong> 02-713-6793</p>
#                         <p><strong>Emergency Services:</strong> 1669</p>
#                         <p><strong>International Crisis Line:</strong> befrienders.org</p>
#                         <p style="margin-top: 15px; color: #556D7A;">
#                             <strong>Note:</strong> Keep this blueprint accessible. Review your techniques daily. 
#                             Progress takes practice - be patient and compassionate with yourself.
#                         </p>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 4: CRISIS RESOURCES (if applicable) ====================
#             if has_crisis:
#                 html_content += f"""
#                     <div class="page-break">
#                         <h1>Crisis Resources & Safety Planning</h1>
                        
#                         <div class="crisis">
#                             <h3>If You Are in Immediate Danger or Crisis</h3>
#                             <p style="font-weight: bold; font-size: 12pt; margin-bottom: 15px;">
#                                 Please reach out for immediate help. You are not alone, and support is available 24/7.
#                             </p>
                            
#                             <h4 style="color: #991b1b;">24/7 Crisis Hotlines:</h4>
#                             <ul style="font-weight: 500;">
#                                 <li><strong>Thailand Suicide Hotline:</strong> 1323</li>
#                                 <li><strong>Samaritans of Thailand:</strong> 02-713-6793</li>
#                                 <li><strong>International Crisis Line:</strong> befrienders.org</li>
#                                 <li><strong>Emergency Services:</strong> 1669</li>
#                             </ul>
                            
#                             <p style="margin-top: 15px; font-weight: 500;">
#                                 <strong>Important:</strong> Your therapist will prioritize contact within 2 hours. 
#                                 Please check your email and phone immediately.
#                             </p>
#                         </div>
                        
#                         <div class="technique">
#                             <h3 style="margin-top: 0;">Your Personal Safety Plan</h3>
#                             <p><em>Complete this now and keep it accessible:</em></p>
                            
#                             <h4>1. Warning Signs I Can Notice:</h4>
#                             <p style="margin-left: 20px; color: #556D7A;">
#                                 • Physical: ________________________________<br>
#                                 • Emotional: ________________________________<br>
#                                 • Behavioral: ________________________________
#                             </p>
                            
#                             <h4>2. People I Can Contact:</h4>
#                             <p style="margin-left: 20px; color: #556D7A;">
#                                 • Friend/Family: ________________________________<br>
#                                 • Crisis Hotline: 1323 (always available)<br>
#                                 • Therapist: (will be provided after consultation)
#                             </p>
                            
#                             <h4>3. Safe Places I Can Go:</h4>
#                             <p style="margin-left: 20px; color: #556D7A;">
#                                 • ________________________________<br>
#                                 • ________________________________
#                             </p>
                            
#                             <h4>4. Things That Help Me Feel Better:</h4>
#                             <p style="margin-left: 20px; color: #556D7A;">
#                                 • ________________________________<br>
#                                 • ________________________________<br>
#                                 • ________________________________
#                             </p>
                            
#                             <h4>5. My Reasons for Living:</h4>
#                             <p style="margin-left: 20px; color: #556D7A;">
#                                 • ________________________________<br>
#                                 • ________________________________<br>
#                                 • ________________________________
#                             </p>
#                         </div>
                        
#                         <div class="highlight-box">
#                             <p style="margin: 0; font-weight: bold;">
#                                 Keep this safety plan visible. Share it with someone you trust. 
#                                 Your life matters, and help is always available.
#                             </p>
#                         </div>
#                     </div>
#                 """
            
#             # ==================== PAGE 5: PERSONALIZED MANTRAS ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Personalized Transformation Mantras</h1>
#                     <p style="color: #556D7A;"><em>Generated from YOUR words - read these daily, say them out loud</em></p>
                    
#                     <div class="highlight-box">
#                         <p style="margin: 0;"><strong>Why mantras work:</strong> Repetition creates new neural pathways. 
#                         These phrases counter your old automatic thoughts with empowering truths. Say them even when 
#                         you don't fully believe them yet - belief follows action.</p>
#                     </div>
#             """
            
#             if mantras:
#                 for i, (source, mantra) in enumerate(mantras, 1):
#                     html_content += f"""
#                     <div class="mantra">
#                         <div class="mantra-source">Mantra {i}: {source}</div>
#                         <div class="mantra-text">"{mantra}"</div>
#                     </div>
#                     """
#             else:
#                 # Fallback pattern-based mantras
#                 pattern_mantra = self._get_pattern_mantra(dominant.get('id'))
#                 html_content += f"""
#                     <div class="mantra">
#                         <div class="mantra-source">Your Primary Pattern Mantra</div>
#                         <div class="mantra-text">"{pattern_mantra}"</div>
#                     </div>
#                 """
            
#             html_content += """
#                     <div class="technique">
#                         <h3 style="margin-top: 0;">How to Use Your Mantras</h3>
#                         <ul>
#                             <li><strong>Morning practice:</strong> Say all mantras out loud before starting your day</li>
#                             <li><strong>When triggered:</strong> Use your intervention phrase immediately</li>
#                             <li><strong>Throughout the day:</strong> Repeat silently whenever old thoughts arise</li>
#                             <li><strong>Before sleep:</strong> Review mantras to program your subconscious overnight</li>
#                         </ul>
#                         <p style="margin-top: 15px; font-style: italic; color: #556D7A;">
#                             Tip: Record yourself saying these mantras and listen during commute or exercise
#                         </p>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 6-7: COMPLETE PATTERN ANALYSIS ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Complete Pattern Analysis</h1>
#                     <p style="color: #556D7A;"><em>Your unique behavioral pattern constellation</em></p>
                    
#                     <div class="metric">
#                         <h2 style="margin-top: 0;">Assessment Overview</h2>
#                         <p><strong>Total patterns identified:</strong> {pattern_hierarchy.get('pattern_count', 0)}</p>
#                         <p><strong>Completion rate:</strong> {quality.get('completion_rate', 0):.0f}%</p>
#                         <p><strong>Assessment quality:</strong> {quality.get('quality_tier', 'Good')}</p>
#                         <p><strong>Complexity level:</strong> {pattern_hierarchy.get('complexity_assessment', 'Standard')}</p>
#                     </div>
                    
#                     <h2>Pattern Intensity Breakdown</h2>
#                     <p style="color: #556D7A; margin-bottom: 20px;">
#                         Your patterns are scored 0-10 based on frequency, intensity, and impact. 
#                         Scores ≥6.0 indicate clinical concern requiring intervention.
#                     </p>
                    
#                     <table class="pattern-table">
#                         <thead>
#                             <tr>
#                                 <th>Pattern</th>
#                                 <th>Score</th>
#                                 <th>Intensity</th>
#                                 <th>Status</th>
#                             </tr>
#                         </thead>
#                         <tbody>
#             """
            
#             # Sort patterns by score
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
#             for pattern_id, score in sorted_patterns:
#                 pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                 intensity_pct = min((score / 10) * 100, 100)
                
#                 if score >= 8.0:
#                     status = "Severe - Primary target"
#                     status_color = "#ef4444"
#                 elif score >= 6.0:
#                     status = "Significant - Address"
#                     status_color = "#F59E0B"
#                 elif score >= 4.0:
#                     status = "Moderate - Monitor"
#                     status_color = "#eab308"
#                 else:
#                     status = "Adaptive - Stable"
#                     status_color = "#22c55e"
                
#                 html_content += f"""
#                             <tr>
#                                 <td><strong>{pattern_name}</strong></td>
#                                 <td>{score:.1f}/10</td>
#                                 <td>
#                                     <div class="progress-bar" style="width: 100px;">
#                                         <div class="progress-fill" style="width: {intensity_pct}%;"></div>
#                                     </div>
#                                 </td>
#                                 <td style="color: {status_color}; font-weight: bold;">{status}</td>
#                             </tr>
#                 """
            
#             html_content += """
#                         </tbody>
#                     </table>
#             """
            
#             # Dominant pattern detail
#             if dominant:
#                 pattern_desc = dominant.get('description', {})
#                 html_content += f"""
#                     <div class="page-break">
#                         <h2>Your Dominant Pattern: {dominant.get('name', 'Unknown')}</h2>
                        
#                         <div class="insight-card">
#                             <p><strong>Intensity:</strong> {dominant.get('score', 0):.1f}/10 - {dominant.get('severity', 'Significant')}</p>
#                             <p><strong>Core belief:</strong> {pattern_desc.get('core_belief', 'Pattern protecting you from perceived threat')}</p>
#                             <p><strong>Impact:</strong> {pattern_desc.get('impact', 'This pattern affects your daily functioning and relationships')}</p>
#                             <p><strong>Transformation focus:</strong> {pattern_desc.get('transformation', 'Learning new responses and beliefs')}</p>
#                         </div>
                        
#                         <div class="technique">
#                             <h3 style="margin-top: 0;">What You Notice Internally</h3>
#                             <p>{pattern_desc.get('what_you_notice', 'You experience this pattern through automatic thoughts, physical sensations, and emotional reactions')}</p>
                            
#                             <h3>What Others See Externally</h3>
#                             <p>{pattern_desc.get('what_others_see', 'Others may notice behaviors or responses that stem from this pattern')}</p>
                            
#                             <h3>Hidden Cost</h3>
#                             <p style="color: #ef4444;">{pattern_desc.get('hidden_cost', 'This pattern consumes mental energy and limits possibilities')}</p>
                            
#                             <h3>Breakthrough Potential</h3>
#                             <p style="color: #22c55e;">{pattern_desc.get('breakthrough_moment', 'Understanding this pattern is the first step to transforming it')}</p>
#                         </div>
#                 """
                
#                 # Primary patterns
#                 if primary_patterns:
#                     html_content += """
#                         <h2>Primary Supporting Patterns</h2>
#                         <p style="color: #556D7A;">These patterns interact with and reinforce your dominant pattern:</p>
#                     """
                    
#                     for pattern in primary_patterns[:2]:
#                         p_name = pattern.get('name', 'Pattern')
#                         p_score = pattern.get('score', 0)
#                         html_content += f"""
#                         <div class="metric">
#                             <h3 style="margin-top: 0; color: #4CA1A3;">{p_name}</h3>
#                             <p><strong>Intensity:</strong> {p_score:.1f}/10</p>
#                             <p style="color: #556D7A;">{self._get_pattern_brief_description(pattern.get('id'))}</p>
#                         </div>
#                         """
                
#                 # Pattern interactions
#                 active_reinforcements = constellation_analysis.get('active_reinforcements', [])
#                 if active_reinforcements:
#                     html_content += """
#                         <h2>Pattern Interactions</h2>
#                         <p style="color: #556D7A;">Your patterns don't operate in isolation - they interact and amplify each other:</p>
#                     """
                    
#                     for reinforcement in active_reinforcements[:3]:
#                         p1_id = reinforcement.get('pattern_1')
#                         p2_id = reinforcement.get('pattern_2')
#                         p1_name = self.pattern_names.get(p1_id, 'Pattern')
#                         p2_name = self.pattern_names.get(p2_id, 'Pattern')
#                         amp = reinforcement.get('amplification', 1.0)
                        
#                         html_content += f"""
#                         <div class="insight-card">
#                             <p><strong>{p1_name}</strong> reinforces <strong>{p2_name}</strong> 
#                             (amplification factor: {amp}x)</p>
#                             <p style="color: #556D7A; margin-top: 10px;">
#                                 {self._describe_pattern_interaction(p1_id, p2_id)}
#                             </p>
#                         </div>
#                         """
            
#             html_content += """
#                     </div>
#             """
            
#             # ==================== PAGE 8: BEHAVIORAL BLUEPRINT ====================
#             sequence = trigger_analysis.get('trigger_sequence', {})
#             intervention_windows = trigger_analysis.get('intervention_windows', [])
            
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Behavioral Blueprint</h1>
#                     <p style="color: #556D7A;"><em>This is YOUR unique automatic sequence - memorize this pattern</em></p>
                    
#                     <div class="highlight-box">
#                         <p style="margin: 0;"><strong>Why this matters:</strong> Understanding your exact behavioral 
#                         sequence allows you to interrupt it at specific points. The earlier you catch it, the easier 
#                         it is to choose differently.</p>
#                     </div>
                    
#                     <h2>Your Complete Behavioral Chain</h2>
#             """
            
#             sequence_steps = [
#                 ('environmental_trigger', '🎯 Environmental Trigger', 'What starts the sequence'),
#                 ('awareness_entry_point', '👁️ First Awareness', 'What you notice first'),
#                 ('physical_response', '💓 Physical Response', 'Body sensations'),
#                 ('automatic_thought', '💭 Automatic Thought', 'Mental response'),
#                 ('emotional_response', '😰 Emotional Response', 'Feelings activated'),
#                 ('behavioral_response', '🎬 Behavioral Response', 'What you do'),
#                 ('immediate_consequence', '📊 Immediate Result', 'What happens next'),
#                 ('extended_impact', '🔄 Extended Impact', 'Hours later effect')
#             ]
            
#             for key, icon_title, description in sequence_steps:
#                 value = sequence.get(key, 'Not yet captured')
                
#                 if value and value != 'Not yet captured':
#                     html_content += f"""
#                     <div class="insight-card">
#                         <h3 style="margin-top: 0; color: #4CA1A3;">{icon_title}</h3>
#                         <p style="color: #556D7A; font-size: 10pt; margin-bottom: 8px;"><em>{description}</em></p>
#                         <p style="font-weight: 500; color: #273548;">{value}</p>
#                     </div>
#                     """
            
#             if intervention_windows:
#                 html_content += """
#                     <h2>Your Intervention Opportunities</h2>
#                     <p style="color: #556D7A;">These are the critical moments where you can interrupt your automatic pattern:</p>
#                 """
                
#                 for i, window in enumerate(intervention_windows, 1):
#                     if isinstance(window, dict):
#                         point = window.get('point', 'Intervention point')
#                         description = window.get('description', '')
#                         technique = window.get('technique', '')
                        
#                         html_content += f"""
#                         <div class="success-indicator">
#                             <h4 style="margin-top: 0; color: #22c55e;">Window {i}: {point}</h4>
#                             <p style="margin: 5px 0;"><strong>What to do:</strong> {description}</p>
#                             <p style="margin: 5px 0;"><strong>Technique:</strong> {technique}</p>
#                         </div>
#                         """
#                     else:
#                         html_content += f"""
#                         <div class="success-indicator">
#                             <p style="margin: 0;"><strong class="checkmark">✓</strong> {window}</p>
#                         </div>
#                         """
            
#             html_content += """
#                 </div>
#             """
            
#             # ==================== PAGE 9: PERSONALIZED TECHNIQUES ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Personalized Intervention Techniques</h1>
#                     <p style="color: #556D7A;"><em>Start using these TODAY - before your first session</em></p>
                    
#                     <div class="highlight-box">
#                         <p style="margin: 0;"><strong>Implementation strategy:</strong> Pick ONE technique to practice 
#                         daily for a week. Master it before adding another. Quality over quantity.</p>
#                     </div>
#             """
            
#             # Technique 1: Somatic intervention
#             physical_response = sequence.get('physical_response', 'physical tension')
#             html_content += f"""
#                     <h2>Technique 1: Somatic Intervention</h2>
#                     <div class="technique">
#                         <h3 style="margin-top: 0;">When You Notice: "{physical_response}"</h3>
                        
#                         <h4>Immediate 5-Step Response:</h4>
#                         <ol>
#                             <li><strong>STOP</strong> - Freeze your body exactly as it is</li>
#                             <li><strong>BREATHE</strong> - 4 counts in through nose, 6 counts out through mouth (3 times)</li>
#                             <li><strong>SCAN</strong> - Notice the sensation without judgment: "I notice tension in my chest"</li>
#                             <li><strong>RELEASE</strong> - Consciously relax that area, imagine breathing into it</li>
#                             <li><strong>GROUND</strong> - Feel your feet on the floor, notice 3 things you can see</li>
#                         </ol>
                        
#                         <p style="margin-top: 15px; font-style: italic; color: #556D7A;">
#                             <strong>Why this works:</strong> This interrupts the automatic chain BEFORE thoughts cascade 
#                             into emotions and behaviors. Physical awareness is your earliest intervention point.
#                         </p>
#                     </div>
#             """
            
#             # Technique 2: Cognitive reframe
#             if automatic_thought:
#                 reframed = self._reframe_automatic_thought(automatic_thought)
#                 html_content += f"""
#                     <h2>Technique 2: Cognitive Reframe</h2>
#                     <div class="technique">
#                         <h3 style="margin-top: 0;">Your Automatic Thought:</h3>
#                         <p style="background: #fee2e2; padding: 10px; border-radius: 6px; color: #991b1b;">
#                             "{automatic_thought[:200]}{'...' if len(automatic_thought) > 200 else ''}"
#                         </p>
                        
#                         <h3>Your New Empowering Response:</h3>
#                         <p style="background: #dcfce7; padding: 10px; border-radius: 6px; color: #166534; font-weight: bold;">
#                             "{reframed}"
#                         </p>
                        
#                         <h4>Practice Protocol:</h4>
#                         <ul>
#                             <li>Say your new response OUT LOUD 3 times every morning</li>
#                             <li>When old thought appears, immediately counter with new response</li>
#                             <li>Write it on sticky notes and place around your environment</li>
#                             <li>Record yourself saying it and listen during commute</li>
#                         </ul>
                        
#                         <p style="margin-top: 15px; font-style: italic; color: #556D7A;">
#                             <strong>Why this works:</strong> Repetition builds new neural pathways. After 3-4 weeks of 
#                             consistent practice, the new thought will become automatic.
#                         </p>
#                     </div>
#                 """
            
#             # Technique 3: Behavioral substitution
#             behavioral_response = sequence.get('behavioral_response', '')
#             if behavioral_response:
#                 alternative = self._generate_alternative_behavior(behavioral_response)
#                 html_content += f"""
#                     <h2>Technique 3: Behavioral Substitution</h2>
#                     <div class="technique">
#                         <h3 style="margin-top: 0;">Old Automatic Behavior:</h3>
#                         <p style="background: #fee2e2; padding: 10px; border-radius: 6px; color: #991b1b;">
#                             "{behavioral_response}"
#                         </p>
                        
#                         <h3>Your New Alternative Response:</h3>
#                         <p style="background: #dcfce7; padding: 10px; border-radius: 6px; color: #166534; font-weight: bold;">
#                             "{alternative}"
#                         </p>
                        
#                         <h4>Implementation Steps:</h4>
#                         <ol>
#                             <li><strong>Prepare in advance:</strong> Visualize yourself doing the new behavior successfully</li>
#                             <li><strong>Start small:</strong> Practice in low-stakes situations first</li>
#                             <li><strong>Use your trigger:</strong> When old urge arises, do the new behavior immediately</li>
#                             <li><strong>Track wins:</strong> Every time you choose the new behavior, note it</li>
#                         </ol>
                        
#                         <p style="margin-top: 15px; font-style: italic; color: #556D7A;">
#                             <strong>Remember:</strong> New behaviors feel awkward at first. That's normal. 
#                             The discomfort means you're creating new neural pathways.
#                         </p>
#                     </div>
#                 """
            
#             # Technique 4: Pattern-specific mastery
#             pattern_technique = self._get_pattern_specific_technique(dominant.get('id'))
#             html_content += f"""
#                     <h2>Technique 4: Pattern-Specific Mastery</h2>
#                     <div class="technique">
#                         {pattern_technique.replace('<br>', '<br/>')}
#                     </div>
                    
#                     <div class="highlight-box">
#                         <h3 style="margin-top: 0;">Quick Reference: The PAUSE Protocol</h3>
#                         <p style="margin-bottom: 10px;">Use this ANY time, with ANY technique:</p>
#                         <ul style="margin: 0;">
#                             <li><strong>P</strong> - Pause what you're doing</li>
#                             <li><strong>A</strong> - Acknowledge the pattern: "There's my pattern"</li>
#                             <li><strong>U</strong> - Understand it's protecting you: "This served me once"</li>
#                             <li><strong>S</strong> - Select a new response from your techniques</li>
#                             <li><strong>E</strong> - Execute with self-compassion, celebrate any attempt</li>
#                         </ul>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 10: INTEGRATED SESSION ROADMAP ====================
#             has_digital = digital_interplay and digital_interplay.get('total_amplification_factor', 1.0) > 1.3
#             session_structure = session_prediction.get('session_structure', {})
#             detailed_planning = session_prediction.get('detailed_planning', {})
            
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Transformation Timeline</h1>
#                     <p style="color: #556D7A;"><em>Session-by-session roadmap with integrated interventions</em></p>
                    
#                     <div class="metric">
#                         <h2 style="margin-top: 0;">Timeline Overview</h2>
#                         <p><strong>Total sessions:</strong> {session_structure.get('total_sessions', '2 sessions')}</p>
#                         <p><strong>Session length:</strong> {session_structure.get('session_length', '90 minutes each')}</p>
#                         <p><strong>Total timeline:</strong> {session_structure.get('timeline', '2-3 weeks')}</p>
#                         <p><strong>Success probability:</strong> {success_prediction.get('overall_success_rate', 85)}%</p>
#                     </div>
#             """
            
#             # Session 1
#             session1_plan = detailed_planning.get('session_1', 'Complete pattern mapping and initial programming')
            
#             if has_digital:
#                 digital_priorities = digital_interplay.get('intervention_priority', [])
#                 html_content += f"""
#                     <h2>Session 1: Foundation & Pattern Mapping (90 minutes)</h2>
                    
#                     <div class="session-card">
#                         <h3 style="color: #4CA1A3; margin-top: 0;">Phase 1: Digital Foundation (30 min)</h3>
#                         <p style="color: #556D7A; margin-bottom: 10px;">
#                             <strong>Why this matters:</strong> Your patterns are amplified by digital conditioning. 
#                             We address this first to create foundation for core work.
#                         </p>
#                         <ul>
#                 """
#                 for priority in digital_priorities[:2]:
#                     html_content += f"<li>{priority}</li>"
                
#                 html_content += f"""
#                         </ul>
                        
#                         <h3 style="color: #4CA1A3; margin-top: 20px;">Phase 2: Core Pattern Mapping (60 min)</h3>
#                         <p>{session1_plan}</p>
                        
#                         <h4>What to Expect:</h4>
#                         <ul>
#                             <li>Digital amplification assessment and reduction protocols</li>
#                             <li>Complete behavioral chain mapping (your specific sequence)</li>
#                             <li>Subconscious pattern identification and origin exploration</li>
#                             <li>Initial positive programming and response preparation</li>
#                             <li>You'll leave with clarity, techniques, and immediate action steps</li>
#                         </ul>
                        
#                         <h4>How to Prepare:</h4>
#                         <ul>
#                             <li>Review this blueprint thoroughly before session</li>
#                             <li>Track pattern occurrences this week - bring specific examples</li>
#                             <li>Practice your personalized techniques daily</li>
#                             <li>Come with questions and openness to explore origins</li>
#                         </ul>
#                     </div>
#                 """
#             else:
#                 html_content += f"""
#                     <h2>Session 1: Pattern Mapping & Rapport Building (90 minutes)</h2>
                    
#                     <div class="session-card">
#                         <h3 style="color: #4CA1A3; margin-top: 0;">Core Objectives</h3>
#                         <p>{session1_plan}</p>
                        
#                         <h4>What to Expect:</h4>
#                         <ul>
#                             <li>Complete behavioral chain mapping (your specific sequence)</li>
#                             <li>Subconscious pattern identification and origin exploration</li>
#                             <li>Initial positive programming and response preparation</li>
#                             <li>Therapeutic alliance establishment in safe, collaborative space</li>
#                             <li>You'll leave with clarity about your patterns and techniques to use</li>
#                         </ul>
                        
#                         <h4>How to Prepare:</h4>
#                         <ul>
#                             <li>Review this blueprint thoroughly before session</li>
#                             <li>Track pattern occurrences - bring specific recent examples</li>
#                             <li>Practice your personalized techniques daily</li>
#                             <li>Come ready to explore origins openly and compassionately</li>
#                         </ul>
#                     </div>
#                 """
            
#             # Session 2
#             session2_plan = detailed_planning.get('session_2', 'Deep neural rewiring and integration')
#             html_content += f"""
#                     <h2>Session 2: Deep Transformation & Integration (90 minutes)</h2>
                    
#                     <div class="session-card">
#                         <h3 style="color: #4CA1A3; margin-top: 0;">Core Objectives</h3>
#                         <p>{session2_plan}</p>
                        
#                         <h4>What to Expect:</h4>
#                         <ul>
#                             <li>Deep hypnotic state for direct subconscious access (you remain aware)</li>
#                             <li>Pattern interruption at neural level - rewiring automatic responses</li>
#                             <li>New response pathway installation with behavioral anchoring</li>
#                             <li>Testing and integration of new patterns in imagined scenarios</li>
#                             <li>You'll notice measurable shifts within 48-72 hours</li>
#                         </ul>
                        
#                         <h4>Between Sessions (Critical):</h4>
#                         <ul>
#                             <li>Practice ALL techniques from this blueprint daily</li>
#                             <li>Track pattern occurrences and your new responses</li>
#                             <li>Use your intervention phrase whenever triggered</li>
#                             <li>Notice any shifts in automatic reactions - celebrate small wins</li>
#                             <li>Review your mantras morning and evening</li>
#                         </ul>
#                     </div>
#             """
            
#             # Session 3 if needed
#             session3_plan = detailed_planning.get('session_3', '')
#             if session3_plan and 'unlikely' not in session3_plan.lower():
#                 html_content += f"""
#                     <h2>Session 3: Integration & Reinforcement (60 minutes)</h2>
#                     <p style="color: #556D7A;"><em>Only if needed (approximately 15% of clients)</em></p>
                    
#                     <div class="session-card">
#                         <p>{session3_plan}</p>
                        
#                         <p style="margin-top: 15px; color: #556D7A;">
#                             <strong>Note:</strong> Most clients achieve complete transformation in 2 sessions. 
#                             This optional reinforcement session is available for complex pattern integration 
#                             or to address unexpected challenges during implementation.
#                         </p>
#                     </div>
#                 """
            
#             html_content += """
#                 </div>
#             """
            
#             # ==================== PAGE 11: PERSONALIZED SUCCESS METRICS ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Personalized Success Metrics</h1>
#                     <p style="color: #556D7A;"><em>Track these specific milestones from YOUR vision</em></p>
                    
#                     <div class="highlight-box">
#                         <p style="margin: 0;"><strong>How to use this section:</strong> Review these metrics weekly. 
#                         Track progress, not perfection. Transformation is rarely linear - celebrate every win, 
#                         learn from every setback.</p>
#                     </div>
#             """
            
#             # Week 1 milestone
#             if first_action:
#                 html_content += f"""
#                     <h2>Week 1 Immediate Milestone</h2>
#                     <div class="success-indicator">
#                         <h3 style="margin-top: 0; color: #166534;">Your First Win (from your vision):</h3>
#                         <p style="font-weight: 500;">"{first_action[:250]}{'...' if len(first_action) > 250 else ''}"</p>
                        
#                         <p style="margin-top: 15px;"><strong>Success criteria:</strong></p>
#                         <ul>
#                             <li><strong class="checkmark">✓</strong> Any attempt counts as success (perfection not required)</li>
#                             <li><strong class="checkmark">✓</strong> Notice if you even THOUGHT about trying</li>
#                             <li><strong class="checkmark">✓</strong> Celebrate awareness even without action</li>
#                         </ul>
#                     </div>
#                 """
            
#             # Month 1 transformation markers
#             if future_vision:
#                 markers = self._extract_behavioral_markers(future_vision)
#                 html_content += f"""
#                     <h2>Month 1 Transformation Markers</h2>
#                     <p style="color: #556D7A;">From your 6-month vision, watch for these changes:</p>
                    
#                     <div class="technique">
#                 """
#                 for i, marker in enumerate(markers[:5], 1):
#                     html_content += f"""
#                         <p style="margin: 8px 0;">
#                             <strong>{i}.</strong> {marker}
#                         </p>
#                     """
#                 html_content += """
#                     </div>
#                 """
            
#             # Domain-specific wins
#             if impact_area:
#                 domain_wins = self._generate_domain_specific_wins(impact_area)
#                 html_content += f"""
#                     <h2>Primary Impact Area: {impact_area.title()}</h2>
#                     <p style="color: #556D7A;">Track improvements in this life domain specifically:</p>
                    
#                     <div class="technique">
#                 """
#                 for i, win in enumerate(domain_wins, 1):
#                     html_content += f"""
#                         <p style="margin: 8px 0;">
#                             <strong class="checkmark">✓</strong> {win}
#                         </p>
#                     """
#                 html_content += """
#                     </div>
#                 """
            
#             # Success probability breakdown
#             html_content += f"""
#                     <h2>Your Success Probability Analysis</h2>
                    
#                     <div class="metric">
#                         <h3 style="margin-top: 0; color: #4CA1A3;">Overall Success Rate: {success_prediction.get('overall_success_rate', 85)}%</h3>
                        
#                         <div class="progress-bar" style="height: 30px; margin: 15px 0;">
#                             <div class="progress-fill" style="width: {success_prediction.get('overall_success_rate', 85)}%;"></div>
#                         </div>
                        
#                         <p><strong>Confidence level:</strong> {success_prediction.get('confidence_level', 'High')}</p>
#                         <p><strong>Success tier:</strong> {success_prediction.get('success_tier', 'High')}</p>
#                         <p><strong>Timeline estimate:</strong> {success_prediction.get('timeline_estimate', '2-3 weeks')}</p>
#                     </div>
#             """
            
#             # Weekly self-assessment
#             html_content += """
#                     <h2>Weekly Self-Assessment Protocol</h2>
#                     <p style="color: #556D7A;">Complete this every Sunday evening:</p>
                    
#                     <div class="technique">
#                         <h4>Rate each area (1-10):</h4>
#                         <ol style="line-height: 2;">
#                             <li>Pattern awareness: How often did I catch it early? _____</li>
#                             <li>New responses: How often did I choose differently? _____</li>
#                             <li>Technique usage: How consistently did I practice? _____</li>
#                             <li>Empowerment: How capable do I feel? _____</li>
#                             <li>Life satisfaction: Overall quality this week? _____</li>
#                         </ol>
                        
#                         <p style="margin-top: 20px;"><strong>Weekly reflection prompts:</strong></p>
#                         <ul>
#                             <li>Biggest win this week: ________________________________</li>
#                             <li>Most challenging moment: ________________________________</li>
#                             <li>Key learning: ________________________________</li>
#                             <li>Next week's focus: ________________________________</li>
#                         </ul>
                        
#                         <p style="margin-top: 20px; font-style: italic; color: #556D7A;">
#                             <strong>Remember:</strong> Progress isn't linear. Some weeks will feel like huge leaps, 
#                             others like setbacks. Track the trend over time, not daily fluctuations.
#                         </p>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 12: TRANSFORMATION ASSETS ====================
#             # Extract transformation assets
#             assets = []
            
#             completion_rate = quality.get('completion_rate', 0)
#             if completion_rate >= 90:
#                 assets.append("High commitment: Your 90%+ assessment completion shows dedication to change")
#             elif completion_rate >= 80:
#                 assets.append("Strong engagement: Your thorough assessment shows readiness for transformation")
            
#             pattern_count = pattern_hierarchy.get('pattern_count', 0)
#             if pattern_count >= 3:
#                 assets.append("Strong self-awareness: You recognize multiple patterns - awareness is 60% of the work")
            
#             text_responses = quality.get('text_responses', 0)
#             if text_responses >= 8:
#                 assets.append("Excellent self-expression: Your detailed responses show insight and reflection capacity")
            
#             readiness_stage = readiness_analysis.get('readiness_stage', '')
#             if 'Action' in readiness_stage or 'Preparation' in readiness_stage:
#                 assets.append(f"High readiness: You're in the {readiness_stage} stage - primed for transformation")
            
#             if motivation and len(motivation) > 20:
#                 assets.append("Clear motivation: You know WHY you want this change - motivation sustains action")
            
#             if future_vision and len(future_vision) > 30:
#                 assets.append("Vision clarity: You can see your transformed future - this pulls you forward")
            
#             # Add default assets if few identified
#             if len(assets) < 4:
#                 assets.extend([
#                     "Courage: You're here, seeking help - that takes real strength",
#                     "Intelligence: You're approaching this systematically and thoughtfully",
#                     "Neuroplasticity: Your brain can rewire at any age - science proves it"
#                 ])
            
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Your Transformation Assets</h1>
#                     <p style="color: #556D7A;"><em>The strengths you already have for this journey</em></p>
                    
#                     <div class="highlight-box">
#                         <p style="margin: 0; font-size: 12pt; font-weight: bold;">
#                             You have everything needed for transformation. These patterns developed to protect you - 
#                             they served a purpose. Now you're ready to update them consciously.
#                         </p>
#                     </div>
                    
#                     <h2>Your Existing Strengths</h2>
#             """
            
#             for i, asset in enumerate(assets[:8], 1):
#                 html_content += f"""
#                     <div class="success-indicator">
#                         <p style="margin: 0;"><strong class="checkmark">✓</strong> {asset}</p>
#                     </div>
#                 """
            
#             html_content += """
#                     <div class="metric" style="margin-top: 30px;">
#                         <h3 style="margin-top: 0; color: #4CA1A3;">What Makes You Ready for Rapid Transformation</h3>
#                         <ul style="line-height: 1.8;">
#                             <li><strong>Self-awareness:</strong> You can identify your patterns - this is half the battle</li>
#                             <li><strong>Commitment:</strong> You invested time in this assessment - action follows commitment</li>
#                             <li><strong>Openness:</strong> You're willing to explore new approaches - flexibility enables change</li>
#                             <li><strong>Neuroplasticity:</strong> Your brain is wired to adapt - this is biology, not wishful thinking</li>
#                             <li><strong>Support:</strong> You're seeking professional guidance - collaboration accelerates results</li>
#                         </ul>
#                     </div>
#                 </div>
#             """
            
#             # ==================== PAGE 13: NEXT STEPS & RESOURCES ====================
#             html_content += f"""
#                 <div class="page-break">
#                     <h1>Next Steps & Resources</h1>
                    
#                     <h2>What Happens Next</h2>
                    
#                     <div class="session-card">
#                         <h3 style="color: #4CA1A3; margin-top: 0;">Immediate Actions (Next 24-48 Hours)</h3>
#                         <ol style="line-height: 1.8;">
#                             <li><strong>Clinical review:</strong> Your assessment is being analyzed for optimal approach</li>
#                             <li><strong>Personal contact:</strong> Expect contact within 24-48 hours via email/phone</li>
#                             <li><strong>Start practicing:</strong> Begin using your personalized techniques TODAY</li>
#                             <li><strong>Track patterns:</strong> Notice when they activate, use your intervention phrase</li>
#                         </ol>
#                     </div>
                    
#                     <div class="technique">
#                         <h3 style="margin-top: 0;">While You Wait for Session 1</h3>
#                         <ul style="line-height: 1.8;">
#                             <li>Read this blueprint daily - keep Quick Reference Card visible</li>
#                             <li>Practice your personalized mantras out loud every morning</li>
#                             <li>Use the PAUSE protocol whenever you notice your pattern</li>
#                             <li>Track your wins - any attempt counts as success</li>
#                             <li>Note specific recent examples to discuss in session 1</li>
#                         </ul>
#                     </div>
                    
#                     <h2>Scheduling Your Sessions</h2>
                    
#                     <div class="metric">
#                         <p><strong>Session format options:</strong></p>
#                         <ul>
#                             <li><strong>In-person:</strong> 27 Soi Sukhumvit 10, Bangkok (BTS Asoke)</li>
#                             <li><strong>Online:</strong> Secure video conferencing (equally effective)</li>
#                         </ul>
                        
#                         <p style="margin-top: 20px;"><strong>Investment:</strong></p>
#                         <ul>
#                             <li><strong>Standard program:</strong> ฿3,000 (Sessions 1 + 2)</li>
#                             <li><strong>Complete program:</strong> ฿4,000 (Sessions 1 + 2 + 3 if needed)</li>
#                         </ul>
                        
#                         <p style="margin-top: 20px; color: #556D7A;">
#                             <strong>Value comparison:</strong> Traditional therapy ฿15,000+ over 18+ months vs. 
#                             Specialized hypnotherapy ฿3,000-4,000 in 2-3 weeks
#                         </p>
#                     </div>
                    
#                     <h2>Additional Resources</h2>
                    
#                     <div class="technique">
#                         <h4>Crisis Support (24/7):</h4>
#                         <ul>
#                             <li><strong>Thailand Crisis Hotline:</strong> 1323</li>
#                             <li><strong>Samaritans of Thailand:</strong> 02-713-6793</li>
#                             <li><strong>Emergency Services:</strong> 1669</li>
#                         </ul>
                        
#                         <h4 style="margin-top: 20px;">Between-Session Support:</h4>
#                         <ul>
#                             <li>Email support for urgent questions</li>
#                             <li>This blueprint as your daily reference</li>
#                             <li>Weekly self-assessment protocol</li>
#                         </ul>
#                     </div>
                    
#                     <div class="success-indicator" style="margin-top: 30px;">
#                         <p style="margin: 0; font-weight: bold; font-size: 12pt;">
#                             <strong class="checkmark">✓</strong> You've taken the first step. Transformation has already begun. 
#                             Your awareness, commitment, and this roadmap position you for rapid, lasting change.
#                         </p>
#                     </div>
#                 </div>
#             """
            
#             # ==================== FOOTER & DISCLAIMER ====================
#             html_content += f"""
#                     <div class="footer">
#                         <div style="text-align: center; margin-bottom: 30px;">
#                             <p style="font-size: 11pt;">© {datetime.now().year} Rapid Transformation Hypnotherapy</p>
#                             <p style="font-size: 10pt; margin: 10px 0;">
#                                 <a href="https://hypnotherapy.streamlit.app" style="color: #4CA1A3; text-decoration: none;">
#                                     hypnotherapy.streamlit.app
#                                 </a>
#                             </p>
#                             <p>This document is confidential and prepared exclusively for {name}</p>
#                         </div>
                    
#                     <div class="highlight-box">
#                         <h4 style="margin-top: 0; color: #92400E;">IMPORTANT DISCLAIMER</h4>
#                         <p style="margin: 0; font-size: 10pt; color: #78350F; line-height: 1.6;">
#                             This assessment is a proprietary framework for hypnotherapy treatment planning. 
#                             It is not clinically validated and should not be used for self-diagnosis or as 
#                             a replacement for professional mental health care. Consult with qualified mental 
#                             health professionals for diagnostic assessment and evidence-based treatment recommendations.
#                         </p>
                        
#                         <p style="margin-top: 15px; font-size: 10pt; color: #78350F; line-height: 1.6;">
#                             <strong>Success rates and timelines:</strong> Individual results may vary. Success rates 
#                             are based on historical client outcomes and are not a guarantee of individual results. 
#                             Timeline estimates are typical but may vary based on individual circumstances and commitment 
#                             to the process.
#                         </p>
#                     </div>
                    
#                     <div style="text-align: center; margin-top: 30px; font-size: 9pt; color: #94A3B8;">
#                         <p>For questions or support: laetitiasheppard@gmail.com.com</p>
#                         <p style="margin-top: 10px;">
#                             <strong>Crisis Support:</strong> Thailand Mental Health Hotline 1323 (24/7) | Emergency 1669
#                         </p>
#                     </div>
#                 </div>
#             </body>
#             </html>
#             """
            
#             # Convert HTML to PDF
#             pdf_buffer = BytesIO()
#             pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
            
#             if pisa_status.err:
#                 print(f"PDF generation error: {pisa_status.err}")
#                 return None
            
#             pdf_buffer.seek(0)
#             return pdf_buffer.getvalue()
            
#         except Exception as e:
#             print(f"PDF generation error: {str(e)}")
#             import traceback
#             traceback.print_exc()
#             return None

#     def _check_crisis_indicators(self, responses: Dict) -> bool:
#         """Check for crisis indicators in responses"""
#         crisis_keywords = ['suicide', 'kill myself', 'end my life', 'no point living', 
#                         'want to die', 'better off dead', 'self harm', 'hurt myself']
        
#         for response_data in responses.values():
#             if isinstance(response_data, dict):
#                 response_text = str(response_data.get('response', '')).lower()
#             else:
#                 response_text = str(response_data).lower()
                
#             if any(keyword in response_text for keyword in crisis_keywords):
#                 return True
        
#         return False

#     def _generate_mantra_list(self, responses: Dict, pattern_hierarchy: Dict) -> List[Tuple[str, str]]:
#         """Generate list of personalized mantras"""
#         mantras = []
        
#         # Extract data
#         presenting_problem = self._extract_response_text(responses, 1)
#         automatic_thought = self._extract_response_text(responses, 37)
#         core_belief = self._extract_response_text(responses, 70)
#         first_action = self._extract_response_text(responses, 74)
        
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
#         pattern_id = dominant.get('id')
        
#         # Mantra 1: From presenting problem
#         if presenting_problem:
#             behavior = self._extract_key_behavior(presenting_problem)
#             mantras.append(('From your presenting concern', f"I am worthy even when I'm not {behavior}"))
        
#         # Mantra 2: From core belief
#         if core_belief:
#             inverted = self._invert_limiting_belief(core_belief)
#             mantras.append(('Your new empowering belief', inverted))
        
#         # Mantra 3: From automatic thought
#         if automatic_thought:
#             reframed = self._reframe_automatic_thought(automatic_thought)
#             mantras.append(('When that old thought appears', reframed))
        
#         # Mantra 4: From first action
#         if first_action:
#             action = self._extract_key_action(first_action)
#             mantras.append(('Your immediate possibility', f"I can {action} and remain whole"))
        
#         # Mantra 5: Pattern-specific
#         if pattern_id:
#             pattern_mantra = self._get_pattern_mantra(pattern_id)
#             mantras.append(('Your pattern transformation', pattern_mantra))
        
#         return mantras[:5]


# def create_behavioral_blueprint():
#     """Factory function"""
#     return BehavioralBlueprint()







"""
Blueprint Component - Premium Clinical Analysis (Production Ready)
COMPLETE VERSION with Professional ReportLab PDF Generation

Key Features:
1. Personalized mantras from user's actual language
2. Success metrics from user's visions
3. Technique scripts from trigger sequence + responses
4. Crisis resources if indicators detected
5. Professional PDF with ReportLab (Streamlit Cloud compatible)
6. Complete data utilization from master_analytics
"""

import streamlit as st
from typing import Dict, Optional, List, Tuple
from datetime import datetime
import plotly.graph_objects as go
import re


class BehavioralBlueprint:
    """Renders complete clinical blueprint with full data personalization"""

    def __init__(self):
        self.pattern_names = {
            1: "Unhappiness culture", 2: "Power struggles", 3: "Systematic mistrust",
            4: "Separation and division", 5: "Doing versus being", 
            6: "Compartmentalized authenticity", 7: "Self sacrifice and care avoidance",
            8: "Inherited missions", 9: "Context dependent weakness", 
            10: "Digital reality dissociation"
        }
        self._apply_print_friendly_styles()

    def _apply_print_friendly_styles(self):
        """Styles optimized for both screen and print/PDF - per color palette"""
        st.markdown("""
            <style>
            @media print {
                .stButton, .stDownloadButton { display: none; }
                .insight-card { page-break-inside: avoid; }
            }
            
            /* Color palette compliance */
            .insight-card {
                background: #FFFFFF;
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
                border-left: 4px solid #4CA1A3;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            }
            
            .action-item {
                background: #E1F0F0;
                padding: 1rem;
                border-radius: 6px;
                margin: 0.5rem 0;
                border-left: 3px solid #22c55e;
            }
            
            .mantra-box {
                background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                margin: 1rem 0;
                font-size: 1rem;
                font-weight: 500;
                line-height: 1.6;
            }
            
            .metric-card {
                background: #F3F6F8;
                padding: 1rem;
                border-radius: 8px;
                text-align: center;
                border: 1px solid #CBD5E1;
            }
            
            .session-card {
                background: #ffffff;
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
                border: 2px solid #4CA1A3;
            }
            
            .crisis-alert {
                background: #fee2e2;
                border-left: 6px solid #ef4444;
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
            }
            
            .success-indicator {
                background: #dcfce7;
                border-left: 4px solid #22c55e;
                padding: 1rem;
                border-radius: 6px;
                margin: 0.5rem 0;
            }
            
            /* Typography per guidelines */
            h1 { font-size: 2.2rem; color: #273548; margin-bottom: 0.5rem; }
            h2 { font-size: 1.8rem; color: #273548; margin-top: 2rem; margin-bottom: 1rem; }
            h3 { font-size: 1.4rem; color: #4CA1A3; margin-top: 1.5rem; }
            h4 { font-size: 1.2rem; color: #4CA1A3; }
            body, p, li { font-size: 1rem; color: #273548; line-height: 1.6; }
            .caption-text { font-size: 0.9rem; color: #556D7A; }
            </style>
        """, unsafe_allow_html=True)
    
    def render_complete_blueprint(self, assessment_data: Dict):
        """Render complete premium blueprint with FULL data utilization"""
        
        try:
            master_analytics = assessment_data.get('master_analytics', {})
            responses = assessment_data.get('responses', {})
            
            if not master_analytics:
                st.error("Analysis data not available. Please complete assessment first.")
                return
            
            # Single primary download button at top
            self._render_primary_download_section(assessment_data)
            
            st.markdown("---")
            
            # Table of contents
            self._render_table_of_contents()
            
            # 1. Personal cover page
            self._render_cover_page(assessment_data)
            
            # 2. Crisis resources (if needed - PRIORITY)
            self._render_crisis_resources_if_needed(responses, master_analytics)
            
            # 3. Quick reference card
            self._render_quick_reference_card(master_analytics, responses)
            
            # 4. PERSONALIZED mantras
            self._render_personalized_mantras(master_analytics, responses)
            
            # 5. Complete pattern analysis with visualization
            self._render_pattern_constellation(master_analytics)
            
            # 6. Behavioral blueprint (trigger sequence)
            self._render_trigger_blueprint(master_analytics, responses)
            
            # 7. PERSONALIZED immediate techniques
            self._render_personalized_techniques(master_analytics, responses)
            
            # 8. Session roadmap with digital integration
            self._render_integrated_session_roadmap(master_analytics)
            
            # 9. PERSONALIZED success tracking
            self._render_personalized_success_tracking(master_analytics, responses)
            
            # 10. Transformation assets
            self._render_transformation_assets(master_analytics, responses)
            
        except Exception as e:
            st.error(f"Error rendering blueprint: {str(e)}")
            st.info("Please contact support if this issue persists.")
            print(f"Blueprint rendering error: {str(e)}")
    
    def _render_primary_download_section(self, assessment_data: Dict):
        """Single primary PDF download button - PRODUCTION READY"""
        st.markdown("## Your complete transformation blueprint")
        st.caption("Complete clinical analysis with personalized techniques and roadmap")
        
        try:
            # Generate PDF
            pdf_bytes = self._generate_comprehensive_pdf(assessment_data)
            
            if pdf_bytes:
                contact = assessment_data.get('contact_info', {})
                name_slug = contact.get('full_name', 'client').lower().replace(' ', '_')
                filename = f"transformation_blueprint_{name_slug}_{datetime.now().strftime('%Y%m%d')}.pdf"
                
                # Primary centered download button
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.download_button(
                        label="📥 Download your complete blueprint (PDF)",
                        data=pdf_bytes,
                        file_name=filename,
                        mime="application/pdf",
                        type="primary",
                        use_container_width=True
                    )
                    st.caption("*Professional PDF report - ready to print or save*")
            else:
                st.warning("PDF generation temporarily unavailable. Viewing online version below.")
                
        except Exception as e:
            st.error("PDF download temporarily unavailable")
            st.info("You can view your complete blueprint below")
            print(f"PDF generation error: {str(e)}")
    
    def _generate_comprehensive_pdf(self, assessment_data: Dict) -> bytes:
        """Generate PREMIUM clinical blueprint PDF using ReportLab"""
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import inch, cm
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
            from io import BytesIO
            
            # Initialize PDF buffer
            buffer = BytesIO()
            
            # Extract data
            master_analytics = assessment_data.get('master_analytics', {})
            responses = assessment_data.get('responses', {})
            contact = assessment_data.get('contact_info', {})
            name = contact.get('full_name', 'Valued Client')
            
            # Define color palette (matching brand guidelines)
            PRIMARY_TEXT = colors.HexColor('#273548')
            SECONDARY_TEXT = colors.HexColor('#556D7A')
            ACCENT = colors.HexColor('#4CA1A3')
            ACCENT_LIGHT = colors.HexColor('#E1F0F0')
            SUCCESS = colors.HexColor('#22c55e')
            BACKGROUND = colors.HexColor('#F3F6F8')
            WHITE = colors.white
            
            # Create PDF document
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm,
                title=f"Transformation Blueprint - {name}",
                author="Rapid Transformation Hypnotherapy"
            )
            
            # Define custom styles
            styles = getSampleStyleSheet()
            
            # Title style (2.2rem equivalent)
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=28,
                textColor=ACCENT,
                spaceAfter=12,
                spaceBefore=0,
                alignment=TA_LEFT,
                fontName='Helvetica-Bold'
            )
            
            # Header style (1.8rem equivalent)
            header_style = ParagraphStyle(
                'CustomHeader',
                parent=styles['Heading2'],
                fontSize=22,
                textColor=ACCENT,
                spaceAfter=10,
                spaceBefore=20,
                alignment=TA_LEFT,
                fontName='Helvetica-Bold'
            )
            
            # Subheader style
            subheader_style = ParagraphStyle(
                'CustomSubheader',
                parent=styles['Heading3'],
                fontSize=14,
                textColor=PRIMARY_TEXT,
                spaceAfter=8,
                spaceBefore=12,
                fontName='Helvetica-Bold'
            )
            
            # Body text style (1rem equivalent)
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=11,
                textColor=PRIMARY_TEXT,
                spaceAfter=6,
                spaceBefore=0,
                alignment=TA_JUSTIFY,
                leading=16
            )
            
            # Caption style
            caption_style = ParagraphStyle(
                'CustomCaption',
                parent=styles['Normal'],
                fontSize=9,
                textColor=SECONDARY_TEXT,
                spaceAfter=4,
                italic=True
            )
            
            # Mantra box style
            mantra_style = ParagraphStyle(
                'MantraStyle',
                parent=styles['Normal'],
                fontSize=13,
                textColor=WHITE,
                spaceAfter=8,
                spaceBefore=8,
                alignment=TA_CENTER,
                fontName='Helvetica-Bold',
                leading=18
            )
            
            # Build document content
            story = []
            
            # Extract analytics
            pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            success_prediction = master_analytics.get('success_prediction', {})
            trigger_analysis = master_analytics.get('trigger_sequence', {})
            session_prediction = master_analytics.get('session_prediction', {})
            quality = master_analytics.get('assessment_quality', {})
            dominant = pattern_hierarchy.get('dominant_pattern', {})
            pattern_scores = pattern_hierarchy.get('all_scores', {})
            
            # ========== COVER PAGE ==========
            story.append(Spacer(1, 2*inch))
            
            story.append(Paragraph("Complete Transformation Blueprint", title_style))
            story.append(Spacer(1, 0.2*inch))
            story.append(Paragraph("Personalized Clinical Analysis & Roadmap", caption_style))
            story.append(Spacer(1, inch))
            
            # Client info box
            cover_data = [
                ["Prepared exclusively for:", name],
                ["Date:", datetime.now().strftime('%B %d, %Y')],
                ["Document ID:", f"BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}"]
            ]
            cover_table = Table(cover_data, colWidths=[3*inch, 3*inch])
            cover_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                ('TEXTCOLOR', (0, 0), (0, -1), SECONDARY_TEXT),
                ('TEXTCOLOR', (1, 0), (1, -1), PRIMARY_TEXT),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('PADDING', (0, 0), (-1, -1), 12),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1'))
            ]))
            story.append(cover_table)
            story.append(Spacer(1, 0.5*inch))
            
            # Summary metrics
            story.append(Paragraph("Your transformation summary", subheader_style))
            summary_data = [
                ["Primary pattern:", dominant.get('name', 'Assessment pending')],
                ["Intensity:", f"{dominant.get('score', 0):.1f}/10"],
                ["Success probability:", f"{success_prediction.get('overall_success_rate', 85)}%"],
                ["Timeline:", success_prediction.get('timeline_estimate', '2-3 weeks')]
            ]
            summary_table = Table(summary_data, colWidths=[2.5*inch, 3.5*inch])
            summary_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), WHITE),
                ('TEXTCOLOR', (0, 0), (0, -1), SECONDARY_TEXT),
                ('TEXTCOLOR', (1, 0), (1, -1), PRIMARY_TEXT),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('PADDING', (0, 0), (-1, -1), 10),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('ALIGN', (1, 0), (1, -1), 'LEFT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
                ('BOX', (0, 0), (-1, -1), 2, ACCENT)
            ]))
            story.append(summary_table)
            story.append(Spacer(1, 0.3*inch))
            
            story.append(Paragraph(
                "<i>This personalized clinical analysis contains your unique behavioral patterns, "
                "transformation roadmap, and actionable techniques for lasting change.</i>",
                caption_style
            ))
            
            story.append(PageBreak())
            
            # ========== TABLE OF CONTENTS ==========
            story.append(Paragraph("Table of contents", title_style))
            story.append(Spacer(1, 0.2*inch))
            
            toc_items = [
                "1. Quick reference card",
                "2. Your personalized mantras",
                "3. Complete pattern analysis",
                "4. Your behavioral blueprint",
                "5. Personalized intervention techniques",
                "6. Integrated session roadmap",
                "7. Personalized success metrics",
                "8. Your transformation assets",
                "9. Next steps & resources"
            ]
            
            for item in toc_items:
                story.append(Paragraph(f"• {item}", body_style))
                story.append(Spacer(1, 0.1*inch))
            
            story.append(PageBreak())
            
            # ========== QUICK REFERENCE CARD ==========
            story.append(Paragraph("Quick reference card", title_style))
            story.append(Paragraph("<i>Print this page and keep it visible - refer to it daily</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Primary pattern box
            pattern_box_data = [
                [Paragraph("<b>Your primary pattern</b>", subheader_style)],
                [Paragraph(f"<b>{dominant.get('name', 'Unknown')}</b>", ParagraphStyle('PatternName', parent=body_style, fontSize=16, textColor=ACCENT, fontName='Helvetica-Bold'))],
                [Paragraph(f"<b>Intensity:</b> {dominant.get('score', 0):.1f}/10", body_style)],
                [Paragraph(self._get_pattern_brief_description(dominant.get('id')), caption_style)]
            ]
            pattern_box = Table(pattern_box_data, colWidths=[6*inch])
            pattern_box.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                ('PADDING', (0, 0), (-1, -1), 12),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('BOX', (0, 0), (-1, -1), 2, ACCENT)
            ]))
            story.append(pattern_box)
            story.append(Spacer(1, 0.2*inch))
            
            # PAUSE protocol
            story.append(Paragraph("When you notice your pattern starting:", subheader_style))
            pause_items = [
                f"<b>1. PAUSE</b> - Stop what you're doing, take 3 deep breaths",
                f"<b>2. NAME</b> - Say: 'This is my {dominant.get('name', 'pattern')} pattern'",
                f"<b>3. CHOOSE</b> - Say: 'I can respond differently'",
                f"<b>4. ACT</b> - Use one of your personalized techniques"
            ]
            
            for item in pause_items:
                story.append(Paragraph(f"• {item}", body_style))
                story.append(Spacer(1, 0.05*inch))
            
            story.append(Spacer(1, 0.2*inch))
            
            # Intervention phrase (mantra box)
            core_belief = self._extract_response_text(responses, 70)
            intervention_phrase = self._invert_limiting_belief(core_belief) if core_belief else self._get_intervention_phrase(dominant.get('id'))
            
            mantra_data = [
                [Paragraph("Your daily intervention phrase", ParagraphStyle('MantraCaption', parent=caption_style, textColor=WHITE, alignment=TA_CENTER))],
                [Paragraph(f'"{intervention_phrase}"', mantra_style)],
                [Paragraph("<i>Say this OUT LOUD every morning and whenever you notice your pattern activating</i>", ParagraphStyle('MantraNote', parent=caption_style, textColor=WHITE, alignment=TA_CENTER, fontSize=9))]
            ]
            mantra_box = Table(mantra_data, colWidths=[6*inch])
            mantra_box.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), ACCENT),
                ('PADDING', (0, 0), (-1, -1), 15),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0)
            ]))
            story.append(mantra_box)
            story.append(Spacer(1, 0.2*inch))
            
            # Emergency resources
            story.append(Paragraph("Emergency support resources", subheader_style))
            resources_data = [
                ["Thailand crisis hotline:", "1323 (24/7)"],
                ["Samaritans of Thailand:", "02-713-6793"],
                ["Emergency services:", "1669"]
            ]
            resources_table = Table(resources_data, colWidths=[2.5*inch, 3.5*inch])
            resources_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), WHITE),
                ('TEXTCOLOR', (0, 0), (-1, -1), PRIMARY_TEXT),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('PADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1'))
            ]))
            story.append(resources_table)
            
            story.append(PageBreak())
            
            # ========== PERSONALIZED MANTRAS ==========
            story.append(Paragraph("Your personalized transformation mantras", title_style))
            story.append(Paragraph("<i>Generated from YOUR words - read these daily, say them out loud</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            mantras = self._generate_mantra_list(responses, pattern_hierarchy)
            
            if mantras:
                for i, (source, mantra) in enumerate(mantras, 1):
                    mantra_item_data = [
                        [Paragraph(f"<i>{source}</i>", caption_style)],
                        [Paragraph(f'"{mantra}"', ParagraphStyle('MantraItem', parent=body_style, fontSize=12, fontName='Helvetica-Bold', textColor=ACCENT))]
                    ]
                    mantra_item_box = Table(mantra_item_data, colWidths=[6*inch])
                    mantra_item_box.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                        ('PADDING', (0, 0), (-1, -1), 12),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('BOX', (0, 0), (-1, -1), 1, ACCENT)
                    ]))
                    story.append(mantra_item_box)
                    story.append(Spacer(1, 0.15*inch))
            
            story.append(PageBreak())
            
            # ========== PATTERN ANALYSIS ==========
            story.append(Paragraph("Complete pattern analysis", title_style))
            story.append(Paragraph("<i>Your unique behavioral pattern constellation</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            if pattern_scores:
                # Pattern intensity breakdown
                story.append(Paragraph("Pattern intensity breakdown", header_style))
                story.append(Paragraph(
                    "Your patterns are scored 0-10 based on frequency, intensity, and impact. "
                    "Scores ≥6.0 indicate clinical concern requiring intervention.",
                    caption_style
                ))
                story.append(Spacer(1, 0.15*inch))
                
                # Create pattern table
                pattern_table_data = [["Pattern", "Score", "Status"]]
                
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
                for pattern_id, score in sorted_patterns:
                    if score > 0:
                        pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                        
                        if score >= 8.0:
                            status = "Severe"
                        elif score >= 6.0:
                            status = "Significant"
                        elif score >= 4.0:
                            status = "Moderate"
                        else:
                            status = "Adaptive"
                        
                        pattern_table_data.append([
                            pattern_name,
                            f"{score:.1f}/10",
                            status
                        ])
                
                pattern_table = Table(pattern_table_data, colWidths=[3*inch, 1.5*inch, 1.5*inch])
                pattern_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
                    ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('BACKGROUND', (0, 1), (-1, -1), WHITE),
                    ('TEXTCOLOR', (0, 1), (-1, -1), PRIMARY_TEXT),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('PADDING', (0, 0), (-1, -1), 8),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
                    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                    ('ALIGN', (2, 0), (2, -1), 'CENTER'),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, BACKGROUND])
                ]))
                story.append(pattern_table)
            
            story.append(PageBreak())
            
            # ========== BEHAVIORAL BLUEPRINT ==========
            sequence = trigger_analysis.get('trigger_sequence', {})
            
            story.append(Paragraph("Your behavioral blueprint", title_style))
            story.append(Paragraph("<i>This is YOUR unique automatic sequence - memorize this pattern</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            sequence_steps = [
                ('environmental_trigger', 'Environmental trigger', 'What starts the sequence'),
                ('physical_response', 'Physical response', 'Body sensations'),
                ('automatic_thought', 'Automatic thought', 'Mental response'),
                ('emotional_response', 'Emotional response', 'Feelings activated'),
                ('behavioral_response', 'Behavioral response', 'What you do'),
                ('immediate_consequence', 'Immediate result', 'What happens next')
            ]
            
            for key, title, description in sequence_steps:
                value = sequence.get(key, 'Not yet captured')
                
                if value and value != 'Not yet captured':
                    step_data = [
                        [Paragraph(f"<b>{title}</b>", subheader_style)],
                        [Paragraph(f"<i>{description}</i>", caption_style)],
                        [Paragraph(value, body_style)]
                    ]
                    step_box = Table(step_data, colWidths=[6*inch])
                    step_box.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                        ('PADDING', (0, 0), (-1, -1), 10),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('BOX', (0, 0), (-1, -1), 1, ACCENT)
                    ]))
                    story.append(step_box)
                    story.append(Spacer(1, 0.15*inch))
            
            story.append(PageBreak())
            
            # ========== PERSONALIZED TECHNIQUES ==========
            story.append(Paragraph("Your personalized intervention techniques", title_style))
            story.append(Paragraph("<i>Start using these TODAY - before your first session</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Technique 1: Somatic
            physical_response = sequence.get('physical_response', 'physical tension')
            story.append(Paragraph("Technique 1: Somatic intervention", header_style))
            story.append(Paragraph(f'<b>When you notice:</b> "{physical_response}"', body_style))
            story.append(Spacer(1, 0.1*inch))
            
            somatic_steps = [
                "<b>STOP</b> - Freeze your body exactly as it is",
                "<b>BREATHE</b> - 4 counts in through nose, 6 counts out through mouth (3 times)",
                "<b>SCAN</b> - Notice the sensation without judgment",
                "<b>RELEASE</b> - Consciously relax that area",
                "<b>GROUND</b> - Feel your feet on the floor, notice 3 things you can see"
            ]
            
            for i, step in enumerate(somatic_steps, 1):
                story.append(Paragraph(f"{i}. {step}", body_style))
                story.append(Spacer(1, 0.05*inch))
            
            story.append(Spacer(1, 0.15*inch))
            
            # Technique 2: Cognitive reframe
            automatic_thought = self._extract_response_text(responses, 37)
            if automatic_thought:
                reframed = self._reframe_automatic_thought(automatic_thought)
                story.append(Paragraph("Technique 2: Cognitive reframe", header_style))
                story.append(Paragraph(f'<b>Old automatic thought:</b> "{automatic_thought[:150]}..."', body_style))
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph(f'<b>Your new empowering response:</b> <font color="#22c55e">"{reframed}"</font>', body_style))
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph("<i>Say your new response OUT LOUD 3 times daily</i>", caption_style))
            
            story.append(PageBreak())
            
            # ========== SESSION ROADMAP ==========
            session_structure = session_prediction.get('session_structure', {})
            detailed_planning = session_prediction.get('detailed_planning', {})
            
            story.append(Paragraph("Your transformation timeline", title_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Timeline overview
            timeline_data = [
                ["Total sessions:", session_structure.get('total_sessions', '2 sessions')],
                ["Session length:", session_structure.get('session_length', '90 minutes each')],
                ["Total timeline:", session_structure.get('timeline', '2-3 weeks')]
            ]
            timeline_table = Table(timeline_data, colWidths=[2*inch, 4*inch])
            timeline_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), BACKGROUND),
                ('TEXTCOLOR', (0, 0), (0, -1), SECONDARY_TEXT),
                ('TEXTCOLOR', (1, 0), (1, -1), PRIMARY_TEXT),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('PADDING', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1'))
            ]))
            story.append(timeline_table)
            story.append(Spacer(1, 0.2*inch))
            
            # Session 1
            story.append(Paragraph("Session 1: Foundation and pattern mapping (90 minutes)", header_style))
            session1_plan = detailed_planning.get('session_1', 'Complete pattern mapping and initial programming')
            story.append(Paragraph(session1_plan, body_style))
            story.append(Spacer(1, 0.15*inch))
            
            # Session 2
            story.append(Paragraph("Session 2: Deep transformation and integration (90 minutes)", header_style))
            session2_plan = detailed_planning.get('session_2', 'Deep neural rewiring and integration')
            story.append(Paragraph(session2_plan, body_style))
            
            story.append(PageBreak())
            
            # ========== SUCCESS METRICS ==========
            story.append(Paragraph("Your personalized success metrics", title_style))
            story.append(Paragraph("<i>Track these specific milestones from YOUR vision</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            first_action = self._extract_response_text(responses, 74)
            if first_action:
                story.append(Paragraph("Week 1 immediate milestone", header_style))
                story.append(Paragraph(f'<b>Your first win:</b> "{first_action[:200]}"', body_style))
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph("✓ Any attempt counts as success", body_style))
                story.append(Spacer(1, 0.15*inch))
            
            # Success probability
            story.append(Paragraph("Your success probability analysis", header_style))
            success_data = [
                ["Overall success rate:", f"{success_prediction.get('overall_success_rate', 85)}%"],
                ["Timeline estimate:", success_prediction.get('timeline_estimate', '2-3 weeks')],
                ["Success tier:", success_prediction.get('success_tier', 'High')]
            ]
            success_table = Table(success_data, colWidths=[2.5*inch, 3.5*inch])
            success_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                ('TEXTCOLOR', (0, 0), (0, -1), SECONDARY_TEXT),
                ('TEXTCOLOR', (1, 0), (1, -1), PRIMARY_TEXT),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 11),
                ('PADDING', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, ACCENT),
                ('BOX', (0, 0), (-1, -1), 2, ACCENT)
            ]))
            story.append(success_table)
            
            story.append(PageBreak())
            
            # ========== TRANSFORMATION ASSETS ==========
            story.append(Paragraph("Your transformation assets", title_style))
            story.append(Paragraph("<i>The strengths you already have for this journey</i>", caption_style))
            story.append(Spacer(1, 0.2*inch))
            
            # Extract assets
            assets = []
            
            completion_rate = quality.get('completion_rate', 0)
            if completion_rate >= 90:
                assets.append("High commitment: Your 90%+ assessment completion shows dedication to change")
            
            pattern_count = pattern_hierarchy.get('pattern_count', 0)
            if pattern_count >= 3:
                assets.append("Strong self-awareness: You recognize multiple patterns")
            
            if len(assets) < 3:
                assets.extend([
                    "Courage: You're here, seeking help - that takes real strength",
                    "Intelligence: You're approaching this systematically",
                    "Neuroplasticity: Your brain can rewire at any age"
                ])
            
            for asset in assets[:6]:
                story.append(Paragraph(f"✓ {asset}", body_style))
                story.append(Spacer(1, 0.08*inch))
            
            story.append(PageBreak())
            
            # ========== NEXT STEPS ==========
            story.append(Paragraph("Next steps & resources", title_style))
            story.append(Spacer(1, 0.2*inch))
            
            story.append(Paragraph("What happens next", header_style))
            next_steps = [
                "<b>Clinical review</b> (24-48 hours): Your assessment is being analyzed",
                "<b>Personal contact</b> (48-72 hours): Expect contact via email/phone",
                "<b>Start practicing</b>: Begin using your techniques TODAY",
                "<b>Track patterns</b>: Notice when they activate"
            ]
            
            for i, step in enumerate(next_steps, 1):
                story.append(Paragraph(f"{i}. {step}", body_style))
                story.append(Spacer(1, 0.08*inch))
            
            story.append(Spacer(1, 0.2*inch))
            
            # Investment
            story.append(Paragraph("Investment", header_style))
            investment_data = [
                ["Standard program (2 sessions):", "฿3,000"],
                ["Complete program (3 sessions):", "฿4,000"]
            ]
            investment_table = Table(investment_data, colWidths=[3.5*inch, 2.5*inch])
            investment_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), SUCCESS),
                ('TEXTCOLOR', (0, 0), (-1, -1), WHITE),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('PADDING', (0, 0), (-1, -1), 12),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT')
            ]))
            story.append(investment_table)
            story.append(Spacer(1, 0.15*inch))
            
            story.append(Paragraph(
                "<i>Value comparison: Traditional therapy ฿15,000+ over 18+ months vs. "
                "Specialized hypnotherapy ฿3,000-4,000 in 2-3 weeks</i>",
                caption_style
            ))
            
            story.append(Spacer(1, 0.3*inch))
            
            # Footer
            footer_text = f"""
            <para alignment="center">
            © {datetime.now().year} Rapid Transformation Hypnotherapy<br/>
            This document is confidential and prepared exclusively for {name}<br/>
            <br/>
            <b>IMPORTANT DISCLAIMER:</b> This assessment is a proprietary framework for hypnotherapy 
            treatment planning. It is not clinically validated and should not be used for self-diagnosis 
            or as a replacement for professional mental health care.<br/>
            <br/>
            For questions or support: laetitiasheppard@gmail.com<br/>
            <b>Crisis Support:</b> Thailand Mental Health Hotline 1323 (24/7) | Emergency 1669
            </para>
            """
            story.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=caption_style, fontSize=8, alignment=TA_CENTER, leading=12)))
            
            # Build PDF
            doc.build(story)
            
            buffer.seek(0)
            return buffer.getvalue()
            
        except Exception as e:
            print(f"PDF generation error: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    # ========== HELPER METHODS FOR PERSONALIZATION ==========
    
    def _extract_response_text(self, responses: Dict, question_id: int) -> str:
        """Extract text response from responses dict"""
        response_data = responses.get(question_id)
        
        if isinstance(response_data, dict):
            return str(response_data.get('response', ''))
        elif isinstance(response_data, str):
            return response_data
        return ''
    
    def _extract_key_behavior(self, presenting_problem: str) -> str:
        """Extract key behavior from presenting problem text"""
        text = presenting_problem.lower().strip()
        
        if 'stop' in text or 'quit' in text:
            words = text.split()
            for i, word in enumerate(words):
                if word in ['stop', 'quit', 'avoiding', 'procrastinating']:
                    if i + 1 < len(words):
                        return ' '.join(words[i+1:i+4])
        
        words = text.split()
        return ' '.join(words[:min(5, len(words))])
    
    def _invert_limiting_belief(self, core_belief: str) -> str:
        """Invert limiting belief to empowering belief"""
        text = core_belief.lower().strip()
        
        inversions = {
            "can't": "can",
            "cannot": "can",
            "never": "can always",
            "not good enough": "enough exactly as I am",
            "don't deserve": "deserve",
            "impossible": "possible",
            "won't work": "will work",
            "too late": "never too late",
            "not worthy": "worthy"
        }
        
        inverted = text
        for old, new in inversions.items():
            if old in inverted:
                inverted = inverted.replace(old, new)
                break
        
        if inverted and inverted != text:
            return inverted[0].upper() + inverted[1:]
        
        return "I am capable of transformation and growth"
    
    def _reframe_automatic_thought(self, automatic_thought: str) -> str:
        """Reframe automatic negative thought to empowering response"""
        text = automatic_thought.lower().strip()
        
        if 'never' in text or 'always fail' in text:
            return "Every moment is a new opportunity to choose differently"
        elif 'not good enough' in text or 'inadequate' in text:
            return "I am enough exactly as I am in this moment"
        elif 'can\'t' in text or 'impossible' in text:
            return "I am discovering new capabilities every day"
        elif 'should' in text or 'must' in text:
            return "I choose my path with compassion and wisdom"
        elif 'everyone' in text or 'nobody' in text:
            return "I release others' opinions and trust my own knowing"
        
        return "I choose to respond with awareness and compassion"
    
    def _extract_key_action(self, first_action: str) -> str:
        """Extract key action from first action vision"""
        text = first_action.lower().strip()
        
        prefixes = ['i would', 'i will', 'i could', 'i can', 'i\'d']
        for prefix in prefixes:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
                break
        
        if ',' in text:
            text = text.split(',')[0]
        if '.' in text:
            text = text.split('.')[0]
        
        text = text.strip()
        
        return text if text else "take my first step toward freedom"
    
    def _generate_alternative_behavior(self, old_behavior: str) -> str:
        """Generate healthier alternative to automatic behavior"""
        text = old_behavior.lower()
        
        if 'scroll' in text or 'social media' in text or 'phone' in text:
            return "Take a 5-minute walk outside or call a real person"
        elif 'avoid' in text or 'withdraw' in text or 'isolate' in text:
            return "Text one person you trust: 'I'm struggling and could use connection'"
        elif 'argue' in text or 'defensive' in text or 'attack' in text:
            return "Say: 'I need a moment to process this. Can we continue in 10 minutes?'"
        elif 'numb' in text or 'zone out' in text or 'dissociate' in text:
            return "Use the 5-4-3-2-1 grounding technique (engage all senses)"
        elif 'busy' in text or 'work' in text or 'productive' in text:
            return "Set timer for 10 minutes of intentional rest - no agenda"
        elif 'please' in text or 'accommodate' in text or 'say yes' in text:
            return "Practice: 'Let me check my capacity and get back to you'"
        
        return "Pause for 3 breaths, then choose a response that honors both me and others"
    
    def _generate_mantra_list(self, responses: Dict, pattern_hierarchy: Dict) -> List[Tuple[str, str]]:
        """Generate list of personalized mantras"""
        mantras = []
        
        presenting_problem = self._extract_response_text(responses, 1)
        automatic_thought = self._extract_response_text(responses, 37)
        core_belief = self._extract_response_text(responses, 70)
        first_action = self._extract_response_text(responses, 74)
        
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        pattern_id = dominant.get('id')
        
        if presenting_problem:
            behavior = self._extract_key_behavior(presenting_problem)
            mantras.append(('From your presenting concern', f"I am worthy even when I'm not {behavior}"))
        
        if core_belief:
            inverted = self._invert_limiting_belief(core_belief)
            mantras.append(('Your new empowering belief', inverted))
        
        if automatic_thought:
            reframed = self._reframe_automatic_thought(automatic_thought)
            mantras.append(('When that old thought appears', reframed))
        
        if first_action:
            action = self._extract_key_action(first_action)
            mantras.append(('Your immediate possibility', f"I can {action} and remain whole"))
        
        if pattern_id:
            pattern_mantra = self._get_pattern_mantra(pattern_id)
            mantras.append(('Your pattern transformation', pattern_mantra))
        
        return mantras[:5]
    
    def _get_pattern_mantra(self, pattern_id: Optional[int]) -> str:
        """Pattern-specific mantra"""
        if pattern_id is None or pattern_id not in range(1, 11):
            return "I am capable of transformation and growth"
        
        mantras = {
            1: "I deserve happiness and it's safe for me to feel joy",
            2: "Collaboration strengthens me more than conflict ever could",
            3: "Discernment and openness can coexist - I am wise AND trusting",
            4: "I embrace complexity and find creative solutions beyond either/or",
            5: "My worth exists independent of any achievement or productivity",
            6: "My authentic self is enough in every situation",
            7: "Taking care of myself enables me to truly serve others",
            8: "I honor my family AND claim my own authentic path",
            9: "My boundaries remain consistent across all contexts and people",
            10: "Real connection happens offline - I choose presence over performance"
        }
        return mantras.get(pattern_id, "I am capable of transformation and growth")
    
    def _get_intervention_phrase(self, pattern_id: Optional[int]) -> str:
        """Pattern intervention phrase"""
        if pattern_id is None or pattern_id not in range(1, 11):
            return "I choose a new response"
        
        phrases = {
            1: "This happiness is mine to keep",
            2: "Curiosity, not combat",
            3: "Discernment yes, cynicism no",
            4: "Both/and, not either/or",
            5: "I am, not I do",
            6: "One me, all contexts",
            7: "My needs matter too",
            8: "My path, my choice",
            9: "Consistent boundaries, confident self",
            10: "Present moment, real connection"
        }
        return phrases.get(pattern_id, "I choose a new response")
    
    def _get_pattern_brief_description(self, pattern_id: int) -> str:
        """Brief pattern description"""
        descriptions = {
            1: "Difficulty accepting and maintaining positive emotional states",
            2: "Recurring conflicts and defensive responses in relationships",
            3: "Default skepticism about others' intentions and motivations",
            4: "Black-and-white thinking that limits creative solutions",
            5: "Self-worth tied to productivity and achievement",
            6: "Different selves in different contexts, lacking integration",
            7: "Prioritizing others' needs while neglecting self-care",
            8: "Life choices driven by family expectations vs personal desires",
            9: "Boundaries and limits varying dramatically by context",
            10: "Digital world feels more real than offline relationships"
        }
        return descriptions.get(pattern_id, "Pattern affects daily functioning")
    
    def _get_pattern_specific_technique(self, pattern_id: Optional[int]) -> str:
        """Pattern-specific technique"""
        if pattern_id is None or pattern_id not in range(1, 11):
            return "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it. Breathe. Choose differently."
        
        techniques = {
            1: "<strong>Happiness permission practice:</strong><br>When something good happens, say out loud: 'I deserve this and it's safe to enjoy it.' Repeat 3 times.",
            2: "<strong>Curiosity reframe:</strong><br>When you feel defensive, say: 'I'm curious about their perspective.' Take 3 breaths.",
            3: "<strong>Discernment check:</strong><br>When suspicion arises, ask: 'What evidence do I actually have?' Then: 'What would trust look like here?'",
            4: "<strong>Both/and thinking:</strong><br>When facing a decision, complete: 'Instead of choosing X OR Y, what if I could have aspects of X AND Y by...'",
            5: "<strong>Being practice:</strong><br>Set timer for 5 minutes. Sit quietly. Every time you think 'I should be doing something', respond: 'Right now, being is enough.'",
            6: "<strong>Authenticity anchor:</strong><br>Before entering any situation, touch your heart and say: 'Same me, every context.'",
            7: "<strong>Boundary affirmation:</strong><br>When asked for something, pause. Feel your body. Ask: 'Do I genuinely want to do this?' Honor the answer.",
            8: "<strong>Path clarification:</strong><br>Daily ask: 'If no one would know, judge, or be disappointed, what would I choose?'",
            9: "<strong>Consistent self practice:</strong><br>Identify your 'difficult context.' Practice saying 'no' to small requests there.",
            10: "<strong>Digital detox micro-practice:</strong><br>Before checking phone/social media, ask: 'Am I seeking connection or avoiding feeling?'"
        }
        return techniques.get(pattern_id, "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it. Breathe. Choose differently.")
    
    def _extract_behavioral_markers(self, future_vision: str) -> List[str]:
        """Extract specific behavioral markers from future vision text"""
        sentences = re.split(r'[.!?]+', future_vision)
        
        markers = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 10:
                markers.append(sentence[:100])
        
        if len(markers) < 3:
            markers.extend([
                "Reduced anxiety and increased peace",
                "Improved relationships and communication",
                "Greater confidence in decision-making"
            ])
        
        return markers[:5]
    
    def _generate_domain_specific_wins(self, impact_area: str) -> List[str]:
        """Generate success metrics for specific life domain"""
        domain = impact_area.lower()
        
        domain_metrics = {
            'work': [
                "Reduced procrastination on important tasks",
                "Better boundaries with colleagues/clients",
                "Increased focus and productivity",
                "More confident in meetings/presentations"
            ],
            'relationship': [
                "Authentic communication without masks",
                "Comfortable setting boundaries",
                "Reduced defensiveness in conflicts",
                "Deeper emotional connections"
            ],
            'family': [
                "Reduced reactivity with family members",
                "Clearer boundaries maintained",
                "More authentic self-expression",
                "Reduced guilt about own choices"
            ],
            'health': [
                "Prioritizing self-care without guilt",
                "Reduced stress-related symptoms",
                "Better sleep quality",
                "Consistent healthy habits"
            ]
        }
        
        for key, metrics in domain_metrics.items():
            if key in domain:
                return metrics
        
        return [
            "Increased self-awareness and pattern recognition",
            "More conscious choices vs. automatic reactions",
            "Greater emotional regulation",
            "Improved overall life satisfaction"
        ]

    # ========== SCREEN RENDERING METHODS (existing methods continue below) ==========
    
    def _render_crisis_resources_if_needed(self, responses: Dict, master_analytics: Dict):
        """PRIORITY: Add crisis resources if indicators detected"""
        
        crisis_keywords = ['suicide', 'kill myself', 'end my life', 'no point living', 
                          'want to die', 'better off dead']
        
        has_crisis = False
        for response_data in responses.values():
            if isinstance(response_data, dict):
                response_text = str(response_data.get('response', '')).lower()
            else:
                response_text = str(response_data).lower()
                
            if any(keyword in response_text for keyword in crisis_keywords):
                has_crisis = True
                break
        
        quality = master_analytics.get('assessment_quality', {})
        validation_flags = quality.get('validation_flags', [])
        
        if has_crisis or 'crisis_indicator' in str(validation_flags):
            st.markdown("## 🚨 Immediate support resources")
            
            st.error("""
**If you are in immediate danger or crisis**

Please reach out for immediate help. You are not alone, and support is available 24/7.

**24/7 crisis hotlines:**
- **Thailand suicide hotline:** 1323
- **Samaritans of Thailand:** 02-713-6793
- **International crisis line:** [befrienders.org](https://www.befrienders.org)
- **Emergency services:** 1669

**Important:** Your therapist will prioritize contact within 2 hours. Please check your email and phone.
            """)
            
            st.markdown("### Safety planning")
            
            st.info("""
**Create your safety plan now:**

1. **Warning signs I can notice:**
- (Write down physical, emotional, mental signs)

2. **People I can contact:**
- Friend/family: _______________
- Crisis hotline: 1323
- Therapist: (will be provided)

3. **Safe places I can go:**
- _______________
- _______________

4. **Things that help me feel better:**
- _______________
- _______________

5. **Reasons for living:**
- _______________
- _______________
            """)
            
            st.markdown("---")
    
    def _render_table_of_contents(self):
        """Table of contents"""
        with st.expander("📋 **Table of contents**", expanded=False):
            st.markdown("""
            1. **Personal cover page**
            2. **Crisis resources** (if applicable)
            3. **Quick reference card**
            4. **Personalized mantras** (from your words)
            5. **Complete pattern analysis**
            6. **Behavioral blueprint** (trigger sequence)
            7. **Personalized techniques** (for your patterns)
            8. **Session roadmap** (with digital integration)
            9. **Success tracking** (your metrics)
            10. **Transformation assets** (your strengths)
            """)

    def _render_cover_page(self, assessment_data: Dict):
        """Personal cover page"""
        contact = assessment_data.get('contact_info', {})
        name = contact.get('full_name', 'Valued client')
        
        master_analytics = assessment_data.get('master_analytics', {})
        pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
        success_prediction = master_analytics.get('success_prediction', {})
        
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        
        st.markdown(f"""
        # Complete transformation blueprint
        
        **Prepared exclusively for:** {name}  
        **Date:** {datetime.now().strftime('%B %d, %Y')}  
        **Document ID:** BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}
        
        ---
        
        ### Your transformation summary
        
        **Primary pattern:** {dominant.get('name', 'Assessment pending')}  
        **Intensity:** {dominant.get('score', 0):.1f}/10  
        **Success probability:** {success_prediction.get('overall_success_rate', 85)}%  
        **Timeline:** {success_prediction.get('timeline_estimate', '2-3 weeks')}  
        
        ---
        
        *This personalized clinical analysis contains your unique behavioral patterns, 
        transformation roadmap, and actionable techniques for lasting change.*
        """)

    def _render_quick_reference_card(self, master_analytics: Dict, responses: Dict):
        """Quick reference card with personalization"""
        st.markdown("## 🎯 Quick reference card")
        st.caption("Print this section and keep it visible")
        
        pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Your primary pattern")
            if dominant:
                st.info(f"**{dominant.get('name', 'Unknown')}**\n\nIntensity: {dominant.get('score', 0):.1f}/10")
            
            st.markdown("### When you notice it starting:")
            st.success("""
            1. **PAUSE** - Take 3 deep breaths
            2. **NAME** - "This is my pattern"
            3. **CHOOSE** - "I can respond differently"
            """)
        
        with col2:
            st.markdown("### Your intervention phrase")
            
            core_belief = self._extract_response_text(responses, 70)
            if core_belief:
                inverted = self._invert_limiting_belief(core_belief)
                intervention = inverted
            else:
                pattern_id = dominant.get('id')
                intervention = self._get_intervention_phrase(pattern_id)
            
            st.markdown(f"""
            <div class="mantra-box">
                "{intervention}"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### Emergency support")
            st.markdown("""
            - **Crisis hotline:** 1323 (24/7)
            - **Keep this blueprint:** Review techniques daily
            - **Track wins:** Every small victory matters
            """)

    def _render_personalized_mantras(self, master_analytics: Dict, responses: Dict):
        """ENHANCED: Generate mantras from user's ACTUAL language"""
        st.markdown("## 💪 Your personal transformation mantras")
        st.caption("Generated from YOUR words - read these daily")
        
        try:
            mantras = self._generate_mantra_list(responses, master_analytics.get('pattern_hierarchy', {}))
            
            if mantras:
                for i, (source, mantra) in enumerate(mantras, 1):
                    st.markdown(f"""
                    <div class="mantra-box">
                        <div style="font-size: 0.85rem; opacity: 0.9; margin-bottom: 0.5rem;">{source}</div>
                        <div style="font-size: 1.1rem; font-weight: 600;">"{mantra}"</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
                self._render_pattern_based_mantras(pattern_hierarchy)
                
        except Exception as e:
            st.warning("Personalized mantras will be refined in session 1")
            self._render_pattern_based_mantras(master_analytics.get('pattern_hierarchy', {}))
            print(f"Personalized mantras error: {str(e)}")
    
    def _render_pattern_based_mantras(self, pattern_hierarchy: Dict):
        """Fallback: Pattern-based mantras if personalization fails"""
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        
        mantras = []
        
        if dominant:
            pattern_id = dominant.get('id')
            mantras.append(self._get_pattern_mantra(pattern_id))
        
        for pattern in primary_patterns[:2]:
            pattern_id = pattern.get('id')
            mantras.append(self._get_pattern_mantra(pattern_id))
        
        for i, mantra in enumerate(mantras, 1):
            st.markdown(f"""
            <div class="mantra-box">
                <div style="font-size: 1.1rem; font-weight: 600;">"{mantra}"</div>
            </div>
            """, unsafe_allow_html=True)

    def _render_pattern_constellation(self, master_analytics: Dict):
        """Pattern constellation with radar chart"""
        st.markdown("## Complete pattern analysis")
        st.caption("Your unique behavioral pattern constellation")
        
        try:
            pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            pattern_scores = pattern_hierarchy.get('all_scores', {})
            
            if not pattern_scores:
                st.info("Pattern analysis will be completed in session 1")
                return
            
            # Radar chart
            self._render_pattern_radar_chart(pattern_scores)
            
            st.markdown("---")
            
            # Pattern breakdown
            st.markdown("### Pattern intensity breakdown")
            
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            for pattern_id, score in sorted_patterns:
                if score > 0:
                    pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                    intensity_pct = min((score / 10) * 100, 100)
                    
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{pattern_name}**")
                        st.progress(intensity_pct / 100)
                    with col2:
                        st.markdown(f"**{score:.1f}/10**")
                    
                    st.caption(self._get_pattern_brief_description(pattern_id))
                    st.markdown("")
            
        except Exception as e:
            st.warning("Complete pattern visualization will be available in session 1")
            print(f"Pattern constellation error: {str(e)}")

    def _render_pattern_radar_chart(self, pattern_scores: Dict):
        """Render radar chart"""
        try:
            categories = []
            values = []
            
            for pattern_id in range(1, 11):
                pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                score = pattern_scores.get(pattern_id, 0)
                categories.append(pattern_name)
                values.append(score)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                fillcolor='rgba(76, 161, 163, 0.3)',
                line=dict(color='#4CA1A3', width=2),
                name='Your patterns'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10],
                        tickfont=dict(size=10),
                        gridcolor='#CBD5E1'
                    ),
                    angularaxis=dict(
                        tickfont=dict(size=10)
                    )
                ),
                showlegend=False,
                height=500,
                margin=dict(t=50, b=50, l=50, r=50),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.info("Radar chart will be available after data processing")
            print(f"Radar chart error: {str(e)}")

    def _render_trigger_blueprint(self, master_analytics: Dict, responses: Dict):
        """Trigger sequence with personalization"""
        st.markdown("## Your behavioral blueprint")
        st.caption("This is YOUR unique sequence - memorize this pattern")
        
        try:
            trigger_analysis = master_analytics.get('trigger_sequence', {})
            sequence = trigger_analysis.get('trigger_sequence', {})
            completeness = trigger_analysis.get('sequence_completeness', 0)
            
            st.markdown(f"**Sequence completeness:** {completeness}%")
            st.progress(completeness / 100)
            
            if completeness < 50:
                st.warning("We'll complete your trigger sequence mapping in session 1")
                return
            
            st.markdown("---")
            st.markdown("### Your automatic behavioral sequence")
            
            sequence_steps = [
                ('environmental_trigger', '🎯 Trigger', 'What starts it'),
                ('physical_response', '💓 Physical', 'Body sensations'),
                ('automatic_thought', '💭 Thought', 'Mental response'),
                ('emotional_response', '😰 Emotion', 'Feelings activated'),
                ('behavioral_response', '🎬 Behavior', 'What you do'),
                ('immediate_consequence', '📊 Result', 'What happens next')
            ]
            
            for key, icon_title, description in sequence_steps:
                value = sequence.get(key, 'Not yet captured')
                
                if value != 'Not yet captured':
                    with st.container():
                        st.markdown(f"**{icon_title}**")
                        st.caption(description)
                        st.info(value)
            
            intervention_windows = trigger_analysis.get('intervention_windows', [])
            if intervention_windows:
                st.markdown("---")
                st.markdown("### 🎯 Intervention opportunities")
                st.success("These are the moments where you can interrupt and choose differently:")
                
                for window in intervention_windows:
                    if isinstance(window, dict):
                        st.markdown(f"✅ {window.get('point', window)}")
                    else:
                        st.markdown(f"✅ {window}")
            
        except Exception as e:
            st.warning("Complete trigger blueprint will be mapped in session 1")
            print(f"Trigger blueprint error: {str(e)}")

    def _render_personalized_techniques(self, master_analytics: Dict, responses: Dict):
        """ENHANCED: Personalized techniques from trigger sequence + responses"""
        st.markdown("## 🛠️ Your personalized intervention techniques")
        st.caption("Start using these today - designed for YOUR specific patterns")
        
        try:
            trigger_analysis = master_analytics.get('trigger_sequence', {})
            sequence = trigger_analysis.get('trigger_sequence', {})
            pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            dominant = pattern_hierarchy.get('dominant_pattern', {})
            
            automatic_thought = self._extract_response_text(responses, 37)
            physical_response = sequence.get('physical_response', '')
            behavioral_response = sequence.get('behavioral_response', '')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Somatic intervention")
                st.markdown(f"""
                <div class="action-item">
                    <strong>When you notice: "{physical_response or 'physical tension'}"</strong><br><br>
                    <strong>Immediate response:</strong><br>
                    1. <strong>STOP</strong> - Freeze your body exactly as it is<br>
                    2. <strong>BREATHE</strong> - 4 counts in, 6 counts out (3 times)<br>
                    3. <strong>SCAN</strong> - Notice sensation without judgment<br>
                    4. <strong>RELEASE</strong> - Consciously relax that area<br>
                    5. <strong>GROUND</strong> - Feel feet on floor, present moment<br><br>
                    <em>This interrupts the automatic chain before thoughts cascade</em>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### Cognitive reframe")
                
                if automatic_thought:
                    reframed = self._reframe_automatic_thought(automatic_thought)
                    st.markdown(f"""
                    <div class="action-item">
                        <strong>Old automatic thought:</strong><br>
                        "{automatic_thought[:100]}..."<br><br>
                        <strong>Your new response:</strong><br>
                        "{reframed}"<br><br>
                        <strong>Practice:</strong><br>
                        Say the new response OUT LOUD 3 times daily,<br>
                        even when not triggered<br><br>
                        <em>This builds new neural pathways</em>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="action-item">
                        <strong>The PAUSE protocol:</strong><br><br>
                        <strong>P</strong> - Pause what you're doing<br>
                        <strong>A</strong> - Acknowledge the pattern<br>
                        <strong>U</strong> - Understand it's protecting you<br>
                        <strong>S</strong> - Select a new response<br>
                        <strong>E</strong> - Execute with compassion<br><br>
                        <em>Practice this 2-3 times daily, even when calm</em>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("### Behavioral substitution")
            
            if behavioral_response:
                alternative = self._generate_alternative_behavior(behavioral_response)
                st.markdown(f"""
                <div class="action-item">
                    <strong>Old automatic behavior:</strong><br>
                    "{behavioral_response}"<br><br>
                    <strong>Your new alternative:</strong><br>
                    "{alternative}"<br><br>
                    <strong>Implementation:</strong><br>
                    • Prepare this response in advance<br>
                    • Visualize yourself doing it successfully<br>
                    • Start with easiest situations first<br>
                    • Celebrate ANY attempt, even imperfect<br><br>
                    <em>New behaviors feel awkward at first - this is normal</em>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("### Pattern-specific mastery technique")
            pattern_technique = self._get_pattern_specific_technique(dominant.get('id'))
            st.markdown(f"""
            <div class="action-item">
                {pattern_technique}
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.warning("Detailed techniques will be provided in session 1")
            print(f"Personalized techniques error: {str(e)}")

    def _render_integrated_session_roadmap(self, master_analytics: Dict):
        """Session roadmap"""
        st.markdown("## Your transformation timeline")
        st.caption("Session-by-session roadmap with integrated interventions")
        
        try:
            session_prediction = master_analytics.get('session_prediction', {})
            session_structure = session_prediction.get('session_structure', {})
            detailed_planning = session_prediction.get('detailed_planning', {})
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                sessions = session_structure.get('total_sessions', '2 sessions')
                st.metric("Total sessions", sessions)
            
            with col2:
                duration = session_structure.get('session_length', '90 minutes')
                st.metric("Session length", duration)
            
            with col3:
                timeline = session_structure.get('timeline', '2-3 weeks')
                st.metric("Total timeline", timeline)
            
            st.markdown("---")
            
            st.markdown("### Session 1: foundation and pattern mapping")
            st.markdown("**Duration:** 90 minutes")
            
            session1_plan = detailed_planning.get('session_1', '')
            st.write(session1_plan)
            
            st.markdown("### Session 2: deep transformation and integration")
            st.markdown("**Duration:** 90 minutes")
            
            session2_plan = detailed_planning.get('session_2', '')
            st.write(session2_plan)
            
        except Exception as e:
            st.warning("Detailed session planning will be provided after consultation")
            print(f"Session roadmap error: {str(e)}")

    def _render_personalized_success_tracking(self, master_analytics: Dict, responses: Dict):
        """Success metrics"""
        st.markdown("## 📊 Your personalized success metrics")
        st.caption("Track these specific milestones from YOUR vision")
        
        try:
            first_action = self._extract_response_text(responses, 74)
            future_vision = self._extract_response_text(responses, 75)
            impact_area = self._extract_response_text(responses, 76)
            
            success_prediction = master_analytics.get('success_prediction', {})
            
            if first_action:
                st.markdown("### Week 1 milestone")
                st.markdown(f"""
                <div class="success-indicator">
                    <strong>Your immediate win:</strong><br>
                    "{first_action[:200]}"<br><br>
                    ✓ Track: Have you attempted this action?<br>
                    ✓ Success = Any attempt, even imperfect
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("### Your transformation likelihood")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                success_rate = success_prediction.get('overall_success_rate', 85)
                st.metric("Success probability", f"{success_rate}%")
            
            with col2:
                timeline = success_prediction.get('timeline_estimate', '2-3 weeks')
                st.metric("Expected timeline", timeline)
            
            with col3:
                tier = success_prediction.get('success_tier', 'High')
                st.metric("Confidence level", tier)
            
        except Exception as e:
            st.warning("Personalized metrics will be created in session 1")
            print(f"Personalized success tracking error: {str(e)}")

    def _render_transformation_assets(self, master_analytics: Dict, responses: Dict):
        """What you bring to transformation - empowerment section"""
        st.markdown("## 💎 Your transformation assets")
        st.caption("The strengths you already have for this journey")
        
        try:
            quality = master_analytics.get('assessment_quality', {})
            pattern_hierarchy = master_analytics.get('pattern_hierarchy', {})
            
            assets = []
            
            completion_rate = quality.get('completion_rate', 0)
            if completion_rate >= 90:
                assets.append("**High commitment:** Your 90%+ assessment completion shows dedication to change")
            
            pattern_count = pattern_hierarchy.get('pattern_count', 0)
            if pattern_count >= 3:
                assets.append("**Strong self-awareness:** You recognize multiple patterns - awareness is 60% of the work")
            
            if len(assets) < 4:
                assets.extend([
                    "**Courage:** You're here, seeking help - that takes strength",
                    "**Intelligence:** You're approaching this systematically and thoughtfully",
                    "**Neuroplasticity:** Your brain can rewire at any age - science proves it"
                ])
            
            st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
            for asset in assets[:6]:
                st.markdown(f"✓ {asset}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.success("""
            **You have everything needed for transformation.**  
            These patterns developed to protect you - they served a purpose. Now you're ready 
            to update them consciously. Your awareness, commitment, and readiness position you 
            for rapid, lasting change.
            """)
            
        except Exception as e:
            st.info("Your transformation assets will be identified in consultation")
            print(f"Transformation assets error: {str(e)}")


def create_behavioral_blueprint():
    """Factory function"""
    return BehavioralBlueprint()
