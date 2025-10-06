"""
Blueprint Component - Premium Clinical Analysis (Production Ready)
Complete implementation with error handling and validation
"""

import streamlit as st
from typing import Dict, Optional, List, Tuple
from datetime import datetime
import plotly.graph_objects as go


class BehavioralBlueprint:
    """Renders complete clinical blueprint - production ready"""

    def __init__(self):
        self.pattern_names = {
            1: "Unhappiness culture", 2: "Power struggles", 3: "Systematic mistrust",
            4: "Separation and division", 5: "Doing versus being", 
            6: "Compartmentalized authenticity", 7: "Self sacrifice and care avoidance",
            8: "Inherited missions", 9: "Context dependent weakness"
        }
        self._apply_print_friendly_styles()

    def _apply_print_friendly_styles(self):
        """Styles optimized for both screen and print/PDF"""
        st.markdown("""
            <style>
            @media print {
                .stButton, .stDownloadButton { display: none; }
                .insight-card { page-break-inside: avoid; }
            }
            
            .insight-card {
                background: #ffffff;
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
                text-align: center;
                font-size: 1.1rem;
                font-weight: 600;
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
            
            .cost-comparison {
                background: linear-gradient(135deg, #F3F6F8 0%, #ffffff 100%);
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
            }
            </style>
        """, unsafe_allow_html=True)
    
    def render_complete_blueprint(self, assessment_data: Dict):
        """Render complete premium blueprint with error handling"""
        
        try:
            master_analytics = assessment_data.get('master_analytics', {})
            
            if not master_analytics:
                st.error("Analysis data not available. Please complete assessment first.")
                return
            
            # Header with download buttons
            self._render_blueprint_header(assessment_data)
            
            # Table of contents
            self._render_table_of_contents()
            
            # 1. Personal cover page
            self._render_cover_page(assessment_data)
            
            # 2. Quick reference card
            self._render_quick_reference_card(master_analytics)
            
            # # 3. Executive summary
            # self._render_executive_summary(master_analytics)
            
            # 4. Personal mantras
            self._render_personal_mantras(master_analytics)
            
            # 5. Complete pattern analysis with radar chart
            self._render_pattern_constellation(master_analytics)
            
            # 6. Behavioral blueprint (trigger sequence)
            self._render_trigger_blueprint(master_analytics)
            
            # 7. Immediate action techniques
            self._render_immediate_techniques(master_analytics)
            
            # 8. Session roadmap
            self._render_session_roadmap(master_analytics)
            
            # 9. Success tracking
            self._render_success_tracking(master_analytics)
            
            # # 10. Investment analysis
            # self._render_investment_analysis(master_analytics)
            
            # 11. Downloadable resources
            self._render_downloadable_resources(master_analytics)
            
        except Exception as e:
            st.error(f"Error rendering blueprint: {str(e)}")
            st.info("Please contact support if this issue persists.")
            print(f"Blueprint rendering error: {str(e)}")
    
    def _render_blueprint_header(self, assessment_data: Dict):
        """Render header with download options"""
        st.markdown("### Your complete transformation blueprint")
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.caption("Complete clinical analysis with actionable techniques")
        
        with col2:
            try:
                markdown_content = self._generate_markdown_report(assessment_data)
                st.download_button(
                    label="Download as text",
                    data=markdown_content,
                    file_name=f"transformation_blueprint_{datetime.now().strftime('%Y%m%d')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            except Exception as e:
                st.button("Download text", disabled=True, use_container_width=True)
                print(f"Download generation error: {str(e)}")
        
        with col3:
        # PDF download - NOW WORKING
            try:
                pdf_bytes = self._generate_pdf_report(assessment_data)
                if pdf_bytes:
                    st.download_button(
                        label="Download PDF",
                        data=pdf_bytes,
                        file_name=f"transformation_blueprint_{datetime.now().strftime('%Y%m%d')}.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        type="primary"
                    )
                else:
                    st.button("Download PDF", disabled=True, use_container_width=True)
                    st.caption("*(Generation failed)*")
            except Exception as e:
                st.button("Download PDF", disabled=True, use_container_width=True)
                st.caption("*(Install xhtml2pdf)*")
        
        st.markdown("---")
    
    def _render_executive_summary(self, master_analytics: Dict):
        """Executive summary with key metrics and insights"""
        st.markdown("## Executive summary")
        st.caption("Your transformation at a glance")
        
        try:
            pattern_analysis = master_analytics.get('pattern_analysis', {})
            success_prediction = master_analytics.get('success_prediction', {})
            digital_analysis = master_analytics.get('digital_analysis')
            
            # Key metrics row
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                pattern_count = pattern_analysis.get('pattern_count', 0)
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 2rem; color: #4CA1A3; font-weight: bold;">{pattern_count}</div>
                    <div style="color: #556D7A; font-size: 0.9rem;">Patterns identified</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                success_rate = success_prediction.get('overall_success_rate', 85)
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 2rem; color: #22c55e; font-weight: bold;">{success_rate}%</div>
                    <div style="color: #556D7A; font-size: 0.9rem;">Success rate</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                timeline = success_prediction.get('timeline_estimate', '2-3 weeks')
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 1.5rem; color: #4CA1A3; font-weight: bold;">{timeline}</div>
                    <div style="color: #556D7A; font-size: 0.9rem;">Timeline</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                sessions = success_prediction.get('recommended_sessions', 2)
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 2rem; color: #4CA1A3; font-weight: bold;">{sessions}</div>
                    <div style="color: #556D7A; font-size: 0.9rem;">Sessions needed</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Dominant pattern analysis
            dominant = pattern_analysis.get('dominant_pattern', {})
            if dominant:
                st.markdown("### Primary pattern analysis")
                
                pattern_name = dominant.get('name', 'Unknown pattern')
                pattern_score = dominant.get('score', 0)
                pattern_desc = dominant.get('description', {})
                
                st.markdown(f"""
                <div class="insight-card">
                    <h4 style="color: #4CA1A3; margin-bottom: 0.5rem;">{pattern_name}</h4>
                    <p style="color: #273548; margin-bottom: 0.5rem;"><strong>Intensity:</strong> {pattern_score:.1f}/10</p>
                    <p style="color: #556D7A; margin-bottom: 0.5rem;">
                        <strong>Core belief:</strong> {pattern_desc.get('core_belief', 'Pattern analysis in progress')}
                    </p>
                    <p style="color: #556D7A;">
                        <strong>Impact:</strong> {pattern_desc.get('impact', 'This pattern affects your daily functioning')}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Digital analysis if applicable
            if digital_analysis and digital_analysis.get('severity_level') != 'MINIMAL':
                severity = digital_analysis.get('severity_level', 'UNKNOWN')
                score = digital_analysis.get('digital_despair_score', 0)
                
                st.markdown("### Digital conditioning analysis")
                st.info(f"""
                **Level:** {severity} ({score:.0f}% digital despair score)
                
                Specialized digital-native protocols activated. Your assessment shows patterns 
                common in digitally-conditioned psychology, requiring adapted therapeutic approach.
                """)
            
            # Complexity assessment
            complexity = pattern_analysis.get('complexity_assessment', 'Standard')
            st.markdown(f"""
            **Complexity level:** {complexity}  
            **Intervention approach:** {self._get_complexity_description(complexity)}
            """)
            
        except Exception as e:
            st.warning("Executive summary partially unavailable")
            st.info("Core metrics will be available after clinical review")
            print(f"Executive summary error: {str(e)}")
    
    def _get_complexity_description(self, complexity: str) -> str:
        """Get description for complexity level"""
        descriptions = {
            'Simple': 'Focused intervention targeting single dominant pattern',
            'Standard': 'Comprehensive approach addressing primary pattern constellation',
            'Moderate': 'Integrated approach for multiple interacting patterns',
            'Complex': 'Sophisticated multi-layered intervention with careful sequencing',
            'High': 'Advanced protocol with extended integration support'
        }
        return descriptions.get(complexity, 'Personalized therapeutic approach')
    
    def _render_pattern_constellation(self, master_analytics: Dict):
        """Pattern analysis with radar chart visualization"""
        st.markdown("## Complete pattern analysis")
        st.caption("Your unique behavioral pattern constellation")
        
        try:
            pattern_analysis = master_analytics.get('pattern_analysis', {})
            pattern_scores = pattern_analysis.get('pattern_scores', {})
            
            if not pattern_scores:
                st.info("Pattern analysis will be available after session 1")
                return
            
            # Create radar chart
            self._render_pattern_radar_chart(pattern_scores)
            
            st.markdown("---")
            
            # Detailed pattern breakdown
            st.markdown("### Pattern intensity breakdown")
            
            # Sort patterns by intensity
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
                    
                    # Add brief description
                    st.caption(self._get_pattern_brief_description(pattern_id))
                    st.markdown("")
            
            # Pattern interactions
            if len(sorted_patterns) >= 2:
                st.markdown("### Pattern interactions")
                st.info("""
                Your patterns don't operate in isolation - they interact and reinforce each other. 
                Understanding these connections is key to breaking the cycle.
                """)
                
                dominant = pattern_analysis.get('dominant_pattern', {})
                primary = pattern_analysis.get('primary_patterns', [])
                
                if dominant and primary:
                    interaction = self._describe_pattern_interaction(
                        dominant.get('id'), 
                        primary[0].get('id') if primary else None
                    )
                    st.markdown(f"""
                    <div class="insight-card">
                        {interaction}
                    </div>
                    """, unsafe_allow_html=True)
            
        except Exception as e:
            st.warning("Pattern visualization temporarily unavailable")
            st.info("Complete pattern analysis will be provided in session 1")
            print(f"Pattern constellation error: {str(e)}")
    
    def _render_pattern_radar_chart(self, pattern_scores: Dict):
        """Render radar chart of pattern intensities"""
        try:
            # Prepare data
            categories = []
            values = []
            
            for pattern_id in range(1, 10):
                pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                score = pattern_scores.get(pattern_id, 0)
                categories.append(pattern_name)
                values.append(score)
            
            # Create radar chart
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
                        tickfont=dict(size=11)
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
            st.info("Radar chart visualization will be available after data processing")
            print(f"Radar chart error: {str(e)}")
    
    def _get_pattern_brief_description(self, pattern_id: int) -> str:
        """Get brief description for pattern"""
        descriptions = {
            1: "Difficulty accepting and maintaining positive emotional states",
            2: "Recurring conflicts and defensive responses in relationships",
            3: "Default skepticism about others' intentions and motivations",
            4: "Black-and-white thinking that limits creative solutions",
            5: "Self-worth tied to productivity and achievement",
            6: "Different selves in different contexts, lacking integration",
            7: "Prioritizing others' needs while neglecting self-care",
            8: "Life choices driven by family expectations vs personal desires",
            9: "Boundaries and limits varying dramatically by context"
        }
        return descriptions.get(pattern_id, "Pattern affects daily functioning")
    
    def _describe_pattern_interaction(self, pattern1_id: Optional[int], pattern2_id: Optional[int]) -> str:
        """Describe how two patterns interact and reinforce each other"""
        if not pattern1_id or not pattern2_id:
            return "Your patterns interact in complex ways that will be mapped in session 1"
        
        # Some common interactions
        interactions = {
            (1, 5): "Your unhappiness culture reinforces your achievement addiction - you push harder thinking success will finally allow happiness, but the underlying belief prevents enjoyment.",
            (2, 3): "Power struggles emerge from systematic mistrust - when you assume negative intentions, you enter conversations defensively, creating the conflict you feared.",
            (3, 6): "Systematic mistrust drives compartmentalized authenticity - you show different selves because you don't trust anyone to accept your real self.",
            (5, 7): "Achievement addiction and self-sacrifice combine dangerously - you serve others compulsively to prove your worth, depleting yourself entirely.",
            (1, 3): "Unhappiness culture and mistrust create a closed loop - you expect the worst, so you don't trust good things, confirming your negative beliefs.",
            (4, 5): "Binary thinking intensifies achievement pressure - life becomes 'extraordinary success or complete failure' with no middle ground.",
            (6, 9): "Compartmentalized authenticity and context-dependent weakness overlap - you lose yourself in certain contexts because there's no integrated authentic self.",
            (7, 8): "Self-sacrifice for inherited missions is double-binding - you neglect yourself while fulfilling someone else's dream.",
            (2, 9): "Power struggles in specific contexts reveal where your boundaries collapse - these are often the same situations/people."
        }
        
        # Check both orderings
        interaction = interactions.get((pattern1_id, pattern2_id)) or interactions.get((pattern2_id, pattern1_id))
        
        if interaction:
            return interaction
        
        # Generic interaction description
        p1_name = self.pattern_names.get(pattern1_id, "your primary pattern")
        p2_name = self.pattern_names.get(pattern2_id, "your secondary pattern")
        return f"Your {p1_name} and {p2_name} patterns interact and reinforce each other in ways we'll explore in detail during session 1."
    
    def _render_trigger_blueprint(self, master_analytics: Dict):
        """Render complete trigger chain analysis"""
        st.markdown("## Your behavioral blueprint")
        st.caption("This is YOUR unique sequence - memorize this pattern")
        
        try:
            trigger_analysis = master_analytics.get('trigger_chain_analysis', {})
            
            if not trigger_analysis:
                st.info("Complete trigger sequence will be mapped in session 1")
                return
            
            sequence = trigger_analysis.get('trigger_sequence', {})
            completeness = trigger_analysis.get('sequence_completeness', 0)
            
            # Completeness indicator
            st.markdown(f"""
            **Sequence completeness:** {completeness}%
            """)
            st.progress(completeness / 100)
            
            if completeness < 50:
                st.warning("We'll complete your trigger sequence mapping in session 1")
                return
            
            st.markdown("---")
            
            # Visual sequence flow
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
                    st.markdown(f"""
                    <div class="insight-card">
                        <h4 style="color: #4CA1A3; margin-bottom: 0.5rem;">{icon_title}</h4>
                        <p style="color: #556D7A; font-size: 0.9rem; margin-bottom: 0.5rem;">{description}</p>
                        <p style="color: #273548; font-weight: 500;">{value}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: #F3F6F8; padding: 1rem; border-radius: 6px; margin: 0.5rem 0;">
                        <p style="color: #556D7A;"><strong>{icon_title}:</strong> {description} - Will be identified in session 1</p>
                    </div>
                    """)
            
            # Intervention points
            intervention_windows = trigger_analysis.get('intervention_windows', [])
            if intervention_windows:
                st.markdown("---")
                st.markdown("### 🎯 Intervention opportunities")
                st.success("""
                These are the moments where you can interrupt your automatic pattern 
                and choose a different response:
                """)
                
                for window in intervention_windows:
                    st.markdown(f"✅ {window}")
            
        except Exception as e:
            st.warning("Trigger blueprint will be completed in session 1")
            st.info("Your complete behavioral sequence will be mapped during our first meeting")
            print(f"Trigger blueprint error: {str(e)}")
    
    def _render_session_roadmap(self, master_analytics: Dict):
        """Render detailed session-by-session roadmap"""
        st.markdown("## Your transformation timeline")
        st.caption("Session-by-session breakdown of your journey")
        
        try:
            session_planning = master_analytics.get('session_planning', {})
            
            if not session_planning:
                st.info("Detailed session planning will be created after assessment review")
                return
            
            session_structure = session_planning.get('session_structure', {})
            detailed_planning = session_planning.get('detailed_planning', {})
            
            # Timeline overview
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
            
            # Session 1 details
            st.markdown("### Session 1: Pattern mapping & rapport building")
            st.markdown("**Duration:** 90 minutes")
            
            session1_plan = detailed_planning.get('session_1', '')
            
            st.markdown(f"""
            <div class="session-card">
                <h4 style="color: #4CA1A3; margin-bottom: 1rem;">Core objectives</h4>
                <p style="color: #273548; margin-bottom: 1rem;">{session1_plan}</p>
                
                <h4 style="color: #4CA1A3; margin-bottom: 0.5rem;">What to expect</h4>
                <ul style="color: #556D7A; line-height: 1.8;">
                    <li>Complete behavioral chain mapping</li>
                    <li>Subconscious pattern identification</li>
                    <li>Initial positive programming and preparation</li>
                    <li>Therapeutic alliance establishment</li>
                    <li>You'll leave with clarity about your patterns</li>
                </ul>
                
                <h4 style="color: #4CA1A3; margin-top: 1rem; margin-bottom: 0.5rem;">How to prepare</h4>
                <ul style="color: #556D7A; line-height: 1.8;">
                    <li>Review this blueprint beforehand</li>
                    <li>Note any recent pattern occurrences</li>
                    <li>Come with specific examples if possible</li>
                    <li>Be ready to explore origins openly</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Session 2 details
            st.markdown("### Session 2: Neural rewiring & integration")
            st.markdown("**Duration:** 90 minutes")
            
            session2_plan = detailed_planning.get('session_2', '')
            
            st.markdown(f"""
            <div class="session-card">
                <h4 style="color: #4CA1A3; margin-bottom: 1rem;">Core objectives</h4>
                <p style="color: #273548; margin-bottom: 1rem;">{session2_plan}</p>
                
                <h4 style="color: #4CA1A3; margin-bottom: 0.5rem;">What to expect</h4>
                <ul style="color: #556D7A; line-height: 1.8;">
                    <li>Deep hypnotic state for direct subconscious access</li>
                    <li>Pattern interruption at neural level</li>
                    <li>New response pathway installation</li>
                    <li>Behavioral anchoring and testing</li>
                    <li>You'll notice shifts within 48-72 hours</li>
                </ul>
                
                <h4 style="color: #4CA1A3; margin-top: 1rem; margin-bottom: 0.5rem;">Between sessions</h4>
                <ul style="color: #556D7A; line-height: 1.8;">
                    <li>Practice pattern awareness daily</li>
                    <li>Use intervention techniques from session 1</li>
                    <li>Track your responses and wins</li>
                    <li>Notice any shifts in automatic reactions</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Session 3 if needed
            session3_plan = detailed_planning.get('session_3')
            if session3_plan and 'unlikely' not in session3_plan.lower():
                st.markdown("### Session 3: Integration & reinforcement (if needed)")
                st.markdown("**Duration:** 60 minutes")
                
                st.markdown(f"""
                <div class="session-card">
                    <h4 style="color: #4CA1A3; margin-bottom: 1rem;">Core objectives</h4>
                    <p style="color: #273548; margin-bottom: 1rem;">{session3_plan}</p>
                    
                    <p style="color: #556D7A; margin-top: 1rem;">
                        <strong>Note:</strong> Only about 15% of clients need this reinforcement session. 
                        Most find complete transformation in 2 sessions. This is available if needed for 
                        complex pattern integration.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
        except Exception as e:
            st.warning("Detailed session roadmap will be provided after clinical review")
            
            # Provide basic timeline
            st.markdown("""
            ### Standard transformation timeline
            
            **Session 1 (90 min):** Complete pattern mapping and initial programming  
            **Session 2 (90 min):** Deep neural rewiring and integration  
            **Session 3 (60 min):** Optional reinforcement if needed (15% of clients)  
            
            **Total timeline:** 2-3 weeks for complete transformation
            """)
            
            print(f"Session roadmap error: {str(e)}")
    
    def _render_investment_analysis(self, master_analytics: Dict = None):
        """Render comprehensive ROI and investment analysis"""
        st.markdown("## Investment analysis")
        st.caption("Understanding the true cost of change vs. staying the same")
        
        try:
            # Cost comparison section
            st.markdown("### Approach comparison")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="cost-comparison">
                    <h4 style="color: #556D7A; margin-bottom: 1rem;">Traditional therapy</h4>
                    <ul style="color: #273548; line-height: 1.8;">
                        <li><strong>Duration:</strong> 18-24 months</li>
                        <li><strong>Sessions:</strong> 40-60+ sessions</li>
                        <li><strong>Investment:</strong> ฿15,000 - ฿25,000+</li>
                        <li><strong>Time to results:</strong> 3-6 months</li>
                        <li><strong>Success rate:</strong> 30-40%</li>
                    </ul>
                    <p style="color: #556D7A; margin-top: 1rem; font-style: italic;">
                        Gradual conscious mind work with talk therapy
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="cost-comparison" style="border: 2px solid #4CA1A3;">
                    <h4 style="color: #4CA1A3; margin-bottom: 1rem;">Rapid transformation hypnotherapy</h4>
                    <ul style="color: #273548; line-height: 1.8;">
                        <li><strong>Duration:</strong> 2-3 weeks</li>
                        <li><strong>Sessions:</strong> 2-3 specialized sessions</li>
                        <li><strong>Investment:</strong> ฿3,000 - ฿4,000</li>
                        <li><strong>Time to results:</strong> 48-72 hours</li>
                        <li><strong>Success rate:</strong> 85%+</li>
                    </ul>
                    <p style="color: #4CA1A3; margin-top: 1rem; font-weight: 600;">
                        Direct subconscious rewiring through hypnosis
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Cost of unchanged patterns
            st.markdown("### 5-year cost of unchanged patterns")
            
            cost_analysis = {}
            if master_analytics:
                cost_analysis = master_analytics.get('cost_analysis', {})
            
            if cost_analysis:
                annual_cost = cost_analysis.get('annual', {}).get('total', 0)
                five_year_cost = annual_cost * 5
                
                st.markdown(f"""
                <div class="insight-card">
                    <h4 style="color: #ef4444; margin-bottom: 1rem;">Hidden costs of staying the same</h4>
                    <ul style="color: #273548; line-height: 1.8;">
                        <li><strong>Annual opportunity cost:</strong> ~฿{annual_cost:,.0f}</li>
                        <li><strong>5-year projection:</strong> ~฿{five_year_cost:,.0f}</li>
                        <li><strong>Lost productivity:</strong> Significant</li>
                        <li><strong>Relationship strain:</strong> Immeasurable</li>
                        <li><strong>Quality of life impact:</strong> Substantial</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="insight-card">
                    <h4 style="color: #ef4444; margin-bottom: 1rem;">Hidden costs of staying the same</h4>
                    <ul style="color: #273548; line-height: 1.8;">
                        <li><strong>Lost productivity:</strong> ฿50,000 - ฿100,000 over 5 years</li>
                        <li><strong>Missed opportunities:</strong> Career advancement, relationships</li>
                        <li><strong>Quality of life:</strong> Ongoing stress and dissatisfaction</li>
                        <li><strong>Health impacts:</strong> Stress-related conditions</li>
                        <li><strong>Relationship costs:</strong> Strain on personal connections</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # ROI calculation
            st.markdown("### Return on investment")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Direct investment", "฿3,000-4,000", "One-time")
            
            with col2:
                st.metric("Expected ROI", "10-25x", "Over 5 years")
            
            with col3:
                st.metric("Time investment", "3-4.5 hours", "Total sessions")
            
            st.success("""
            **Most clients report:**
            - Improved work performance and productivity within weeks
            - Better relationships and communication immediately
            - Reduced stress and increased life satisfaction
            - Confidence and decision-making improvements
            - ROI that far exceeds the initial investment
            """)
            
            # Value beyond money
            st.markdown("---")
            st.markdown("### Value beyond the numbers")
            
            st.info("""
            **What price would you put on:**
            - Waking up without anxiety or dread?
            - Confident, authentic relationships?
            - Peace of mind and emotional freedom?
            - Living YOUR life, not someone else's expectations?
            - Becoming the person you know you can be?
            
            These transformations are priceless - yet achievable in just 2-3 sessions.
            """)
            
        except Exception as e:
            st.warning("Investment analysis will be personalized during consultation")
            st.info("Contact us for detailed cost-benefit analysis for your situation")
            print(f"Investment analysis error: {str(e)}")

    # Keep all your existing helper methods
    def _render_table_of_contents(self):
        """Table of contents - makes document feel comprehensive"""
        with st.expander("📋 **Table of contents**", expanded=False):
            st.markdown("""
            1. **Personal cover page** - Your transformation document
            2. **Quick reference card** - Daily reminder tool
            3. **Executive summary** - Key insights at a glance
            4. **Your personal mantras** - Empowering affirmations
            5. **Complete pattern analysis** - Detailed constellation
            6. **Your behavioral blueprint** - Trigger sequence map
            7. **Immediate action techniques** - Start using today
            8. **Session roadmap** - Your transformation timeline
            9. **Success tracking dashboard** - Measure your progress
            10. **Investment analysis** - ROI breakdown
            11. **Downloadable resources** - Worksheets and tools
            """)

    def _render_cover_page(self, assessment_data: Dict):
        """Personal cover page"""
        contact = assessment_data.get('contact_info', {})
        name = contact.get('full_name', 'Valued client')
        
        st.markdown(f"""
        # Complete transformation blueprint
        
        **Prepared exclusively for:** {name}  
        **Date:** {datetime.now().strftime('%B %d, %Y')}  
        **Document ID:** BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}
        
        ---
        
        *This personalized clinical analysis contains your unique behavioral patterns, 
        transformation roadmap, and actionable techniques for lasting change.*
        """)

    def _render_quick_reference_card(self, master_analytics: Dict):
        """Quick reference card"""
        st.markdown("## 🎯 Quick reference card")
        st.caption("Print this section and keep it visible")
        
        pattern_analysis = master_analytics.get('pattern_analysis', {})
        dominant = pattern_analysis.get('dominant_pattern', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Your primary pattern")
            if dominant:
                st.info(f"**{dominant.get('name', 'Unknown')}**\n\nIntensity: {dominant.get('score', 0):.1f}/10")
            
            st.markdown("### When you notice it starting:")
            st.success("""
            1. **PAUSE** - Take 3 deep breaths
            2. **NAME** - "This is my [pattern] pattern"
            3. **CHOOSE** - "I can respond differently"
            """)
        
        with col2:
            st.markdown("### Your intervention phrase")
            pattern_id = dominant.get('id')
            intervention_phrase = self._get_intervention_phrase(pattern_id)
            st.markdown(f"""
            <div class="mantra-box">
                "{intervention_phrase}"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### Emergency support")
            st.markdown("""
            - **Crisis hotline:** 1323 (24/7)
            - **Your therapist:** [Contact after consultation]
            - **Session materials:** Keep this document handy
            """)

    def _render_personal_mantras(self, master_analytics: Dict):
        """Personal empowering mantras"""
        st.markdown("## 💪 Your personal transformation mantras")
        st.caption("Read these daily - designed specifically for YOUR patterns")
        
        pattern_analysis = master_analytics.get('pattern_analysis', {})
        dominant = pattern_analysis.get('dominant_pattern', {})
        primary_patterns = pattern_analysis.get('primary_patterns', [])
        
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
                {i}. {mantra}
            </div>
            """, unsafe_allow_html=True)

    def _get_pattern_mantra(self, pattern_id: Optional[int]) -> str:
        """Get empowering mantra for specific pattern"""
        if pattern_id is None or pattern_id not in range(1, 10):
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
            9: "My boundaries remain consistent across all contexts and people"
        }
        return mantras.get(pattern_id, "I am capable of transformation and growth")

    def _get_intervention_phrase(self, pattern_id: Optional[int]) -> str:
        """Get specific intervention phrase"""
        if pattern_id is None or pattern_id not in range(1, 10):
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
            9: "Consistent boundaries, confident self"
        }
        return phrases.get(pattern_id, "I choose a new response")

    def _render_immediate_techniques(self, master_analytics: Dict):
        """Actionable techniques for today"""
        st.markdown("## 🛠️ Immediate action techniques")
        st.caption("Start using these today - before your first session")
        
        pattern_analysis = master_analytics.get('pattern_analysis', {})
        dominant = pattern_analysis.get('dominant_pattern', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Pattern interruption technique")
            st.markdown("""
            <div class="action-item">
                <strong>The 5-4-3-2-1 grounding method:</strong><br><br>
                When you notice your pattern starting:<br>
                • Name 5 things you SEE<br>
                • Name 4 things you FEEL<br>
                • Name 3 things you HEAR<br>
                • Name 2 things you SMELL<br>
                • Name 1 thing you TASTE<br><br>
                <em>This interrupts automatic patterns and returns you to present moment</em>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Alternative response practice")
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
        
        st.markdown("### Your pattern-specific technique")
        pattern_technique = self._get_pattern_specific_technique(dominant.get('id'))
        st.markdown(f"""
        <div class="action-item">
            {pattern_technique}
        </div>
        """, unsafe_allow_html=True)

    def _get_pattern_specific_technique(self, pattern_id: Optional[int]) -> str:
        """Get specific technique for each pattern"""
        if pattern_id is None or pattern_id not in range(1, 10):
            return "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it: 'There's my pattern.' Breathe. Choose one small different response."
        
        techniques = {
            1: "<strong>Happiness permission practice:</strong><br>When something good happens, say out loud: 'I deserve this and it's safe to enjoy it.' Repeat 3 times. Notice any resistance and breathe through it.",
            2: "<strong>Curiosity reframe:</strong><br>When you feel defensive, say: 'I'm curious about their perspective.' Take 3 breaths. Ask: 'Tell me more about what you're thinking?'",
            3: "<strong>Discernment check:</strong><br>When suspicion arises, ask: 'What evidence do I actually have?' Then: 'What would trust look like here?' Choose one small trust action.",
            4: "<strong>Both/and thinking:</strong><br>When facing a decision, complete: 'Instead of choosing X OR Y, what if I could have aspects of X AND Y by...' List 3 creative options.",
            5: "<strong>Being practice:</strong><br>Set timer for 5 minutes. Sit quietly. Every time you think 'I should be doing something', respond: 'Right now, being is enough.'",
            6: "<strong>Authenticity anchor:</strong><br>Before entering any situation, touch your heart and say: 'Same me, every context.' Notice one authentic choice you can make.",
            7: "<strong>Boundary affirmation:</strong><br>When asked for something, pause. Feel your body. Ask: 'Do I genuinely want to do this?' Honor the answer with 'yes' or 'not right now.'",
            8: "<strong>Path clarification:</strong><br>Daily ask: 'If no one would know, judge, or be disappointed, what would I choose?' Write the answer. This reveals YOUR path.",
            9: "<strong>Consistent self practice:</strong><br>Identify your 'difficult person/context.' Practice saying 'no' to small requests there. Notice you remain whole and safe."
        }
        return techniques.get(pattern_id, "<strong>Pattern awareness:</strong><br>Notice when your pattern activates. Name it: 'There's my pattern.' Breathe. Choose one small different response.")

    def _render_success_tracking(self, master_analytics: Dict):
        """Success tracking dashboard"""
        st.markdown("## 📊 Success tracking dashboard")
        st.caption("Use this to measure your transformation - track weekly")
        
        st.markdown("### Weekly check-in questions")
        
        tracking_questions = [
            "How many times did I notice my pattern before it fully activated?",
            "How many times did I choose a different response?",
            "What was my biggest win this week?",
            "What challenge taught me the most?",
            "On a scale 1-10, how empowered do I feel?"
        ]
        
        for question in tracking_questions:
            st.checkbox(question, key=f"track_{hash(question)}")
        
        st.markdown("### Progress indicators to watch")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Early wins (Week 1-2):**")
            st.markdown("""
            - Catching pattern earlier
            - Pausing before automatic response
            - One successful intervention
            - Increased self-awareness
            - Feeling hopeful about change
            """)
        
        with col2:
            st.markdown("**Transformation markers (Week 3-4):**")
            st.markdown("""
            - New responses feeling natural
            - Others noticing differences
            - Reduced pattern frequency
            - Increased life satisfaction
            - Sustained positive changes
            """)

    def _generate_pdf_report(self, assessment_data: Dict) -> bytes:
        """Generate PDF report from blueprint content"""
        try:
            from xhtml2pdf import pisa
            from io import BytesIO
            
            master_analytics = assessment_data.get('master_analytics', {})
            contact = assessment_data.get('contact_info', {})
            name = contact.get('full_name', 'Valued Client')
            
            pattern_analysis = master_analytics.get('pattern_analysis', {})
            dominant = pattern_analysis.get('dominant_pattern', {})
            success_prediction = master_analytics.get('success_prediction', {})
            primary_patterns = pattern_analysis.get('primary_patterns', [])
            
            # Create HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    @page {{
                        size: A4;
                        margin: 2cm;
                    }}
                    body {{
                        font-family: Arial, sans-serif;
                        line-height: 1.6;
                        color: #273548;
                    }}
                    h1 {{
                        color: #4CA1A3;
                        border-bottom: 3px solid #4CA1A3;
                        padding-bottom: 10px;
                    }}
                    h2 {{
                        color: #4CA1A3;
                        margin-top: 30px;
                    }}
                    .cover {{
                        text-align: center;
                        margin-top: 100px;
                        page-break-after: always;
                    }}
                    .metric {{
                        background: #F3F6F8;
                        padding: 15px;
                        border-radius: 8px;
                        margin: 10px 0;
                        border-left: 4px solid #4CA1A3;
                    }}
                    .mantra {{
                        background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
                        color: white;
                        padding: 20px;
                        border-radius: 12px;
                        margin: 15px 0;
                        text-align: center;
                        font-weight: bold;
                    }}
                    .technique {{
                        background: #E1F0F0;
                        padding: 15px;
                        border-radius: 8px;
                        margin: 10px 0;
                        border-left: 3px solid #22c55e;
                    }}
                    .page-break {{
                        page-break-before: always;
                    }}
                </style>
            </head>
            <body>
                <!-- Cover Page -->
                <div class="cover">
                    <h1>Complete Transformation Blueprint</h1>
                    <p><strong>Prepared exclusively for:</strong> {name}</p>
                    <p><strong>Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
                    <p><strong>Document ID:</strong> BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}</p>
                    <p style="margin-top: 50px; font-style: italic;">
                        This personalized clinical analysis contains your unique behavioral patterns,<br>
                        transformation roadmap, and actionable techniques for lasting change.
                    </p>
                </div>
                
                <!-- Quick Reference Card -->
                <div class="page-break">
                    <h1>Quick Reference Card</h1>
                    <p><em>Print this page and keep it visible</em></p>
                    
                    <div class="metric">
                        <h2>Your Primary Pattern</h2>
                        <p><strong>{dominant.get('name', 'Unknown')}</strong></p>
                        <p>Intensity: {dominant.get('score', 0):.1f}/10</p>
                    </div>
                    
                    <div class="metric">
                        <h2>When You Notice It Starting:</h2>
                        <ol>
                            <li><strong>PAUSE</strong> - Take 3 deep breaths</li>
                            <li><strong>NAME</strong> - "This is my {dominant.get('name', 'pattern')} pattern"</li>
                            <li><strong>CHOOSE</strong> - "I can respond differently"</li>
                        </ol>
                    </div>
                    
                    <div class="mantra">
                        <h2 style="color: white; margin: 0;">Your Intervention Phrase</h2>
                        <p style="font-size: 1.2em; margin: 10px 0;">
                            "{self._get_intervention_phrase(dominant.get('id'))}"
                        </p>
                    </div>
                </div>
                
                <!-- Personal Mantras -->
                <div class="page-break">
                    <h1>Your Personal Transformation Mantras</h1>
                    <p><em>Read these daily - designed specifically for YOUR patterns</em></p>
            """
            
            # Add mantras
            if dominant:
                html_content += f"""
                    <div class="mantra">
                        1. {self._get_pattern_mantra(dominant.get('id'))}
                    </div>
                """
            
            for i, pattern in enumerate(primary_patterns[:2], 2):
                html_content += f"""
                    <div class="mantra">
                        {i}. {self._get_pattern_mantra(pattern.get('id'))}
                    </div>
                """
            
            html_content += """
                </div>
                
                <!-- Executive Summary -->
                <div class="page-break">
                    <h1>Executive Summary</h1>
            """
            
            # Add metrics
            html_content += f"""
                    <div class="metric">
                        <strong>Patterns Identified:</strong> {pattern_analysis.get('pattern_count', 0)}<br>
                        <strong>Success Probability:</strong> {success_prediction.get('overall_success_rate', 85)}%<br>
                        <strong>Timeline:</strong> {success_prediction.get('timeline_estimate', '2-3 weeks')}<br>
                        <strong>Recommended Sessions:</strong> {success_prediction.get('recommended_sessions', 2)}
                    </div>
                    
                    <h2>Primary Pattern Analysis</h2>
                    <div class="metric">
                        <h3 style="color: #4CA1A3;">{dominant.get('name', 'Unknown Pattern')}</h3>
                        <p><strong>Intensity:</strong> {dominant.get('score', 0):.1f}/10</p>
            """
            
            pattern_desc = dominant.get('description', {})
            if pattern_desc:
                html_content += f"""
                        <p><strong>Core belief:</strong> {pattern_desc.get('core_belief', 'Pattern analysis in progress')}</p>
                        <p><strong>Impact:</strong> {pattern_desc.get('impact', 'This pattern affects your daily functioning')}</p>
                """
            
            html_content += """
                    </div>
                </div>
                
                <!-- Immediate Techniques -->
                <div class="page-break">
                    <h1>Immediate Action Techniques</h1>
                    <p><em>Start using these today - before your first session</em></p>
                    
                    <div class="technique">
                        <h2>The 5-4-3-2-1 Grounding Method</h2>
                        <p>When you notice your pattern starting:</p>
                        <ul>
                            <li>Name 5 things you SEE</li>
                            <li>Name 4 things you FEEL</li>
                            <li>Name 3 things you HEAR</li>
                            <li>Name 2 things you SMELL</li>
                            <li>Name 1 thing you TASTE</li>
                        </ul>
                        <p><em>This interrupts automatic patterns and returns you to the present moment</em></p>
                    </div>
                    
                    <div class="technique">
                        <h2>The PAUSE Protocol</h2>
                        <ul>
                            <li><strong>P</strong> - Pause what you're doing</li>
                            <li><strong>A</strong> - Acknowledge the pattern</li>
                            <li><strong>U</strong> - Understand it's protecting you</li>
                            <li><strong>S</strong> - Select a new response</li>
                            <li><strong>E</strong> - Execute with compassion</li>
                        </ul>
                        <p><em>Practice this 2-3 times daily, even when calm</em></p>
                    </div>
            """
            
            # Add pattern-specific technique
            html_content += f"""
                    <div class="technique">
                        <h2>Your Pattern-Specific Technique</h2>
                        {self._get_pattern_specific_technique(dominant.get('id')).replace('<strong>', '<strong style="color: #4CA1A3;">').replace('<br>', '<br/>')}
                    </div>
                </div>
                
                <!-- Session Roadmap -->
                <div class="page-break">
                    <h1>Your Transformation Timeline</h1>
                    
                    <div class="metric">
                        <h2>Session 1: Pattern Mapping & Rapport Building</h2>
                        <p><strong>Duration:</strong> 90 minutes</p>
                        <p><strong>What to expect:</strong></p>
                        <ul>
                            <li>Complete behavioral chain mapping</li>
                            <li>Subconscious pattern identification</li>
                            <li>Initial positive programming</li>
                            <li>Therapeutic alliance establishment</li>
                            <li>You'll leave with clarity about your patterns</li>
                        </ul>
                    </div>
                    
                    <div class="metric">
                        <h2>Session 2: Neural Rewiring & Integration</h2>
                        <p><strong>Duration:</strong> 90 minutes</p>
                        <p><strong>What to expect:</strong></p>
                        <ul>
                            <li>Deep hypnotic state for subconscious access</li>
                            <li>Pattern interruption at neural level</li>
                            <li>New response pathway installation</li>
                            <li>Behavioral anchoring and testing</li>
                            <li>You'll notice shifts within 48-72 hours</li>
                        </ul>
                    </div>
                </div>
                
            <!-- Footer with Disclaimer -->
            <div style="margin-top: 50px; padding-top: 30px; border-top: 2px solid #CBD5E1;">
                <div style="text-align: center; color: #556D7A; font-size: 0.9em;">
                    <p>© {datetime.now().year} Bangkok Transformation Hypnotherapy</p>
                    <p>This document is confidential and prepared exclusively for {name}</p>
                </div>
                
                <div style="margin-top: 30px; padding: 20px; background: #FEF3C7; border-left: 4px solid #F59E0B; border-radius: 6px;">
                    <p style="margin: 0 0 10px 0; font-weight: bold; color: #92400E;">IMPORTANT DISCLAIMER</p>
                    <p style="margin: 0; font-size: 0.85em; color: #78350F; line-height: 1.6;">
                        This assessment is a proprietary framework for hypnotherapy treatment planning. 
                        It is not clinically validated and should not be used for self-diagnosis or as 
                        a replacement for professional mental health care.
                    </p>
                    <p style="margin: 10px 0 0 0; font-size: 0.85em; color: #78350F; line-height: 1.6;">
                        Consult with qualified mental health professionals for diagnostic assessment 
                        and evidence-based treatment recommendations.
                    </p>
                </div>
                
                <div style="margin-top: 20px; text-align: center; color: #94A3B8; font-size: 0.75em;">
                    <p>For questions or concerns, contact: [your email/phone]</p>
                    <p>Thailand Mental Health Hotline: 1323 (24/7) | Emergency: 1669</p>
                </div>
            </div>
            </body>
            </html>
            """
            
            # Convert HTML to PDF
            pdf_buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
            
            if pisa_status.err:
                raise Exception("PDF generation failed")
            
            pdf_buffer.seek(0)
            return pdf_buffer.getvalue()
            
        except Exception as e:
            print(f"PDF generation error: {str(e)}")
            return None

    def _render_downloadable_resources(self, master_analytics: Dict):
        """Downloadable worksheets and tools"""
        st.markdown("## 📥 Downloadable resources")
        st.caption("Print-ready worksheets and tracking tools")
        
        worksheets = {
            "daily_tracking": self._generate_daily_tracking_worksheet(),
            "success_journal": self._generate_success_journal(),
            "trigger_worksheet": self._generate_trigger_worksheet(master_analytics),
            "response_checklist": self._generate_response_checklist(master_analytics),
            "weekly_review": self._generate_weekly_review()
        }
        
        for key, (title, description, content) in worksheets.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{title}**")
                st.caption(description)
            with col2:
                st.download_button(
                    "Download",
                    data=content,
                    file_name=f"{key}.txt",
                    mime="text/plain",
                    key=f"dl_{key}",
                    use_container_width=True
                )

    def _generate_daily_tracking_worksheet(self) -> Tuple[str, str, str]:
        """Generate daily tracking worksheet"""
        title = "Daily pattern tracking log"
        description = "Track pattern occurrences and interventions"
        content = """DAILY PATTERN TRACKING LOG

Date: _____________

PATTERN AWARENESS
□ I noticed my pattern starting
□ I caught it before full activation
□ I used my intervention phrase
□ I chose a different response

PATTERN OCCURRENCES
Time | Trigger | Intensity (1-10) | Response Used | Outcome
_____|_________|_________________|_______________|________
     |         |                 |               |
     |         |                 |               |
     |         |                 |               |

WINS TODAY
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

LEARNING
What I discovered: ___________________________________
__________________________________________________________

TOMORROW'S INTENTION
I will: ______________________________________________
__________________________________________________________
"""
        return (title, description, content)

    def _generate_success_journal(self) -> Tuple[str, str, str]:
        """Generate success journal template"""
        title = "Success journal template"
        description = "Document wins and learnings"
        content = """SUCCESS JOURNAL

Week of: _____________

DAILY WINS
Monday:
1-3: _______________________________________________

Tuesday:
1-3: _______________________________________________

Wednesday:
1-3: _______________________________________________

Thursday:
1-3: _______________________________________________

Friday:
1-3: _______________________________________________

Saturday:
1-3: _______________________________________________

Sunday:
1-3: _______________________________________________

WEEKLY REFLECTION
Biggest transformation: _____________________________
Most challenging moment: ____________________________
Key learning: _______________________________________
Next week's focus: __________________________________
"""
        return (title, description, content)

    def _generate_trigger_worksheet(self, master_analytics: Dict) -> Tuple[str, str, str]:
        """Generate trigger identification worksheet"""
        title = "Trigger identification worksheet"
        description = "Map your specific triggers"
        
        pattern_analysis = master_analytics.get('pattern_analysis', {})
        dominant = pattern_analysis.get('dominant_pattern', {})
        pattern_name = dominant.get('name', 'your pattern')
        
        content = f"""TRIGGER IDENTIFICATION WORKSHEET

Your Primary Pattern: {pattern_name}

COMMON TRIGGERS
1-5: List situations, people, or events that activate your pattern

EARLY WARNING SIGNS
Physical: __________________________________________
Emotional: _________________________________________
Mental: ____________________________________________

INTERVENTION PLANNING
For my top 3 triggers, I will:
1-3: _______________________________________________
"""
        return (title, description, content)

    def _generate_response_checklist(self, master_analytics: Dict) -> Tuple[str, str, str]:
        """Generate alternative responses checklist"""
        title = "Alternative responses checklist"
        description = "Pre-planned responses for common triggers"
        
        pattern_analysis = master_analytics.get('pattern_analysis', {})
        dominant = pattern_analysis.get('dominant_pattern', {})
        intervention = self._get_intervention_phrase(dominant.get('id'))
        
        content = f"""ALTERNATIVE RESPONSES CHECKLIST

Your Intervention Phrase: "{intervention}"

BEFORE THE SITUATION
□ Identified likely triggers
□ Practiced intervention phrase
□ Have 3 alternative responses ready
□ Grounded and centered

DURING THE TRIGGER
□ PAUSE - Stop automatic reaction
□ BREATHE - Three deep breaths
□ NAME - "This is my pattern"
□ CHOOSE - Select alternative response

ALTERNATIVE RESPONSES
Option A-C: List your prepared responses

AFTER THE SITUATION
□ Notice what happened
□ Celebrate any different choice
□ Learn from the experience
□ Prepare for next time
"""
        return (title, description, content)

    def _generate_weekly_review(self) -> Tuple[str, str, str]:
        """Generate weekly review template"""
        title = "Weekly progress review"
        description = "Structured reflection template"
        content = """WEEKLY PROGRESS REVIEW

Week of: _____________

PATTERN AWARENESS (Rate 1-10)
How aware was I of my pattern this week? _____
How often did I catch it early? _____
How empowered do I feel? _____

WINS THIS WEEK (3-5 examples)
1-5: Describe trigger, new response, outcome

CHALLENGES
What was difficult: __________________________________
What I learned: _____________________________________

PATTERN FREQUENCY
Compared to last week:
□ Decreased significantly
□ Decreased somewhat
□ Stayed the same
□ Increased (this is data, not failure)

NEXT WEEK'S FOCUS
My intention: _______________________________________
Support needed: _____________________________________
"""
        return (title, description, content)

    def _generate_markdown_report(self, assessment_data: Dict) -> str:
        """Generate comprehensive markdown report"""
        try:
            master_analytics = assessment_data.get('master_analytics', {})
            contact = assessment_data.get('contact_info', {})
            name = contact.get('full_name', 'Valued Client')
            
            pattern_analysis = master_analytics.get('pattern_analysis', {})
            dominant = pattern_analysis.get('dominant_pattern', {})
            success_prediction = master_analytics.get('success_prediction', {})
            
            report = f"""# COMPLETE TRANSFORMATION BLUEPRINT

**Prepared exclusively for:** {name}  
**Date:** {datetime.now().strftime('%B %d, %Y')}  
**Document ID:** BTF-{datetime.now().strftime('%Y%m%d')}-{hash(name) % 10000:04d}

---

## QUICK REFERENCE CARD

### Your Primary Pattern
**{dominant.get('name', 'Unknown')}**  
Intensity: {dominant.get('score', 0):.1f}/10

### When You Notice It Starting:
1. **PAUSE** - Take 3 deep breaths
2. **NAME** - "This is my {dominant.get('name', 'pattern')} pattern"
3. **CHOOSE** - "I can respond differently"

### Your Intervention Phrase
> "{self._get_intervention_phrase(dominant.get('id'))}"

---

## YOUR PERSONAL TRANSFORMATION MANTRAS

"""
            
            if dominant:
                report += f"1. {self._get_pattern_mantra(dominant.get('id'))}\n\n"
            
            primary_patterns = pattern_analysis.get('primary_patterns', [])
            for i, pattern in enumerate(primary_patterns[:2], 2):
                report += f"{i}. {self._get_pattern_mantra(pattern.get('id'))}\n\n"
            
            report += f"""---

## EXECUTIVE SUMMARY

**Patterns Identified:** {pattern_analysis.get('pattern_count', 0)}  
**Success Probability:** {success_prediction.get('overall_success_rate', 85)}%  
**Timeline:** {success_prediction.get('timeline_estimate', '2-3 weeks')}  
**Recommended Sessions:** {success_prediction.get('recommended_sessions', 2)}

---

*Complete blueprint with detailed techniques, session planning, and tracking tools*

**© {datetime.now().year} Bangkok Transformation Hypnotherapy**  
"""
            
            return report
            
        except Exception as e:
            print(f"Markdown generation error: {str(e)}")
            return "# Transformation Blueprint\n\nError generating report. Please contact support."


def create_behavioral_blueprint():
    """Factory function"""
    return BehavioralBlueprint()
