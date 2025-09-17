# components/blueprint.py
# Comprehensive Behavioral Blueprint Component
# Detailed insights for visitors questioning their patterns and seeking clarity
# Integrates traditional behavioral patterns with digital syndrome analysis

import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

class BehavioralBlueprint:
    """Comprehensive blueprint component providing detailed pattern insights"""
    
    def __init__(self):
        self.patterns = {
            1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
            4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
            7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
        }
        
        self.pattern_descriptions = {
            1: {
                "description": "You may find it challenging to accept or maintain positive emotional states",
                "impact": "This can limit your ability to fully enjoy success and happiness, creating cycles of self-sabotage",
                "transformation": "Learning to trust that joy and success can be sustainable and deserved",
                "what_you_notice": "Feeling guilty when things go well, waiting for the other shoe to drop, minimizing achievements",
                "what_others_see": "Someone who deflects compliments, seems uncomfortable with praise, or finds problems in good situations",
                "hidden_cost": "Missing out on life's genuine pleasures and the motivation that comes from celebrating wins",
                "breakthrough_moment": "Realizing that happiness doesn't make you vulnerable - it makes you stronger and more resilient"
            },
            2: {
                "description": "You experience recurring conflicts and power struggles in relationships",
                "impact": "This can create stress and prevent collaborative problem-solving, damaging important relationships",
                "transformation": "Developing skills for curious dialogue and win-win resolution",
                "what_you_notice": "Feeling defensive quickly, needing to be right, seeing disagreements as threats",
                "what_others_see": "Someone who argues their point intensely, seems confrontational, or withdraws when challenged",
                "hidden_cost": "Exhausting mental energy on conflicts instead of creative collaboration and genuine connection",
                "breakthrough_moment": "Discovering that being curious about others' perspectives actually strengthens your position"
            },
            3: {
                "description": "You maintain a default skepticism about others' intentions",
                "impact": "This protective mechanism may limit deep connections and opportunities for growth",
                "transformation": "Calibrating trust responses and building authentic relationships",
                "what_you_notice": "Analyzing people's motives, feeling suspicious of kindness, expecting hidden agendas",
                "what_others_see": "Someone who seems guarded, asks probing questions, or appears cynical about human nature",
                "hidden_cost": "Living in emotional isolation and missing genuine opportunities for support and connection",
                "breakthrough_moment": "Understanding that discernment and openness can coexist - you can be wise AND trusting"
            },
            4: {
                "description": "You tend toward black-and-white thinking patterns",
                "impact": "This can limit creative solutions and increase decision paralysis when faced with complexity",
                "transformation": "Developing nuanced thinking and embracing creative possibilities",
                "what_you_notice": "Feeling stuck between two options, seeing things as all good or all bad, struggling with grey areas",
                "what_others_see": "Someone who wants clear answers, seems frustrated by ambiguity, or makes quick either/or judgments",
                "hidden_cost": "Missing innovative solutions that require holding multiple perspectives simultaneously",
                "breakthrough_moment": "Realizing that complexity isn't confusion - it's where the most elegant solutions hide"
            },
            5: {
                "description": "Your self-worth is closely tied to productivity and achievement",
                "impact": "This can lead to burnout and difficulty with rest or self-care without feeling guilty",
                "transformation": "Anchoring worth in your inherent value, independent of accomplishments",
                "what_you_notice": "Feeling anxious when not productive, equating rest with laziness, measuring yourself by output",
                "what_others_see": "Someone who's always busy, seems uncomfortable with downtime, or talks about achievements frequently",
                "hidden_cost": "Chronic stress, missed opportunities for reflection and creativity that come from mental space",
                "breakthrough_moment": "Discovering that your value exists completely separate from what you do or achieve"
            },
            6: {
                "description": "Your sense of identity shifts significantly across different contexts",
                "impact": "This can create internal confusion and emotional exhaustion from maintaining multiple personas",
                "transformation": "Integrating an authentic, consistent self across all situations",
                "what_you_notice": "Feeling like different people in different settings, adapting personality to fit in, losing sense of 'real self'",
                "what_others_see": "Someone who seems different depending on the group, appears to chameleon, or seems inconsistent",
                "hidden_cost": "Emotional exhaustion from performance, loss of authentic self-expression and genuine connections",
                "breakthrough_moment": "Realizing that your authentic self is actually more likeable and magnetic than any persona"
            },
            7: {
                "description": "You prioritize others' needs while neglecting your own self-care",
                "impact": "This can lead to resentment and emotional depletion over time, hurting the very relationships you're trying to protect",
                "transformation": "Developing healthy boundaries and self-care practices that actually improve your relationships",
                "what_you_notice": "Feeling guilty when focusing on yourself, automatically saying yes to requests, feeling responsible for others' emotions",
                "what_others_see": "Someone who's always helpful, never seems to have needs, or appears stressed but won't ask for help",
                "hidden_cost": "Resentment buildup, burnout, and becoming less effective at helping others when you're depleted",
                "breakthrough_moment": "Understanding that taking care of yourself is actually the most loving thing you can do for others"
            },
            8: {
                "description": "Your life choices are driven more by family expectations than personal desires",
                "impact": "This can create internal conflict and limit authentic self-expression and life satisfaction",
                "transformation": "Clarifying personal values while maintaining family harmony",
                "what_you_notice": "Feeling torn between what you want and what's expected, guilt about disappointing family, unclear about your own desires",
                "what_others_see": "Someone who references family expectations often, seems conflicted about decisions, or appears to live for others",
                "hidden_cost": "Living someone else's life instead of your own, missing your unique contribution to the world",
                "breakthrough_moment": "Realizing you can honor your family AND live authentically - they're not mutually exclusive"
            },
            9: {
                "description": "Your boundaries and limits vary dramatically based on context",
                "impact": "This can lead to inconsistent relationships and difficulty with self-advocacy across different situations",
                "transformation": "Establishing consistent, healthy boundaries across all situations",
                "what_you_notice": "Being strong in some situations but passive in others, feeling like you lose yourself in certain contexts",
                "what_others_see": "Someone who seems confident sometimes but submissive other times, appears unpredictable in their responses",
                "hidden_cost": "Confusion about your own limits, relationships built on false premises, accumulated resentment",
                "breakthrough_moment": "Discovering that consistent boundaries actually make you more trustworthy and respected"
            }
        }
        
        self.digital_insights = {
            'SEVERE': {
                'title': 'Specialized digital-native approach required',
                'description': 'Your assessment reveals significant digital conditioning patterns that require adapted therapeutic techniques.',
                'what_you_notice': 'Feeling more authentic online than offline, struggling with attention span for real-world activities, emotional states tied to digital feeds',
                'what_others_see': 'Someone who seems more engaged with their phone than present conversations, appears cynical about traditional approaches',
                'hidden_cost': 'Living in digital reality while real life passes by, missing genuine human connections and embodied experiences',
                'benefits': 'With proper specialized approach, you can integrate your digital competencies with real-world confidence and authentic emotional expression.',
                'why_traditional_fails': 'Traditional therapy expects attention spans and emotional patterns that digital conditioning has fundamentally altered',
                'hypnotherapy_advantage': 'Bypasses conscious resistance and works directly with the neural patterns that digital conditioning has created'
            },
            'MODERATE': {
                'title': 'Enhanced digital-aware therapy recommended', 
                'description': 'You show moderate digital conditioning that benefits from modified therapeutic approaches.',
                'what_you_notice': 'Some difficulty with extended focus, occasional preference for online interactions, influence of social media on mood',
                'what_others_see': 'Someone who checks their phone regularly, seems more comfortable texting than calling, references online culture',
                'hidden_cost': 'Fragmented attention reducing deep thinking capacity, some authentic emotions filtered through digital expression',
                'benefits': 'Standard techniques enhanced with digital awareness will optimize your transformation process.',
                'why_traditional_fails': 'Traditional approaches don\'t account for how digital environments have shaped your neural pathways',
                'hypnotherapy_advantage': 'Can work with both traditional patterns and digital conditioning simultaneously'
            },
            'MILD': {
                'title': 'Digital considerations integrated',
                'description': 'Some digital influence detected that will be incorporated into your standard approach.',
                'what_you_notice': 'Balanced online and offline life with occasional digital overwhelm, mostly traditional attention patterns',
                'what_others_see': 'Someone who uses technology normally without it dominating their personality or relationships',
                'hidden_cost': 'Minor attention fragmentation and occasional comparison triggered by social media',
                'benefits': 'Your digital skills can be leveraged as strengths in your transformation journey.',
                'why_traditional_fails': 'Standard approaches work well but miss opportunities to leverage your digital competencies',
                'hypnotherapy_advantage': 'Can enhance traditional patterns while optimizing your relationship with technology'
            },
            'MINIMAL': {
                'title': 'Traditional approach optimal',
                'description': 'Minimal digital conditioning detected - standard hypnotherapy approach is ideal.',
                'what_you_notice': 'Technology serves you rather than controlling you, strong attention span for offline activities',
                'what_others_see': 'Someone who uses technology as a tool without being dominated by it, present in conversations',
                'hidden_cost': 'Minimal digital interference with authentic living and relationships',
                'benefits': 'You can benefit from proven traditional techniques without modification.',
                'why_traditional_fails': 'Traditional approaches work well for you - this is about optimizing what already works',
                'hypnotherapy_advantage': 'Direct access to your subconscious without digital conditioning interference'
            }
        }
    
    def apply_styles(self):
        """Apply consistent styling aligned with global styles"""
        st.markdown("""
        <style>
        /* Use global CSS variables from utils/styling.py */
        .blueprint-hero {
            background: linear-gradient(135deg, var(--bg) 0%, #e1f0f0 100%);
            padding: var(--space-xl);
            border-radius: var(--radius-lg);
            margin: var(--space-md) 0;
            text-align: center;
            border: 1px solid var(--border);
            box-shadow: var(--shadow-sm);
        }
        
        .insight-card {
            background: var(--card-bg);
            padding: var(--space-lg);
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            margin: var(--space-md) 0;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
        }
        
        .insight-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .pattern-badge {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: var(--space-xs) var(--space-sm);
            border-radius: 20px;
            font-size: var(--font-size-normal);
            font-weight: 600;
            margin: var(--space-xs);
        }
        
        .severity-high { background: var(--error); }
        .severity-moderate { background: var(--warning); }
        .severity-mild { background: var(--accent); }
        .severity-minimal { background: var(--success); }
        
        .cost-analysis {
            background: #fef3c7;
            border: 1px solid var(--warning);
            color: #92400e;
            padding: var(--space-md);
            border-radius: var(--radius-sm);
            margin: var(--space-md) 0;
            font-weight: 500;
        }
        
        .breakthrough-card {
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
            color: white;
            padding: var(--space-lg);
            border-radius: var(--radius-sm);
            margin: var(--space-md) 0;
            box-shadow: var(--shadow-sm);
        }
        
        .transformation-preview {
            background: #f0f9ff;
            border: 1px solid #0ea5e9;
            padding: var(--space-md);
            border-radius: var(--radius-sm);
            margin: var(--space-md) 0;
        }
        
        .timeline-item {
            display: flex;
            align-items: center;
            margin: var(--space-sm) 0;
            padding: var(--space-sm);
            background: var(--bg);
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--accent);
        }
        
        .timeline-number {
            background: var(--accent);
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: var(--font-size-normal);
            font-weight: 600;
            margin-right: var(--space-md);
            flex-shrink: 0;
        }
        
        .success-indicator {
            display: flex;
            align-items: center;
            gap: var(--space-xs);
            margin: var(--space-xs) 0;
        }
        
        .success-bar {
            flex: 1;
            height: 8px;
            background: var(--border);
            border-radius: 4px;
            overflow: hidden;
        }
        
        .success-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--accent) 0%, var(--success) 100%);
            transition: width 0.5s ease;
        }
        
        .comparison-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-md);
            margin: var(--space-md) 0;
        }
        
        .comparison-card {
            padding: var(--space-md);
            border-radius: var(--radius-sm);
            border: 1px solid var(--border);
            background: var(--card-bg);
        }
        
        .traditional-approach {
            background: #fef2f2;
            border-color: #fecaca;
        }
        
        .hypnotherapy-approach {
            background: #f0fdf4;
            border-color: #bbf7d0;
        }
        
        .aha-moment {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: var(--space-lg);
            border-radius: var(--radius-sm);
            margin: var(--space-md) 0;
            box-shadow: var(--shadow-sm);
        }
        
        .digital-indicator {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: var(--space-sm);
            border-radius: var(--radius-sm);
            margin: var(--space-xs) 0;
            font-size: var(--font-size-normal);
            text-align: center;
        }
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .comparison-grid {
                grid-template-columns: 1fr;
                gap: var(--space-sm);
            }
            
            .blueprint-hero {
                padding: var(--space-lg) var(--space-md);
            }
            
            .insight-card, .breakthrough-card {
                padding: var(--space-md);
            }
        }
        </style>
        """, unsafe_allow_html=True)
    
    def render_pattern_cost_analysis(self, assessment_data):
        """Render detailed pattern cost analysis"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        if not pattern_scores:
            return
        
        # Calculate comprehensive costs
        costs = self._calculate_comprehensive_costs(pattern_scores, assessment_data)
        
        st.markdown("**The hidden cost of your current patterns**")
        
        # Weekly cost breakdown
        st.markdown(f"""
        <div class="cost-analysis">
        <h4 style="margin-top: 0;">Weekly impact analysis</h4>
        <p><strong>Time cost:</strong> Approximately {costs['time_hours']} hours per week of mental/emotional energy</p>
        <p><strong>Opportunity cost:</strong> {costs['opportunities']} missed chances for growth or connection</p>
        <p><strong>Relationship cost:</strong> {costs['relationship_strain']} relationship strain incidents</p>
        <p><strong>Energy cost:</strong> {costs['energy_drain']}% of your natural energy diverted to pattern management</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Compound cost visualization
        self._render_compound_cost_chart(costs)
        
        # Future vision vs current reality
        future_vision = self._extract_future_vision(assessment_data)
        if future_vision:
            st.markdown(f"""
            <div class="transformation-preview">
            <h4 style="color: #0ea5e9; margin-top: 0;">Your vision vs current reality</h4>
            <p><strong>Where you want to be:</strong> {future_vision}</p>
            <p><strong>Current barrier:</strong> These behavioral patterns are the primary obstacle between you and this reality.</p>
            <p><strong>Bridge needed:</strong> Subconscious pattern rewiring to align your automatic responses with your conscious goals.</p>
            </div>
            """, unsafe_allow_html=True)
    
    def render_detailed_pattern_insights(self, assessment_data):
        """Render deeply personalized pattern insights"""
        personal_lang = self._extract_personal_language(assessment_data)
        trigger_analysis = self._create_personalized_trigger_analysis(assessment_data)
        speaking_insights = self._generate_speaking_to_you_insights(assessment_data)
        
        st.markdown("### Your behavioral patterns decoded")
        
        # Personal recognition section
        if speaking_insights:
            st.markdown(f"""
            <div class="aha-moment">
            <h4 style="margin-top: 0;">Speaking directly to your experience</h4>
            <p><strong>Recognition:</strong> {speaking_insights['recognition']}</p>
            <p><strong>Validation:</strong> {speaking_insights['validation']}</p>
            <p><strong>Breakthrough insight:</strong> {speaking_insights['breakthrough']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Your exact trigger sequence
        st.markdown("**Your exact behavioral sequence**")
        sequence = trigger_analysis['sequence']
        intensity = trigger_analysis['intensity_level']
        
        st.markdown(f"""
        **Here's what happens in your specific pattern cycle:**
        
        🎯 **Your trigger:** "{sequence['trigger']}"
        
        ⚡ **What you notice first:** {sequence['awareness_point']}
        
        🫀 **Physical response:** {sequence['physical']} (Intensity: {intensity:.1f}/7)
        
        💭 **Automatic thought:** "{sequence['thought']}"
        
        😔 **Emotional cascade:** {sequence['emotion']}
        
        🏃 **Protective behavior:** {sequence['behavior']}
        
        ⭕ **What happens next:** {sequence['consequence']}
        
        🔄 **How it reinforces:** {sequence['reinforcement']}
        """)

        
        pattern_scores = assessment_data.get('pattern_scores', {})
        if not pattern_scores:
            st.warning("Complete the assessment to see detailed pattern insights")
            return
        
        st.markdown("**Understanding your behavioral patterns**")
        st.markdown("*These insights help you understand what you're experiencing and why traditional approaches may not have worked*")
        
        # Sort patterns by intensity
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Show detailed analysis for top 3 patterns
        for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
            pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
            pattern_info = self.pattern_descriptions.get(pattern_id, {})
            
            # Determine severity display
            if score >= 6:
                intensity_text = "High intensity"
                badge_class = "severity-high"
            elif score >= 4:
                intensity_text = "Moderate intensity" 
                badge_class = "severity-moderate"
            elif score >= 2:
                intensity_text = "Mild intensity"
                badge_class = "severity-mild"
            else:
                intensity_text = "Emerging pattern"
                badge_class = "severity-minimal"
            
            st.markdown(f"""
            <div class="insight-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h4 style="margin: 0; color: #273548;">{i+1}. {pattern_name}</h4>
                    <span class="pattern-badge {badge_class}">{intensity_text}</span>
                </div>
            """, unsafe_allow_html=True)
            
            # Create tabs for different aspects
            tab1, tab2, tab3, tab4 = st.tabs(["What you notice", "What others see", "Hidden costs", "Breakthrough potential"])
            
            with tab1:
                st.markdown(f"**What you might be experiencing:**")
                st.markdown(pattern_info.get('what_you_notice', 'Internal experience varies by individual'))
                st.markdown(f"**Overall impact:** {pattern_info.get('impact', 'Affects daily life and relationships')}")
            
            with tab2:
                st.markdown(f"**How this pattern shows up to others:**")
                st.markdown(pattern_info.get('what_others_see', 'External manifestation varies'))
                st.caption("*Often others see the pattern more clearly than we do ourselves*")
            
            with tab3:
                st.markdown(f"**What this pattern is costing you:**")
                st.markdown(pattern_info.get('hidden_cost', 'Reduces life satisfaction and authentic expression'))
                
                # Add specific cost calculation
                weekly_cost = self._calculate_pattern_specific_cost(pattern_id, score)
                st.warning(f"**Estimated weekly cost:** {weekly_cost}")
            
            with tab4:
                st.markdown(f"**Your breakthrough potential:**")
                st.success(pattern_info.get('breakthrough_moment', 'Transformation creates new possibilities'))
                st.markdown(f"**Transformation focus:** {pattern_info.get('transformation', 'Personalized approach will be developed')}")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Summary of additional patterns
        if len(sorted_patterns) > 3:
            additional_count = len(sorted_patterns) - 3
            additional_patterns = [self.patterns.get(pid, f"Pattern {pid}") for pid, _ in sorted_patterns[3:]]
            
            st.markdown(f"""
            <div class="insight-card">
                <h4 style="color: #273548;">Additional patterns identified ({additional_count})</h4>
                <p>Your comprehensive analysis also reveals these supporting patterns: <strong>{', '.join(additional_patterns)}</strong></p>
                <p style="color: #556D7A;">These secondary patterns often reinforce the primary ones and will be addressed as part of your integrated transformation approach.</p>
            </div>
            """, unsafe_allow_html=True)
    
    def render_aha_moment_bridge(self, assessment_data):
        """Render the 'aha moment' bridge helping visitors understand the deeper layer"""
        hidden_mechanisms = self._identify_hidden_mechanisms(assessment_data)
        protective_functions = self._identify_protective_functions(assessment_data)
        paradoxes = self._identify_paradoxes(assessment_data)
        
        st.markdown("### The hidden layer: why you're stuck (and it's not what you think)")
        
        st.markdown(f"""
        <div class="aha-moment">
        <h4 style="margin-top: 0; color: white;">The paradox that keeps you trapped</h4>
        <p>Your conscious mind is trying to change these patterns using logic and willpower. But here's what's really happening:</p>
        <p><strong>Your unconscious mind is running {len(hidden_mechanisms)} protective programs</strong> that it believes are keeping you safe.</p>
        <p>Every time you try to consciously override these patterns, your unconscious doubles down to "protect" you.</p>
        <p style="margin-bottom: 0;"><em>This is why willpower fails and why you need a different approach.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden mechanisms explanation
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🛡️ Protective mechanisms detected:**")
            for i, mechanism in enumerate(hidden_mechanisms[:4], 1):
                st.markdown(f"{i}. {mechanism}")
        
        with col2:
            st.markdown("**🔄 The reinforcement cycle:**")
            cycle_steps = [
                "You try to change consciously",
                "Unconscious detects 'threat' to protection",
                "Pattern intensifies as 'safety measure'",
                "You feel frustrated and try harder",
                "Cycle repeats and strengthens"
            ]
            for step in cycle_steps:
                st.markdown(f"• {step}")
        
        # The breakthrough insight
        st.markdown(f"""
        <div class="breakthrough-card">
        <h4 style="margin-top: 0;">The breakthrough insight</h4>
        <p><strong>Your patterns aren't broken - they're perfectly designed</strong> to solve problems you faced in the past.</p>
        <p>The issue is they're solving problems that no longer exist, creating new problems in the process.</p>
        <p><strong>Hypnotherapy works because:</strong> Instead of fighting these protective patterns, we work WITH your unconscious mind to update its programming for your current reality.</p>
        <p style="margin-bottom: 0;"><em>When your unconscious feels safe about the change, it stops resisting and starts supporting your transformation.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Future trajectory without intervention
        future_prediction = self._generate_detailed_future_prediction(assessment_data)
        st.warning(f"**Pattern trajectory without intervention:** {future_prediction}")
    
    def render_digital_insights(self, assessment_data):
        """Render comprehensive digital insights"""
        if not assessment_data.get('is_digital_native'):
            return
        
        digital_analysis = assessment_data.get('digital_despair_analysis')
        if not digital_analysis:
            return
        
        severity = digital_analysis['severity_level']
        score = digital_analysis['digital_despair_score']
        insight = self.digital_insights.get(severity, self.digital_insights['MINIMAL'])
        
        st.markdown("**Digital conditioning analysis**")
        
        st.markdown(f"""
        <div class="digital-indicator">
        📲 Digital conditioning detected: {severity} level ({score:.0f}% score)
        </div>
        """, unsafe_allow_html=True)
        
        # Main digital insights
        st.markdown(f"""
        <div class="insight-card">
        <h4 style="color: #273548;">{insight['title']}</h4>
        <p><strong>What this means:</strong> {insight['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed digital analysis in tabs
        tab1, tab2, tab3, tab4 = st.tabs(["What you notice", "Hidden costs", "Why traditional fails", "Hypnotherapy advantage"])
        
        with tab1:
            st.markdown("**Your digital conditioning patterns:**")
            st.markdown(insight['what_you_notice'])
            st.markdown("**How others see it:**")
            st.markdown(insight['what_others_see'])
        
        with tab2:
            st.markdown("**The hidden cost of digital conditioning:**")
            st.markdown(insight['hidden_cost'])
            
            # Component score breakdown
            if 'component_scores' in digital_analysis:
                st.markdown("**Specific areas affected:**")
                components = digital_analysis['component_scores']
                component_names = {
                    'reality_dissociation': 'Online vs offline authenticity gap',
                    'binary_success_pressure': 'Extraordinary achievement pressure',
                    'ironic_detachment': 'Emotional protection through cynicism',
                    'algorithmic_dependency': 'Social media emotional regulation',
                    'nihilistic_worldview': 'Hopelessness and meaning crisis',
                    'hope_avoidance': 'Resistance to optimism',
                    'attention_fragmentation': 'Digital attention conditioning'
                }
                
                for comp, score in components.items():
                    if comp in component_names and score >= 2:
                        name = component_names[comp]
                        level = "High impact" if score >= 4 else "Moderate impact"
                        st.markdown(f"• **{name}:** {level}")
        
        with tab3:
            st.markdown("**Why traditional therapy often fails for digital natives:**")
            st.markdown(insight['why_traditional_fails'])
            
            if severity in ['SEVERE', 'MODERATE']:
                traditional_failures = [
                    "Attention span expectations don't match digital conditioning",
                    "Authority-based therapeutic relationship triggers resistance",
                    "Verbal processing conflicts with ironic protective mechanisms",
                    "Timeline expectations clash with digital instant-feedback conditioning",
                    "Hope-based interventions feel naive to cynicism-trained minds"
                ]
                for failure in traditional_failures:
                    st.markdown(f"• {failure}")
        
        with tab4:
            st.markdown("**How hypnotherapy succeeds with digital conditioning:**")
            st.markdown(insight['hypnotherapy_advantage'])
            
            if severity in ['SEVERE', 'MODERATE']:
                advantages = [
                    "Bypasses conscious ironic defenses to access authentic emotions",
                    "Works with digital-conditioned attention patterns instead of against them",
                    "Non-authoritarian approach reduces resistance",
                    "Rapid results match digital expectations",
                    "Integrates digital competencies rather than pathologizing them"
                ]
                for advantage in advantages:
                    st.markdown(f"✅ {advantage}")
        
        # Transformation potential
        st.markdown(f"""
        <div class="transformation-preview">
        <h4 style="color: #0ea5e9; margin-top: 0;">Your digital-native transformation potential</h4>
        <p><strong>Specialized advantage:</strong> {insight['benefits']}</p>
        <p><strong>Integration outcome:</strong> Your digital skills become strengths supporting your real-world confidence and authentic relationships.</p>
        <p><strong>Timeline:</strong> Digital natives often see faster results due to neuroplasticity advantages from digital adaptation.</p>
        </div>
        """, unsafe_allow_html=True)

    def render_personalized_cost_analysis(self, assessment_data):
        """Calculate costs using client's specific patterns and intensity"""
        trigger_analysis = self._create_personalized_trigger_analysis(assessment_data)
        personal_lang = self._extract_personal_language(assessment_data)
        
        # Extract urgency and life impact
        contact_info = assessment_data.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        primary_concern = contact_info.get('primary_concern', '')
        
        st.markdown("### What this pattern is specifically costing YOU")
        
        # Personal cost calculation
        intensity = trigger_analysis['intensity_level']
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        
        # Calculate based on their intensity and frequency
        weekly_hours = int(8 + (intensity * 2) + (pattern_count * 1.5))
        daily_episodes = max(1, int(intensity - 2))
        
        st.markdown(f"""
        <div class="cost-analysis">
        <h4 style="margin-top: 0;">Your personal pattern cost breakdown</h4>
        <p><strong>Daily episodes:</strong> Approximately {daily_episodes} times per day this sequence activates</p>
        <p><strong>Weekly time cost:</strong> {weekly_hours} hours of mental/emotional energy diverted</p>
        <p><strong>What you told us:</strong> "{primary_concern[:150]}..." - this impact is measurable and preventable</p>
        {"<p><strong>Urgency factor:</strong> You rated this as " + urgency.lower() + " - the cost compounds daily</p>" if urgency != 'Not specified' else ""}
        </div>
        """, unsafe_allow_html=True)
        
        # Use their future vision
        future_vision = self._extract_future_vision(assessment_data)
        if future_vision:
            st.markdown(f"""
            <div class="transformation-preview">
            <h4 style="color: #0ea5e9; margin-top: 0;">Your vision vs current reality gap</h4>
            <p><strong>You described wanting:</strong> "{future_vision}"</p>
            <p><strong>Current barrier:</strong> The exact behavioral sequence mapped above is what's preventing this reality.</p>
            <p><strong>Bridge needed:</strong> Interrupt this sequence at {len(trigger_analysis['intervention_points'])} specific intervention points we've identified.</p>
            </div>
            """, unsafe_allow_html=True)

    def render_your_session_preview(self, assessment_data):
        """Show exactly what will happen in THEIR sessions"""
        st.markdown("### Your personalized session roadmap")
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        digital_analysis = assessment_data.get('digital_despair_analysis')
        trigger_analysis = self._create_personalized_trigger_analysis(assessment_data)
        
        # Session 1 specific to their patterns
        dominant_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)[:2]
        
        session_1_focus = []
        session_2_targets = []
        
        for pattern_id, score in dominant_patterns:
            pattern_name = self.patterns[pattern_id]
            session_1_focus.append(f"Deep dive into your {pattern_name} pattern origins and protective functions")
            session_2_targets.append(f"Install new {pattern_name.lower()} responses using theta brainwave programming")
        
        st.markdown(f"""
        #### Session 1: Your pattern archaeology (90 minutes)
        **Specific to your patterns:**
        {"• " + chr(10).join(session_1_focus)}
        
        **Your trigger sequence work:**
        • Map the complete chain: "{trigger_analysis['sequence']['trigger']}" → automatic response
        • Identify your {len(trigger_analysis['intervention_points'])} intervention points
        • Install pattern interrupts using your natural awareness style
        
        **Rapport and safety:**
        • Address your specific concerns about change
        • Work with your protective mechanisms, not against them
        {"• Digital-native adaptations for your attention style" if assessment_data.get('is_digital_native') else ""}
        """)
        
        st.markdown(f"""
        #### Session 2: Your neural rewiring (90 minutes)
        **Pattern transformation specific to you:**
        {"• " + chr(10).join(session_2_targets)}
        
        **Trigger sequence reprogramming:**
        • New response installation at each intervention point
        • Future scenario testing with your specific triggers
        • Confidence anchoring for real-world application
        
        **Integration and testing:**
        • Mental rehearsal using your actual life situations
        • Reinforcement of new patterns until they feel natural
        • Success programming aligned with your future vision
        """)


    def render_transformation_roadmap(self, assessment_data):
        """Render detailed transformation roadmap"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        st.markdown("### Your personalized transformation roadmap")
        
        # Calculate session plan
        session_plan = self._calculate_session_plan(pattern_scores, digital_analysis)
        
        # Timeline overview
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total sessions", session_plan['total_sessions'])
        with col2:
            st.metric("Timeline", session_plan['timeline'])
        with col3:
            st.metric("Success probability", f"{session_plan['success_rate']}%")
        
        # Success probability visualization
        st.markdown("**Your transformation success likelihood:**")
        success_factors = session_plan['success_factors']
        
        for factor, weight in success_factors.items():
            progress = min(100, max(0, weight))
            st.markdown(f"""
            <div class="success-indicator">
                <span style="width: 150px; font-size: 0.9rem;">{factor}:</span>
                <div class="success-bar">
                    <div class="success-fill" style="width: {progress}%"></div>
                </div>
                <span style="font-size: 0.9rem; font-weight: 600;">{progress}%</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Detailed session breakdown
        st.markdown("**Session-by-session breakdown**")
        
        phases = session_plan['phases']
        for i, phase in enumerate(phases):
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-number">{i+1}</div>
                <div style="flex: 1;">
                    <h5 style="margin: 0 0 0.5rem 0; color: #273548;">{phase['title']}</h5>
                    <p style="margin: 0 0 0.5rem 0; color: #556D7A; font-size: 0.9rem;"><em>{phase['duration']}</em></p>
                    <p style="margin: 0 0 0.5rem 0;">{phase['description']}</p>
                    <p style="margin: 0; font-weight: 600; color: #4CA1A3;">Expected outcome: {phase['outcome']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # What to expect during transformation
        st.markdown("#### What to expect during your transformation")
        
        expectations = [
            {
                "timeframe": "First 24-48 hours",
                "experience": "Initial shifts in awareness and automatic responses",
                "what_you_notice": "Catching yourself before old patterns activate, feeling different in familiar situations"
            },
            {
                "timeframe": "Week 1",
                "experience": "New response patterns beginning to feel natural",
                "what_you_notice": "Responding differently in triggering situations, others commenting on changes"
            },
            {
                "timeframe": "Week 2-3",
                "experience": "Integration and stabilization of new patterns",
                "what_you_notice": "Old patterns feeling foreign, new patterns becoming unconscious habits"
            },
            {
                "timeframe": "Month 1+",
                "experience": "Complete integration and continued evolution",
                "what_you_notice": "Living from new patterns naturally, ongoing growth and refinement"
            }
        ]
        
        for exp in expectations:
            with st.expander(f"**{exp['timeframe']}**: {exp['experience']}"):
                st.markdown(f"**What you'll notice:** {exp['what_you_notice']}")
    
    def render_why_hypnotherapy_works(self, assessment_data):
        """Render comprehensive explanation of why hypnotherapy works for these patterns"""
        st.markdown("**Why hypnotherapy succeeds where other approaches fail**")
        
        # Traditional vs hypnotherapy comparison
        st.markdown("**The approach comparison**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="comparison-card traditional-approach">
            <h5 style="color: #dc2626; margin-top: 0;">Traditional approaches</h5>
            <p><strong>Method:</strong> Conscious analysis and willpower</p>
            <p><strong>Target:</strong> Symptoms and behaviors</p>
            <p><strong>Timeline:</strong> Months to years</p>
            <p><strong>Success rate:</strong> 30-40% for pattern-based issues</p>
            <p><strong>Why it struggles:</strong></p>
            <ul style="margin-bottom: 0;">
                <li>Patterns run below conscious awareness</li>
                <li>Logical understanding doesn't change emotional programming</li>
                <li>Willpower depletes over time</li>
                <li>Focuses on symptoms, not root programming</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="comparison-card hypnotherapy-approach">
            <h5 style="color: #059669; margin-top: 0;">Rapid transformation hypnotherapy</h5>
            <p><strong>Method:</strong> Direct subconscious programming</p>
            <p><strong>Target:</strong> Root neural patterns</p>
            <p><strong>Timeline:</strong> 2-3 sessions</p>
            <p><strong>Success rate:</strong> 85% for pattern-based issues</p>
            <p><strong>Why it succeeds:</strong></p>
            <ul style="margin-bottom: 0;">
                <li>Works directly with pattern source</li>
                <li>Bypasses conscious resistance</li>
                <li>Creates lasting neural pathway changes</li>
                <li>Addresses protective functions compassionately</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # The science behind the success
        st.markdown("#### The neurological advantage")
        
        st.markdown("""
        **How hypnotherapy creates rapid, lasting change:**
        
        1. **Theta brainwave access** (4-8 Hz): The optimal state for neural rewiring, typically only accessible during deep meditation or hypnosis
        
        2. **Neuroplasticity activation**: Direct communication with the subconscious allows rapid creation of new neural pathways
        
        3. **Pattern interruption**: Old behavioral sequences are interrupted at their source, not just managed at the symptom level
        
        4. **Positive programming**: New, empowering response patterns are installed using the same neural mechanisms that created the original patterns
        
        5. **Integration testing**: New patterns are tested and reinforced in imagined scenarios before real-world application
        """)
        
        # Address common concerns
        st.markdown("#### Addressing your concerns about hypnotherapy")
        
        concerns = [
            {
                "concern": "Will I lose control or do things against my will?",
                "reality": "You remain completely aware and in control. You cannot be made to do anything against your values or beliefs. Hypnosis is a collaborative process where you choose to follow suggestions that align with your goals."
            },
            {
                "concern": "What if I can't be hypnotized?",
                "reality": "Everyone experiences hypnosis naturally multiple times per day (highway hypnosis, getting absorbed in a book/movie). Clinical hypnosis simply guides you into this natural state intentionally."
            },
            {
                "concern": "Is this just temporary relaxation or real change?",
                "reality": "While relaxation occurs, the primary work is neural rewiring. Brain imaging shows measurable changes in neural pathway activation that persist long after sessions."
            },
            {
                "concern": "How is this different from stage hypnosis?",
                "reality": "Clinical hypnotherapy is a therapeutic intervention focused on positive change. There's no entertainment aspect - everything is designed around your specific goals and wellbeing."
            },
            {
                "concern": "What if my patterns come back?",
                "reality": "Properly installed patterns typically become permanent because they're more functional than the old ones. Your unconscious mind naturally maintains what works better."
            }
        ]
        
        for concern_data in concerns:
            with st.expander(f"❓ {concern_data['concern']}"):
                st.markdown(f"**Reality:** {concern_data['reality']}")
        
        # Specific advantages for their patterns
        pattern_scores = assessment_data.get('pattern_scores', {})
        if pattern_scores:
            top_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)[:2]
            
            st.markdown("#### Why hypnotherapy is specifically effective for your patterns")
            
            pattern_advantages = {
                1: "Bypasses the conscious guilt about happiness to install permission for joy at the subconscious level",
                2: "Works with the nervous system's fight-or-flight response to install curiosity instead of defensiveness",
                3: "Addresses the unconscious fear driving mistrust while maintaining healthy discernment",
                4: "Expands neural pathways to naturally see multiple options instead of just two",
                5: "Separates worth from achievement at the identity level, not just the logical level",
                6: "Integrates all aspects of personality into one authentic, consistent self",
                7: "Installs healthy self-care as a natural, guilt-free response",
                8: "Honors family loyalty while installing permission for personal authenticity",
                9: "Creates consistent boundary responses that feel natural across all contexts"
            }
            
            for pattern_id, score in top_patterns:
                pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
                advantage = pattern_advantages.get(pattern_id, "Addresses the specific unconscious programming maintaining this pattern")
                
                st.success(f"**{pattern_name}:** {advantage}")
    
    def render_why_traditional_failed_you(self, assessment_data):
        """Specific analysis of why traditional therapy likely failed for this person"""
        st.markdown("### Why traditional approaches haven't worked for YOU specifically")
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        digital_analysis = assessment_data.get('digital_despair_analysis')
        personal_lang = self._extract_personal_language(assessment_data)
        
        # Specific failure analysis
        failure_reasons = []
        
        # Pattern-specific failures
        if 1 in pattern_scores and pattern_scores[1] >= 4:
            failure_reasons.append("Traditional therapy often asks you to 'think positive' about the happiness you're deflecting - but your pattern isn't logical, it's protective programming")
        
        if 2 in pattern_scores and pattern_scores[2] >= 4:
            failure_reasons.append("Talk therapy can trigger your power struggle pattern - you may find yourself debating with therapists rather than collaborating")
        
        if 3 in pattern_scores and pattern_scores[3] >= 4:
            failure_reasons.append("Your systematic mistrust makes it difficult to form the therapeutic relationship traditional therapy requires")
        
        # Digital conditioning failures
        if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
            failure_reasons.extend([
                "Your digital conditioning has shortened attention spans below what traditional 50-minute sessions require",
                "The authority-based therapeutic relationship triggers your ironic detachment defenses",
                "Traditional hope-based interventions feel naive to your cynicism-trained mind"
            ])
        
        # Personal language analysis
        if any(word in ' '.join(personal_lang['emotional_language']) for word in ['stuck', 'frustrated', 'tired']):
            failure_reasons.append("You've likely experienced 'insight without change' - understanding your patterns logically but still being stuck in them emotionally")
        
        st.markdown("**Why your previous attempts likely failed:**")
        for reason in failure_reasons[:4]:
            st.markdown(f"• {reason}")
        
        st.success("**Why hypnotherapy will work:** It bypasses these exact resistance points by working directly with your unconscious protective programming instead of fighting it.")
        
    def render_investment_and_value(self, assessment_data):
        """Render comprehensive investment and value analysis"""
        st.markdown("### Investment analysis: cost of change vs cost of staying the same")
        
        # Calculate comprehensive costs
        pattern_scores = assessment_data.get('pattern_scores', {})
        lifetime_costs = self._calculate_lifetime_costs(pattern_scores, assessment_data)
        
        # Current trajectory costs
        st.markdown("#### The cost of not changing")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Financial impact over 5 years:**")
            st.error(f"• Lost opportunities: ${lifetime_costs['lost_opportunities']:,}")
            st.error(f"• Stress-related costs: ${lifetime_costs['stress_costs']:,}")
            st.error(f"• Relationship costs: ${lifetime_costs['relationship_costs']:,}")
            st.error(f"• **Total estimated cost: ${lifetime_costs['total_5_year']:,}**")
        
        with col2:
            st.markdown("**Life satisfaction impact:**")
            st.error(f"• {lifetime_costs['happiness_hours']} hours of potential happiness missed")
            st.error(f"• {lifetime_costs['relationship_quality']}% reduction in relationship quality")
            st.error(f"• {lifetime_costs['career_impact']}% limitation on career potential")
            st.error(f"• {lifetime_costs['health_impact']} years of stress impact on health")
        
        # Investment comparison
        st.markdown("#### Investment comparison")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="comparison-card traditional-approach">
            <h5 style="color: #dc2626; margin-top: 0;">Traditional therapy</h5>
            <p><strong>Duration:</strong> 18+ months</p>
            <p><strong>Sessions:</strong> 40-60 sessions</p>
            <p><strong>Investment:</strong> $15,000-25,000</p>
            <p><strong>Success rate:</strong> 30-40%</p>
            <p><strong>Time to results:</strong> 3-6 months</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="comparison-card">
            <h5 style="color: #eab308; margin-top: 0;">Alternative approaches</h5>
            <p><strong>Coaching:</strong> $5,000-15,000</p>
            <p><strong>Workshops:</strong> $2,000-8,000</p>
            <p><strong>Self-help:</strong> $500-2,000</p>
            <p><strong>Success rate:</strong> 10-25%</p>
            <p><strong>Sustainability:</strong> Low</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="comparison-card hypnotherapy-approach">
            <h5 style="color: #059669; margin-top: 0;">Hypnotherapy transformation</h5>
            <p><strong>Duration:</strong> 2-3 weeks</p>
            <p><strong>Sessions:</strong> 2-3 sessions</p>
            <p><strong>Investment:</strong> $3,000-4,000</p>
            <p><strong>Success rate:</strong> 85%</p>
            <p><strong>Time to results:</strong> 48-72 hours</p>
            </div>
            """, unsafe_allow_html=True)
        
        # ROI calculation
        roi_percentage = ((lifetime_costs['total_5_year'] - 4000) / 4000) * 100
        
        st.markdown(f"""
        <div class="breakthrough-card">
        <h4 style="margin-top: 0;">Return on investment</h4>
        <p><strong>Investment:</strong> $3,000-4,000 for complete transformation</p>
        <p><strong>5-year savings:</strong> ${lifetime_costs['total_5_year']:,} in avoided costs</p>
        <p><strong>ROI:</strong> {roi_percentage:,.0f}% return on investment</p>
        <p style="margin-bottom: 0;"><strong>Break-even time:</strong> Typically 2-6 months</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Payment options and guarantee
        st.markdown("#### Investment options and guarantee")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Standard transformation package:**
            - 2 sessions (180 minutes total): $3,000
            - Email integration support included
            - 85% success rate guarantee
            """)
            
            st.markdown("""
            **Complete transformation package:**
            - 3 sessions (240 minutes total): $4,000
            - Priority scheduling
            - 100% satisfaction guarantee
            - Complimentary 3rd session if needed
            """)
        
        with col2:
            st.markdown("""
            **Our guarantee:**
            - If you're not satisfied after 2 sessions, receive a complimentary 3rd session
            - If still not satisfied, receive a full refund
            - 95% of clients never need to use this guarantee
            """)
            
            st.success("**Payment plans available** - making transformation accessible regardless of current financial situation")
        
        # Value beyond the patterns
        st.markdown("#### Value beyond pattern resolution")
        
        additional_benefits = [
            "Enhanced decision-making clarity in all life areas",
            "Increased confidence and self-advocacy skills",
            "Improved relationship satisfaction and communication",
            "Greater resilience to future stress and challenges",
            "Access to unconscious creativity and problem-solving abilities",
            "Deeper self-understanding and authentic expression",
            "Increased energy from eliminating internal conflicts",
            "Better sleep and reduced anxiety as byproducts"
        ]
        
        st.markdown("**Additional transformation benefits:**")
        for benefit in additional_benefits:
            st.markdown(f"✅ {benefit}")
    
    def render_empowerment_section(self, assessment_data):
        """Render empowerment section showing visitor's readiness and strengths"""
        st.markdown("### You already have everything needed for rapid transformation")
        
        # Extract readiness indicators
        readiness_indicators = self._extract_readiness_indicators(assessment_data)
        transformation_assets = self._identify_transformation_assets(assessment_data)
        
        st.markdown(f"""
        <div class="breakthrough-card">
        <h4 style="margin-top: 0;">Your transformation readiness profile</h4>
        <p>Most people think they need to "get ready" for change. The truth is, taking this assessment demonstrates you already possess the most important element: <strong>pattern recognition ability</strong>.</p>
        <p>This represents 60% of the transformation work already complete.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Readiness indicators
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**✅ Your readiness indicators:**")
            for indicator in readiness_indicators:
                st.markdown(f"• {indicator}")
        
        with col2:
            st.markdown("**💪 Your transformation assets:**")
            for asset in transformation_assets:
                st.markdown(f"• {asset}")
        
        # Success predictors specific to their profile
        success_predictors = self._calculate_success_predictors(assessment_data)
        
        st.markdown("#### Your success probability factors")
        
        for predictor, score in success_predictors.items():
            color = "#22c55e" if score >= 80 else "#eab308" if score >= 60 else "#ef4444"
            st.markdown(f"""
            <div class="success-indicator">
                <span style="width: 200px; font-size: 0.9rem;">{predictor}:</span>
                <div class="success-bar">
                    <div class="success-fill" style="width: {score}%; background: {color};"></div>
                </div>
                <span style="font-size: 0.9rem; font-weight: 600;">{score}%</span>
            </div>
            """, unsafe_allow_html=True)
        
        # What this means for their transformation
        average_score = sum(success_predictors.values()) / len(success_predictors)
        
        if average_score >= 80:
            outlook = "Excellent"
            message = "You have all the key factors for rapid, lasting transformation. Most clients with your profile see significant shifts within 48 hours of Session 1."
        elif average_score >= 65:
            outlook = "Very good"
            message = "You have strong fundamentals for transformation success. Some areas may need extra attention, but excellent results are highly likely."
        else:
            outlook = "Good with focused work"
            message = "While some factors may need development, your core readiness is solid. With proper approach, transformation is very achievable."
        
        st.info(f"**Overall transformation outlook: {outlook}** - {message}")
        
        # The mindset shift
        st.markdown("#### The mindset shift that changes everything")
        
        st.markdown("""
        **From:** "I need to fix what's wrong with me"  
        **To:** "I need to update programming that served me in the past but no longer fits my current life"
        
        This reframe changes everything because:
        - You're not broken - you're running outdated software
        - Your patterns were intelligent adaptations to past circumstances
        - Change becomes upgrading, not fixing
        - Your unconscious mind cooperates instead of resisting
        """)
    
    def render_next_steps_and_access(self, assessment_data):
        """Render clear next steps and access information"""
        st.markdown("### Your transformation begins now")
        
        # Immediate next steps
        contact_info = assessment_data.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            contact_timeline = "within 24 hours"
            priority_message = "Given your urgency level, you're on our priority contact list."
        else:
            contact_timeline = "within 48-72 hours"
            priority_message = "You'll hear from our clinical team soon."
        
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div style="flex: 1;">
                <h5 style="margin: 0 0 0.5rem 0; color: #273548;">Clinical review and personalization</h5>
                <p style="margin: 0 0 0.5rem 0; color: #556D7A; font-size: 0.9rem;"><em>24-48 hours</em></p>
                <p style="margin: 0 0 0.5rem 0;">Licensed therapist analyzes your comprehensive assessment and designs your personalized transformation protocol. {priority_message}</p>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div style="flex: 1;">
                <h5 style="margin: 0 0 0.5rem 0; color: #273548;">Personal consultation scheduling</h5>
                <p style="margin: 0 0 0.5rem 0; color: #556D7A; font-size: 0.9rem;"><em>{contact_timeline}</em></p>
                <p style="margin: 0 0 0.5rem 0;">We reach out via your preferred method to schedule your first transformation session and answer any questions.</p>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">3</div>
            <div style="flex: 1;">
                <h5 style="margin: 0 0 0.5rem 0; color: #273548;">Transformation session 1</h5>
                <p style="margin: 0 0 0.5rem 0; color: #556D7A; font-size: 0.9rem;"><em>Within 1 week</em></p>
                <p style="margin: 0 0 0.5rem 0;">Your personalized hypnotherapy protocol begins, targeting your specific pattern constellation for maximum effectiveness.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # What to prepare
        st.markdown("#### What to prepare while you wait")
        
        preparation_steps = [
            "Notice your patterns in action without trying to change them - awareness is the first step",
            "Begin to see your patterns as outdated protection rather than personal flaws",
            "Consider what life would look like if these patterns were completely resolved",
            "Stay open to the possibility that change can be easier than you've experienced before"
        ]
        
        for i, step in enumerate(preparation_steps, 1):
            st.markdown(f"{i}. {step}")
        
        # Access and booking options
        st.markdown("#### Ready to accelerate your transformation?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Learn more about our method:**
            - Understand the science behind rapid transformation
            - See detailed success stories and testimonials
            - Explore frequently asked questions
            """)
            st.link_button("🔬 Explore our method", "https://hypnotherapy.streamlit.app", use_container_width=True)
        
        with col2:
            st.markdown("""
            **Schedule direct consultation:**
            - Speak with our clinical team immediately
            - Get personalized recommendations
            - Book your transformation sessions
            """)
            st.link_button("📞 Schedule consultation", "https://calendly.com/laetitiasheppard/discovery", use_container_width=True)
        
        # Support and guarantee information
        st.markdown("#### Your support and guarantee")
        
        st.info("""
        **Complete support included:**
        - Pre-session preparation guidance
        - Between-session email support
        - Post-session integration assistance
        - Access to our clinical team for questions
        
        **Our commitment:**
        - If you're not satisfied after 2 sessions, receive a complimentary 3rd session
        - If still not satisfied, receive a full refund
        - 95% of clients never need to use this guarantee
        """)
    
    # Helper methods for calculations and analysis
    
    def _calculate_comprehensive_costs(self, pattern_scores, assessment_data):
        """Calculate comprehensive weekly and annual costs"""
        if not pattern_scores:
            return {'time_hours': 0, 'opportunities': 0, 'relationship_strain': 0, 'energy_drain': 0}
        
        pattern_count = len(pattern_scores)
        intensity_avg = sum(pattern_scores.values()) / len(pattern_scores)
        
        # Base calculations with realistic estimates
        base_time = 8  # hours per week
        pattern_multiplier = min(pattern_count * 1.5, 12)
        intensity_multiplier = min(intensity_avg / 3, 3)
        
        time_hours = int(base_time + pattern_multiplier + intensity_multiplier)
        opportunities = max(1, int(pattern_count / 2))
        relationship_strain = min(pattern_count, 5)
        energy_drain = min(int(30 + (intensity_avg * 10) + (pattern_count * 5)), 80)
        
        return {
            'time_hours': time_hours,
            'opportunities': opportunities, 
            'relationship_strain': relationship_strain,
            'energy_drain': energy_drain
        }
    
    def _calculate_lifetime_costs(self, pattern_scores, assessment_data):
        """Calculate estimated lifetime costs of patterns"""
        if not pattern_scores:
            return {'total_5_year': 0, 'lost_opportunities': 0, 'stress_costs': 0, 
                   'relationship_costs': 0, 'happiness_hours': 0, 'relationship_quality': 0,
                   'career_impact': 0, 'health_impact': 0}
        
        pattern_count = len(pattern_scores)
        intensity_avg = sum(pattern_scores.values()) / len(pattern_scores)
        
        # Financial calculations (conservative estimates)
        lost_opportunities = pattern_count * intensity_avg * 2000  # Career/business opportunities
        stress_costs = pattern_count * 1500  # Health, therapy, stress management
        relationship_costs = min(pattern_count * 800, 5000)  # Relationship counseling, social costs
        
        total_5_year = int((lost_opportunities + stress_costs + relationship_costs) * 5)
        
        # Life satisfaction calculations
        happiness_hours = int(pattern_count * intensity_avg * 50)  # Hours per year
        relationship_quality = min(int(pattern_count * 8), 40)  # Percentage reduction
        career_impact = min(int(pattern_count * 6), 30)  # Percentage limitation
        health_impact = min(int(pattern_count * 0.5), 3)  # Years of stress impact
        
        return {
            'total_5_year': total_5_year,
            'lost_opportunities': int(lost_opportunities * 5),
            'stress_costs': int(stress_costs * 5),
            'relationship_costs': int(relationship_costs * 5),
            'happiness_hours': happiness_hours,
            'relationship_quality': relationship_quality,
            'career_impact': career_impact,
            'health_impact': health_impact
        }
    
    def _extract_future_vision(self, assessment_data):
        """Extract user's future vision from assessment responses"""
        responses = assessment_data.get('assessment_responses', {})
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            if isinstance(response, str) and any(keyword in question_text.lower() 
                                               for keyword in ['completely resolved', 'different about your daily life', 'first thing you\'d do']):
                if len(response.strip()) > 20:
                    return response.strip()[:200] + "..." if len(response.strip()) > 200 else response.strip()
        
        return "Living authentically without the constraints of automatic behavioral patterns"
    
    def _calculate_pattern_specific_cost(self, pattern_id, score):
        """Calculate specific cost for individual patterns"""
        base_costs = {
            1: "6-10 hours weekly of joy-blocking and success sabotage",
            2: "4-8 hours weekly managing conflicts and relationship stress", 
            3: "5-9 hours weekly analyzing others and maintaining defensive barriers",
            4: "3-7 hours weekly stuck in indecision and either/or thinking",
            5: "8-12 hours weekly of compulsive doing and productivity pressure",
            6: "4-8 hours weekly managing multiple personas and identity confusion",
            7: "6-10 hours weekly giving to others while neglecting self-care",
            8: "3-6 hours weekly internal conflict between personal desires and family expectations",
            9: "4-8 hours weekly boundary violations and inconsistent self-advocacy"
        }
        
        return base_costs.get(pattern_id, "4-8 hours weekly managing this behavioral pattern")
    
    def _render_compound_cost_chart(self, costs):
        """Render compound cost visualization"""
        # Create a simple progression chart
        years = [1, 2, 3, 5, 10]
        cumulative_hours = [costs['time_hours'] * 52 * year for year in years]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years,
            y=cumulative_hours,
            mode='lines+markers',
            name='Cumulative Time Cost',
            line=dict(color='#ef4444', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Cumulative Time Cost of Unchanged Patterns",
            xaxis_title="Years",
            yaxis_title="Total Hours Lost",
            height=300,
            margin=dict(l=0, r=0, t=40, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)

    def _identify_intervention_points(self, sequence):
        """Identify key intervention points in the trigger sequence"""
        intervention_points = []
        
        # Physical awareness point
        if sequence.get('physical') and sequence['physical'] != 'Physical sensation':
            intervention_points.append("Physical sensation awareness")
        
        # Thought interruption point  
        if sequence.get('thought') and sequence['thought'] != 'Automatic thought pattern':
            intervention_points.append("Automatic thought interruption")
        
        # Behavioral choice point
        if sequence.get('behavior') and sequence['behavior'] != 'Behavioral pattern':
            intervention_points.append("Behavioral response choice")
        
        # Always include these standard points
        if len(intervention_points) < 3:
            intervention_points.extend(["Pattern recognition point", "Response choice point", "Future outcome consideration"])
        
        return intervention_points[:4]  # Return max 4 points
    
    def render_your_exact_trigger_sequence(self, assessment_data):
        """Render detailed trigger sequence analysis"""
        st.markdown("**Your exact trigger sequence decoded**")
        
        trigger_analysis = self._create_personalized_trigger_analysis(assessment_data)
        sequence = trigger_analysis['sequence']
        intervention_points = trigger_analysis['intervention_points']
        
        st.markdown(f"""
        **Your complete behavioral chain:**
        
        1. **Environmental trigger:** {sequence['trigger']}
        2. **First awareness:** {sequence['awareness_point']}  
        3. **Physical response:** {sequence['physical']}
        4. **Automatic thought:** "{sequence['thought']}"
        5. **Emotional cascade:** {sequence['emotion']}
        6. **Protective behavior:** {sequence['behavior']}
        7. **Immediate consequence:** {sequence['consequence']}
        8. **Pattern reinforcement:** {sequence['reinforcement']}
        
        **Intervention opportunity points:** {len(intervention_points)} specific moments where we can install new responses
        """)
    
    def render_why_hypnotherapy_works_for_you(self, assessment_data):
        """Personalized version of why hypnotherapy works"""
        st.markdown("**Why hypnotherapy will work specifically for your patterns**")
        
        # Use existing method but add personalization
        self.render_why_hypnotherapy_works(assessment_data)
    
    def render_your_specific_next_steps(self, assessment_data):
        """Personalized next steps"""
        st.markdown("**Your specific next steps**")
        
        # Use existing method
        self.render_next_steps_and_access(assessment_data)

    def _identify_hidden_mechanisms(self, assessment_data):
        """Identify hidden protective mechanisms"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        mechanisms = []
        
        mechanism_map = {
            1: "Happiness deflection to avoid disappointment and maintain familiar identity",
            2: "Control seeking through conflict to prevent vulnerability and maintain power",
            3: "Preemptive rejection and suspicion to avoid potential abandonment",
            4: "Binary thinking to simplify overwhelming complexity and reduce anxiety",
            5: "Achievement addiction to earn worth and prove value to self and others",
            6: "Identity shifting to avoid rejection and maintain acceptance in all groups",
            7: "Self-sacrifice to maintain connection and avoid guilt about selfishness",
            8: "Mission inheritance to avoid family conflict and maintain loyalty bonds",
            9: "Boundary collapse to avoid confrontation and maintain harmony"
        }
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            for pattern_id, score in sorted_patterns:
                if score >= 3:
                    mechanisms.append(mechanism_map.get(pattern_id, "Protective response pattern"))
        
        return mechanisms[:4]  # Return top 4 mechanisms
    
    def _identify_protective_functions(self, assessment_data):
        """Identify what patterns are trying to protect"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return ["Emotional safety", "Social acceptance"]
        
        functions = set()
        function_map = {
            1: "Protection from disappointment",
            2: "Protection from vulnerability", 
            3: "Protection from abandonment",
            4: "Protection from overwhelming complexity",
            5: "Protection from worthlessness",
            6: "Protection from rejection",
            7: "Protection from guilt and selfishness",
            8: "Protection from family conflict",
            9: "Protection from confrontation"
        }
        
        for pattern_id, score in pattern_scores.items():
            if score >= 3:
                functions.add(function_map.get(pattern_id, "Protection from emotional pain"))
        
        return list(functions)[:3]  # Return top 3 functions
    
    def _identify_paradoxes(self, assessment_data):
        """Identify the key paradoxes keeping visitor stuck"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        paradoxes = [
            "The harder you try to change consciously, the more your unconscious resists to 'protect' you",
            "Your patterns were created to solve problems, but now they're creating the very problems they were meant to prevent",
            "The behaviors that once kept you safe are now preventing you from getting what you want most"
        ]
        
        if pattern_scores:
            top_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            
            specific_paradoxes = {
                1: "Protecting yourself from disappointment is preventing you from experiencing genuine happiness",
                2: "Fighting for control through conflict is causing you to lose control of your relationships",
                3: "Protecting yourself from betrayal is preventing you from forming the trusting relationships you crave",
                4: "Trying to avoid making the wrong choice is preventing you from making any empowering choices",
                5: "Working to prove your worth is preventing you from feeling inherently valuable",
                6: "Adapting to fit in everywhere is preventing you from belonging authentically anywhere",
                7: "Taking care of everyone else is preventing you from getting the care and support you need",
                8: "Trying to please your family is preventing you from living the life that would make you truly happy",
                9: "Avoiding confrontation is creating more conflict and resentment in your relationships"
            }
            
            if top_pattern in specific_paradoxes:
                paradoxes.insert(0, specific_paradoxes[top_pattern])
        
        return paradoxes[:3]
    
    def _generate_detailed_future_prediction(self, assessment_data):
        """Generate detailed future trajectory prediction"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        pattern_count = len(pattern_scores)
        
        if pattern_count >= 4:
            return "Based on this complex pattern constellation, without intervention these protective mechanisms typically strengthen and multiply over time, creating increasing life restriction, relationship difficulties, and a sense of being trapped in patterns you can see but can't change. The window for easier change narrows as patterns become more entrenched."
        elif pattern_count >= 2:
            return "These interconnected patterns tend to become more automatic and unconscious without conscious intervention, gradually limiting life satisfaction, authentic relationships, and personal growth. Change becomes more challenging as neural pathways strengthen through repetition."
        else:
            return "This pattern will likely solidify further without intervention, becoming more automatic and harder to change. What feels manageable now typically becomes more restrictive over time as the pattern generalizes to more life areas."
    
    def _calculate_session_plan(self, pattern_scores, digital_analysis):
        """Calculate personalized session plan"""
        pattern_count = len(pattern_scores) if pattern_scores else 0
        digital_severity = digital_analysis.get('severity_level', 'MINIMAL') if digital_analysis else 'MINIMAL'
        
        # Determine session structure
        if pattern_count >= 5 or digital_severity in ['SEVERE', 'MODERATE']:
            total_sessions = "2-3 sessions"
            timeline = "3-4 weeks"
            session_3_probability = 60
            success_rate = 85
        elif pattern_count >= 3:
            total_sessions = "2 sessions"
            timeline = "2-3 weeks" 
            session_3_probability = 25
            success_rate = 88
        else:
            total_sessions = "2 sessions"
            timeline = "2 weeks"
            session_3_probability = 15
            success_rate = 92
        
        # Success factors analysis
        success_factors = {
            "Pattern complexity": max(50, 100 - (pattern_count * 8)),
            "Assessment engagement": 85,  # High for completing full assessment
            "Digital adaptation": 90 if digital_severity in ['MINIMAL', 'MILD'] else 75,
            "Change readiness": 80,  # Default, could be extracted from responses
            "Therapeutic alliance": 90  # High for hypnotherapy approach
        }
        
        # Session phases
        phases = [
            {
                "title": "Deep pattern analysis & rapport building",
                "duration": "Session 1 (90 minutes)",
                "description": "Complete behavioral sequence mapping, unconscious belief identification, protective function analysis, and initial positive programming to prepare your unconscious mind for change.",
                "outcome": "Clear understanding of your pattern origins, therapeutic alliance established, and initial neural pathway preparation completed."
            },
            {
                "title": "Core transformation & neural rewiring",
                "duration": "Session 2 (90 minutes)",
                "description": "Direct pattern interruption using theta brainwave states, installation of new empowering response patterns, integration of authentic identity, and future scenario testing to ensure lasting change.",
                "outcome": "Fundamental shifts in automatic responses, new positive patterns anchored at the unconscious level, and immediate access to new behavioral choices."
            }
        ]
        
        if session_3_probability > 30:
            phases.append({
                "title": "Integration & mastery reinforcement",
                "duration": f"Session 3 if needed ({session_3_probability}% probability)",
                "description": "Advanced pattern reinforcement, fine-tuning of responses, resolution of any remaining resistance, and long-term stability anchoring for sustainable transformation.",
                "outcome": "Complete integration across all life contexts, mastery of new patterns, and sustained transformation confidence with ongoing evolution capacity."
            })
        
        return {
            'total_sessions': total_sessions,
            'timeline': timeline,
            'success_rate': success_rate,
            'success_factors': success_factors,
            'phases': phases,
            'session_3_probability': session_3_probability
        }
    
    def _extract_readiness_indicators(self, assessment_data):
        """Extract readiness indicators from assessment data"""
        indicators = []
        
        # Assessment completion
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.9:
            indicators.append(f"High assessment engagement ({completion_rate*100:.0f}% completion)")
        
        # Pattern recognition
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) >= 2:
            indicators.append("Strong pattern recognition ability demonstrated")
        
        # Response quality
        responses = assessment_data.get('assessment_responses', {})
        detailed_responses = 0
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and len(response.strip()) > 50:
                detailed_responses += 1
        
        if detailed_responses >= 3:
            indicators.append("Thoughtful, self-reflective responses showing introspection capacity")
        
        # Readiness score if available
        for response_data in responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                readiness = response_data['response']['rating']
                if readiness >= 7:
                    indicators.append(f"High change readiness score ({readiness}/10)")
                break
        
        # Motivation indicators
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                if any(phrase in response.lower() for phrase in ['want to change', 'ready for', 'tired of', 'need to']):
                    indicators.append("Clear motivation and desire for change expressed")
                    break
        
        # Digital native advantages
        if assessment_data.get('is_digital_native'):
            indicators.append("Digital-native neuroplasticity advantages for rapid change")
        
        # Default indicators if none found
        if not indicators:
            indicators = [
                "Completion of comprehensive assessment shows commitment to change",
                "Willingness to explore unconscious patterns demonstrates readiness"
            ]
        
        return indicators[:5]  # Return top 5 indicators
    
    def _identify_transformation_assets(self, assessment_data):
        """Identify visitor's existing assets for transformation"""
        assets = []
        
        # Intelligence and insight
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) >= 3:
            assets.append("High emotional intelligence and pattern recognition ability")
        
        # Completion demonstrates persistence
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.8:
            assets.append("Demonstrated persistence and commitment to understanding yourself")
        
        # Self-awareness
        responses = assessment_data.get('assessment_responses', {})
        self_aware_responses = 0
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and any(word in response.lower() for word in ['realize', 'notice', 'aware', 'recognize']):
                self_aware_responses += 1
        
        if self_aware_responses >= 2:
            assets.append("Strong self-awareness and ability to observe your own patterns")
        
        # Communication skills
        detailed_responses = sum(1 for response_data in responses.values() 
                               if isinstance(response_data.get('response'), str) and len(response_data.get('response', '').strip()) > 30)
        
        if detailed_responses >= 4:
            assets.append("Excellent communication and self-expression abilities")
        
        # Analytical thinking
        if pattern_scores:
            assets.append("Strong analytical thinking that can be redirected from self-criticism to self-development")
        
        # Digital competencies
        if assessment_data.get('is_digital_native'):
            assets.append("Digital competencies that can transfer to real-world confidence")
        
        # Courage to seek help
        assets.append("Courage to seek help and willingness to explore new approaches")
        
        # Default assets
        if len(assets) < 3:
            assets.extend([
                "Natural problem-solving abilities",
                "Capacity for insight and self-reflection",
                "Existing coping strategies that show resilience"
            ])
        
        return assets[:6]  # Return top 6 assets
    
    def _calculate_success_predictors(self, assessment_data):
        """Calculate specific success predictors for this visitor"""
        predictors = {}
        
        # Pattern complexity factor
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        if pattern_count <= 2:
            predictors["Pattern complexity"] = 95
        elif pattern_count <= 4:
            predictors["Pattern complexity"] = 85
        else:
            predictors["Pattern complexity"] = 75
        
        # Assessment engagement
        completion_rate = assessment_data.get('completion_rate', 0)
        predictors["Assessment engagement"] = min(100, int(completion_rate * 100 + 10))
        
        # Self-awareness level
        responses = assessment_data.get('assessment_responses', {})
        detailed_responses = sum(1 for response_data in responses.values() 
                               if isinstance(response_data.get('response'), str) and len(response_data.get('response', '').strip()) > 40)
        
        total_responses = len(responses)
        if total_responses > 0:
            awareness_score = min(100, int((detailed_responses / total_responses) * 100 + 30))
        else:
            awareness_score = 70
        predictors["Self-awareness level"] = awareness_score
        
        # Change readiness
        readiness_score = 75  # Default
        for response_data in responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                readiness = response_data['response']['rating']
                readiness_score = min(100, readiness * 10 + 20)
                break
        predictors["Change readiness"] = readiness_score
        
        # Digital adaptation factor
        if assessment_data.get('is_digital_native'):
            digital_analysis = assessment_data.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                if severity == 'MINIMAL':
                    predictors["Digital adaptation"] = 95
                elif severity == 'MILD':
                    predictors["Digital adaptation"] = 88
                elif severity == 'MODERATE':
                    predictors["Digital adaptation"] = 80
                else:  # SEVERE
                    predictors["Digital adaptation"] = 75
            else:
                predictors["Digital adaptation"] = 90
        else:
            predictors["Digital adaptation"] = 92
        
        # Therapeutic fit
        predictors["Hypnotherapy fit"] = 90  # High for pattern-based issues
        
        return predictors
    
    def _extract_personal_language(self, assessment_data):
        """Extract client's actual words and metaphors from responses"""
        responses = assessment_data.get('assessment_responses', {})
        personal_phrases = []
        emotional_language = []
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and len(response.strip()) > 20:
                # Extract meaningful phrases (first-person language)
                if any(word in response.lower() for word in ['i feel', 'i think', 'i notice', 'i want']):
                    personal_phrases.append(response.strip())
                
                # Extract emotional language
                emotion_words = ['anxious', 'frustrated', 'stuck', 'overwhelmed', 'tired', 'afraid']
                for word in emotion_words:
                    if word in response.lower():
                        emotional_language.append(word)
        
        return {
            'personal_phrases': personal_phrases[:3],
            'emotional_language': list(set(emotional_language))
        }
    
    def _create_personalized_trigger_analysis(self, assessment_data):
        """Create detailed trigger sequence using client's actual responses"""
        trigger_chain = assessment_data.get('trigger_chain', {})
        intensity_data = assessment_data.get('intensity_responses', {})
        
        # Build complete sequence with client's words
        sequence = {
            'trigger': trigger_chain.get('trigger', 'Situation needs exploration'),
            'awareness_point': trigger_chain.get('awareness_point', 'Body or thought awareness'),
            'physical': trigger_chain.get('physical_response', 'Physical sensation'),
            'thought': trigger_chain.get('automatic_thought', 'Automatic thought pattern'),
            'emotion': trigger_chain.get('emotional_response', 'Emotional response'),
            'behavior': trigger_chain.get('behavioral_response', 'Behavioral pattern'),
            'consequence': trigger_chain.get('immediate_consequence', 'Immediate outcome'),
            'reinforcement': trigger_chain.get('longer_term_impact', 'Pattern reinforcement')
        }
        
        # Add intensity weighting
        avg_intensity = sum(intensity_data.values()) / len(intensity_data) if intensity_data else 5
        
        return {
            'sequence': sequence,
            'intensity_level': avg_intensity,
            'intervention_points': self._identify_intervention_points(sequence)
        }
        
    def _generate_speaking_to_you_insights(self, assessment_data):
        """Generate insights using client's actual language and responses"""
        personal_lang = self._extract_personal_language(assessment_data)
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return {}
        
        dominant_pattern_id = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        # Use client's emotional language in insights
        emotional_context = personal_lang['emotional_language']
        personal_phrases = personal_lang['personal_phrases']
        
        speaking_insights = {
            'recognition': f"When you mentioned feeling {', '.join(emotional_context[:2]) if emotional_context else 'stuck'}, this perfectly describes the {self.patterns[dominant_pattern_id]} pattern in action.",
            'validation': f"Your awareness that {personal_phrases[0][:100] if personal_phrases else 'these patterns affect your daily life'} shows remarkable self-insight.",
            'breakthrough': f"The fact that you can articulate {personal_phrases[1][:100] if len(personal_phrases) > 1 else 'your experience so clearly'} means you're already 60% of the way to transformation."
        }
        
        return speaking_insights



    def _extract_complete_trigger_analysis(self, assessment_data):
        """Extract and analyze complete trigger sequence with intensity weighting"""
        responses = assessment_data.get('assessment_responses', {})
        intensity_data = assessment_data.get('intensity_responses', {})
        
        # Extract complete 8-step sequence with client's exact words
        trigger_sequence = {
            'environmental_trigger': self._extract_response_by_keywords(responses, ['30 seconds', 'happening']),
            'first_awareness': self._extract_response_by_keywords(responses, ['notice first']),
            'physical_sensation': self._extract_response_by_keywords(responses, ['physical sensation']),
            'automatic_thought': self._extract_response_by_keywords(responses, ['thought automatically']),
            'emotional_cascade': self._extract_response_by_keywords(responses, ['typically feel']),
            'behavioral_response': self._extract_response_by_keywords(responses, ['you typically:']),
            'immediate_consequence': self._extract_response_by_keywords(responses, ['right after']),
            'long_term_impact': self._extract_response_by_keywords(responses, ['few hours later'])
        }
        
        # Calculate intensity per step
        intensity_mapping = {}
        for step, content in trigger_sequence.items():
            related_q_id = self._find_question_id_for_content(responses, content)
            if related_q_id and related_q_id in intensity_data:
                intensity_mapping[step] = intensity_data[related_q_id]
            else:
                intensity_mapping[step] = 5  # Default
        
        return {
            'sequence': trigger_sequence,
            'intensity_map': intensity_mapping,
            'highest_intensity_step': max(intensity_mapping.items(), key=lambda x: x[1]),
            'intervention_windows': self._calculate_intervention_windows(trigger_sequence, intensity_mapping)
        }
    
    def _extract_digital_component_analysis(self, assessment_data):
        """Detailed analysis of each digital conditioning component"""
        digital_analysis = assessment_data.get('digital_despair_analysis', {})
        if not digital_analysis:
            return None
        
        components = digital_analysis.get('component_scores', {})
        responses = assessment_data.get('digital_responses', {})
        
        component_details = {}
        
        # Map each component to specific responses and interventions
        component_map = {
            'reality_dissociation': {
                'questions': [2],  # Authenticity question
                'intervention': 'Offline confidence transfer protocols',
                'timeline': '2-3 sessions for integration'
            },
            'ironic_detachment': {
                'questions': [4],  # Emotional expression question
                'intervention': 'Authentic emotion permission installation',
                'timeline': '1-2 sessions for breakthrough'
            },
            'attention_fragmentation': {
                'questions': [8],  # Attention span question
                'intervention': 'Focused attention restoration therapy',
                'timeline': '2-4 weeks for stabilization'
            }
        }
        
        for component, score in components.items():
            if component in component_map and score >= 2:
                details = component_map[component]
                related_responses = [responses.get(q_id, '') for q_id in details['questions']]
                
                component_details[component] = {
                    'score': score,
                    'severity': 'High' if score >= 4 else 'Moderate',
                    'client_responses': related_responses,
                    'intervention': details['intervention'],
                    'timeline': details['timeline'],
                    'success_indicators': self._generate_success_indicators(component, score)
                }
        
        return component_details
    
    def _extract_pattern_emergence_data(self, assessment_data):
        """Analyze how patterns emerged during assessment"""
        triggered_patterns = assessment_data.get('triggered_patterns', set())
        adaptive_paths = assessment_data.get('adaptive_paths', [])
        pattern_scores = assessment_data.get('pattern_scores', {})
        phase_progress = assessment_data.get('phase_completion', {})
        
        emergence_analysis = {
            'pattern_discovery_order': [],
            'resistance_indicators': [],
            'engagement_patterns': [],
            'therapeutic_readiness': {}
        }
        
        # Analyze pattern discovery order
        for path in adaptive_paths:
            if 'pattern_' in path:
                pattern_id = int(path.split('_')[1])
                if pattern_id in pattern_scores:
                    emergence_analysis['pattern_discovery_order'].append({
                        'pattern_id': pattern_id,
                        'pattern_name': self.patterns[pattern_id],
                        'final_score': pattern_scores[pattern_id],
                        'discovery_phase': self._determine_discovery_phase(path, phase_progress)
                    })
        
        # Analyze engagement patterns
        total_questions = sum(phase_progress.values())
        if total_questions >= 20:
            engagement_level = 'High'
        elif total_questions >= 15:
            engagement_level = 'Moderate'
        else:
            engagement_level = 'Low'
        
        emergence_analysis['engagement_patterns'] = {
            'level': engagement_level,
            'total_questions': total_questions,
            'completion_rate': assessment_data.get('completion_rate', 0),
            'phase_distribution': phase_progress
        }
        
        return emergence_analysis
    
    def _extract_emotional_intensity_profile(self, assessment_data):
        """Create detailed emotional intensity analysis"""
        intensity_responses = assessment_data.get('intensity_responses', {})
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        
        intensity_profile = {
            'emotional_volatility': 0,
            'pattern_intensity_map': {},
            'intervention_priority': [],
            'emotional_regulation_needs': []
        }
        
        if not intensity_responses:
            return intensity_profile
        
        # Calculate emotional volatility (variance in intensity responses)
        intensities = list(intensity_responses.values())
        avg_intensity = sum(intensities) / len(intensities)
        variance = sum((x - avg_intensity) ** 2 for x in intensities) / len(intensities)
        intensity_profile['emotional_volatility'] = variance
        
        # Map patterns to their intensity levels
        for pattern_id, score in pattern_scores.items():
            pattern_intensities = []
            for q_id, intensity in intensity_responses.items():
                # Find questions related to this pattern
                if self._question_relates_to_pattern(q_id, pattern_id, responses):
                    pattern_intensities.append(intensity)
            
            if pattern_intensities:
                avg_pattern_intensity = sum(pattern_intensities) / len(pattern_intensities)
                intensity_profile['pattern_intensity_map'][pattern_id] = {
                    'average_intensity': avg_pattern_intensity,
                    'pattern_name': self.patterns[pattern_id],
                    'regulation_need': 'High' if avg_pattern_intensity >= 6 else 'Moderate' if avg_pattern_intensity >= 4 else 'Low'
                }
        
        # Create intervention priority based on intensity + pattern score
        priority_list = []
        for pattern_id in pattern_scores:
            if pattern_id in intensity_profile['pattern_intensity_map']:
                combined_score = (pattern_scores[pattern_id] * 
                                intensity_profile['pattern_intensity_map'][pattern_id]['average_intensity'])
                priority_list.append((pattern_id, combined_score))
        
        intensity_profile['intervention_priority'] = sorted(priority_list, key=lambda x: x[1], reverse=True)
        
        return intensity_profile
    
    def render_complete_trigger_breakdown(self, assessment_data):
        """Render comprehensive trigger analysis using all available data"""
        trigger_analysis = self._extract_complete_trigger_analysis(assessment_data)
        
        st.markdown("**Your complete neurological trigger sequence**")
        
        sequence = trigger_analysis['sequence']
        intensity_map = trigger_analysis['intensity_map']
        highest_intensity = trigger_analysis['highest_intensity_step']
        
        st.markdown(f"""
        **Your personalized 8-step behavioral chain:**
        
        **Environmental trigger moment:** "{sequence['environmental_trigger']}"
        *Neurological note: Amygdala activation begins here*
        
        **First conscious awareness:** {sequence['first_awareness']}
        *Intensity: {intensity_map.get('first_awareness', 5)}/7*
        
        **Physical sensation cascade:** {sequence['physical_sensation']}
        *Intensity: {intensity_map.get('physical_sensation', 5)}/7 - Sympathetic nervous system activation*
        
        **Automatic thought pattern:** "{sequence['automatic_thought']}"
        *This represents your subconscious protective programming*
        
        **Emotional flood:** {sequence['emotional_cascade']}
        *Limbic system fully engaged - prefrontal cortex going offline*
        
        **Protective behavior:** {sequence['behavioral_response']}
        *Your unconscious solution to perceived threat*
        
        **Immediate consequence:** {sequence['immediate_consequence']}
        
        **Pattern reinforcement:** {sequence['long_term_impact']}
        *How your brain learns this sequence is "effective"*
        """)
        
        # Highlight highest intensity intervention point
        st.markdown(f"""
        <div class="breakthrough-card">
        <h4 style="margin-top: 0;">Prime intervention window identified</h4>
        <p><strong>Highest intensity step:</strong> {highest_intensity[0].replace('_', ' ').title()}</p>
        <p><strong>Intensity level:</strong> {highest_intensity[1]}/7</p>
        <p><strong>Why this matters:</strong> This is where your nervous system is most activated and where therapeutic intervention will be most effective. We'll install new response patterns at this exact moment in your sequence.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Specific intervention windows
        intervention_windows = trigger_analysis['intervention_windows']
        st.markdown("**Your specific intervention opportunities:**")
        for i, window in enumerate(intervention_windows, 1):
            st.markdown(f"""
            **{i}. {window['name']}**
            - Timing: {window['timing']}
            - Success probability: {window['success_rate']}%
            - Technique: {window['technique']}
            """)
    
    def render_digital_component_mastery_plan(self, assessment_data):
        """Detailed intervention plan for each digital component"""
        component_analysis = self._extract_digital_component_analysis(assessment_data)
        
        if not component_analysis:
            return
        
        st.markdown("**Digital conditioning component-by-component transformation plan**")
        
        for component, details in component_analysis.items():
            component_name = component.replace('_', ' ').title()
            
            st.markdown(f"""
            <div class="insight-card">
            <h4 style="color: #273548;">{component_name} - {details['severity']} Impact</h4>
            <p><strong>Your specific responses:</strong> "{details['client_responses'][0] if details['client_responses'] else 'Data not available'}"</p>
            <p><strong>Current score:</strong> {details['score']}/5</p>
            <p><strong>Targeted intervention:</strong> {details['intervention']}</p>
            <p><strong>Expected timeline:</strong> {details['timeline']}</p>
            <p><strong>Success indicators you'll notice:</strong></p>
            <ul>
            """, unsafe_allow_html=True)
            
            for indicator in details['success_indicators']:
                st.markdown(f"<li>{indicator}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
    
    def render_pattern_emergence_insights(self, assessment_data):
        """Show how patterns emerged during assessment"""
        emergence_data = self._extract_pattern_emergence_data(assessment_data)
        
        st.markdown("**How your patterns revealed themselves during assessment**")
        
        # Pattern discovery timeline
        discovery_order = emergence_data['pattern_discovery_order']
        if discovery_order:
            st.markdown("**Pattern emergence sequence:**")
            for i, pattern_info in enumerate(discovery_order, 1):
                st.markdown(f"""
                **{i}. {pattern_info['pattern_name']}**
                - Discovered in: {pattern_info['discovery_phase']} phase
                - Final intensity: {pattern_info['final_score']:.1f}/10
                - Therapeutic implication: {'Priority intervention' if pattern_info['final_score'] >= 6 else 'Secondary focus'}
                """)
        
        # Engagement analysis for therapeutic planning
        engagement = emergence_data['engagement_patterns']
        st.markdown(f"""
        **Your therapeutic engagement profile:**
        - Assessment engagement: {engagement['level']} 
        - Questions completed: {engagement['total_questions']}
        - Completion rate: {engagement['completion_rate']*100:.0f}%
        - Predicted therapy alliance: {'Strong' if engagement['level'] == 'High' else 'Good' if engagement['level'] == 'Moderate' else 'Requires building'}
        """)
    
    def render_emotional_intensity_analysis(self, assessment_data):
        """Render detailed emotional intensity insights"""
        intensity_profile = self._extract_emotional_intensity_profile(assessment_data)
        
        st.markdown("**Your emotional intensity profile and regulation needs**")
        
        # Emotional volatility analysis
        volatility = intensity_profile['emotional_volatility']
        if volatility > 2:
            volatility_desc = "High emotional volatility - rapid intensity changes"
            regulation_approach = "Stabilization and grounding techniques essential"
        elif volatility > 1:
            volatility_desc = "Moderate emotional volatility - some intensity fluctuation"
            regulation_approach = "Standard emotional regulation with intensity awareness"
        else:
            volatility_desc = "Low emotional volatility - consistent intensity levels"
            regulation_approach = "Standard therapeutic approach suitable"
        
        st.markdown(f"""
        **Emotional regulation analysis:**
        - Volatility pattern: {volatility_desc}
        - Therapeutic approach: {regulation_approach}
        """)
        
        # Pattern-specific intensity mapping
        pattern_intensity_map = intensity_profile['pattern_intensity_map']
        if pattern_intensity_map:
            st.markdown("**Pattern-specific emotional intensity:**")
            for pattern_id, intensity_data in pattern_intensity_map.items():
                st.markdown(f"""
                - **{intensity_data['pattern_name']}**: {intensity_data['average_intensity']:.1f}/7 intensity
                  - Regulation need: {intensity_data['regulation_need']}
                """)
        
        # Intervention priority
        priority_list = intensity_profile['intervention_priority']
        if priority_list:
            st.markdown("**Therapeutic intervention priority (intensity × pattern score):**")
            for i, (pattern_id, combined_score) in enumerate(priority_list[:3], 1):
                pattern_name = self.patterns[pattern_id]
                st.markdown(f"{i}. {pattern_name} (Combined urgency score: {combined_score:.1f})")
    
    def render_neuroscience_intervention_plan(self, assessment_data):
        """Detailed neuroscience-based intervention plan"""
        trigger_analysis = self._extract_complete_trigger_analysis(assessment_data)
        intensity_profile = self._extract_emotional_intensity_profile(assessment_data)
        
        st.markdown("**Neuroscience-based intervention protocol**")
        
        # Brain region analysis
        highest_intensity = trigger_analysis['highest_intensity_step']
        brain_region_map = {
            'environmental_trigger': 'Sensory cortex and thalamus activation',
            'first_awareness': 'Prefrontal cortex recognition',
            'physical_sensation': 'Amygdala and sympathetic nervous system',
            'automatic_thought': 'Default mode network and limbic system',
            'emotional_cascade': 'Limbic system dominance, prefrontal cortex offline',
            'behavioral_response': 'Motor cortex and habit circuits',
            'immediate_consequence': 'Reward/punishment centers',
            'long_term_impact': 'Memory consolidation in hippocampus'
        }
        
        st.markdown(f"""
        **Your brain activation sequence:**
        
        **Primary intervention target:** {highest_intensity[0].replace('_', ' ').title()}
        **Brain region involved:** {brain_region_map.get(highest_intensity[0], 'Multiple regions')}
        **Intensity level:** {highest_intensity[1]}/7
        
        **Neuroplasticity intervention strategy:**
        1. **Theta wave induction** (4-8 Hz) to access optimal learning state
        2. **Pattern interruption** at {highest_intensity[0].replace('_', ' ')} moment
        3. **New pathway installation** using memory reconsolidation window
        4. **Synaptic strengthening** through repeated success visualization
        5. **Integration testing** across multiple scenario contexts
        """)
        
        # Timeline with neurological basis
        volatility = intensity_profile['emotional_volatility']
        if volatility > 2:
            timeline = "3-4 sessions (high emotional volatility requires additional stabilization)"
        elif volatility > 1:
            timeline = "2-3 sessions (moderate complexity)"
        else:
            timeline = "2 sessions (optimal neuroplasticity conditions)"
        
        st.markdown(f"""
        **Neuroplasticity timeline prediction:**
        - **Session 1:** Neural pathway mapping and initial pattern interruption
        - **24-48 hours:** Memory reconsolidation window - old patterns become labile
        - **Session 2:** New pattern installation and synaptic strengthening
        - **Week 1-2:** Neural pathway competition - new patterns establishing dominance
        - **Week 3-4:** Synaptic consolidation and automatic response integration
        
        **Total timeline:** {timeline}
        **Success probability:** {self._calculate_neuroscience_success_rate(assessment_data)}%
        """)
    
    def _extract_response_by_keywords(self, responses, keywords):
        """Extract specific responses based on question keywords"""
        for response_data in responses.values():
            question_text = response_data.get('question_text', '').lower()
            if any(keyword.lower() in question_text for keyword in keywords):
                return response_data.get('response', 'Not specified')
        return 'Assessment incomplete'
    
    def _find_question_id_for_content(self, responses, content):
        """Find question ID that matches content"""
        for q_id, response_data in responses.items():
            if response_data.get('response') == content:
                return q_id
        return None
    
    def _calculate_intervention_windows(self, trigger_sequence, intensity_mapping):
        """Calculate optimal intervention windows"""
        windows = []
        
        # Physical sensation window
        physical_intensity = intensity_mapping.get('physical_sensation', 5)
        if physical_intensity >= 5:
            windows.append({
                'name': 'Somatic Awareness Intervention',
                'timing': 'At first physical sensation',
                'success_rate': min(95, 70 + physical_intensity * 5),
                'technique': 'Body scan interruption with breathing reset'
            })
        
        # Thought interruption window  
        thought_intensity = intensity_mapping.get('automatic_thought', 5)
        if thought_intensity >= 4:
            windows.append({
                'name': 'Cognitive Pattern Interrupt',
                'timing': 'At automatic thought emergence',
                'success_rate': min(90, 60 + thought_intensity * 6),
                'technique': 'Thought stopping with positive reframe installation'
            })
        
        # Behavioral choice window
        behavior_intensity = intensity_mapping.get('behavioral_response', 5)
        windows.append({
            'name': 'Behavioral Choice Point',
            'timing': 'Before automatic behavior',
            'success_rate': min(85, 50 + behavior_intensity * 7),
            'technique': 'Pause and alternative response selection'
        })
        
        return sorted(windows, key=lambda x: x['success_rate'], reverse=True)
    
    def _determine_discovery_phase(self, adaptive_path, phase_progress):
        """Determine which phase a pattern was discovered in"""
        if 'pattern_1' in adaptive_path or 'pattern_2' in adaptive_path:
            return 'Early engagement'
        elif 'pattern_3' in adaptive_path or 'pattern_4' in adaptive_path:
            return 'Trigger mapping'
        else:
            return 'Pattern-specific questioning'
    
    def _question_relates_to_pattern(self, q_id, pattern_id, responses):
        """Check if a question relates to a specific pattern"""
        # Implementation would check question content against pattern keywords
        question_text = responses.get(q_id, {}).get('question_text', '').lower()
        
        pattern_keywords = {
            1: ['happy', 'joy', 'success', 'good things'],
            2: ['conflict', 'argument', 'disagree', 'defensive'],
            3: ['trust', 'suspicious', 'motives', 'skeptical'],
            # Add more pattern-keyword mappings
        }
        
        keywords = pattern_keywords.get(pattern_id, [])
        return any(keyword in question_text for keyword in keywords)
    
    def _generate_success_indicators(self, component, score):
        """Generate specific success indicators for digital components"""
        indicators_map = {
            'reality_dissociation': [
                'Feeling equally authentic online and offline',
                'Preferring face-to-face conversations over digital',
                'Natural eye contact during conversations'
            ],
            'ironic_detachment': [
                'Expressing genuine emotions without self-mockery',
                'Sincere enthusiasm without embarrassment',
                'Connecting emotionally with others naturally'
            ],
            'attention_fragmentation': [
                'Reading for 30+ minutes without distraction',
                'Having complete conversations without phone checking',
                'Deep focus on single tasks for extended periods'
            ]
        }
        
        return indicators_map.get(component, ['Improved well-being in this area'])
    
    def _calculate_neuroscience_success_rate(self, assessment_data):
        """Calculate success rate based on neuroplasticity factors"""
        base_rate = 85
        
        # Age factor (younger = more neuroplastic)
        # Digital native factor (faster neural adaptation)
        # Emotional volatility factor (affects learning)
        # Pattern complexity factor
        
        intensity_profile = self._extract_emotional_intensity_profile(assessment_data)
        volatility = intensity_profile['emotional_volatility']
        
        if volatility > 2:
            base_rate -= 10  # High volatility requires more stabilization
        elif volatility < 1:
            base_rate += 5   # Low volatility = stable learning environment
        
        if assessment_data.get('is_digital_native'):
            base_rate += 5   # Digital natives adapt faster
        
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        if pattern_count >= 5:
            base_rate -= 5   # More patterns = more complexity
        
        return max(75, min(95, base_rate))
    def render_complete_blueprint(self, assessment_data):
        """Enhanced blueprint using ALL assessment data"""
        self.apply_styles()
        
        # Personalized hero
        name = assessment_data.get('contact_info', {}).get('name', 'Your')
        st.markdown(f"**{name} complete neurological transformation blueprint**")
        st.markdown("*Using every data point from your comprehensive assessment*")
        
        # Enhanced sections using full data
        self.render_complete_trigger_breakdown(assessment_data)           # NEW - uses trigger_chain + intensity
        self.render_emotional_intensity_analysis(assessment_data)        # NEW - uses intensity_responses
        self.render_pattern_emergence_insights(assessment_data)          # NEW - uses adaptive_paths
        
        if assessment_data.get('is_digital_native'):
            self.render_digital_component_mastery_plan(assessment_data)   # NEW - detailed digital analysis
        
        self.render_neuroscience_intervention_plan(assessment_data)      # NEW - brain-based approach
        
        # Enhanced existing sections
        self.render_personalized_cost_analysis(assessment_data)
        self.render_detailed_pattern_insights(assessment_data)
        self.render_why_traditional_failed_you(assessment_data)
        self.render_transformation_roadmap(assessment_data)
        self.render_why_hypnotherapy_works(assessment_data)
        self.render_investment_and_value(assessment_data)
        self.render_empowerment_section(assessment_data)
        self.render_next_steps_and_access(assessment_data)

    
    # def render_complete_blueprint(self, assessment_data):
    #     """Render the complete behavioral blueprint"""
    #     self.apply_styles()
        
    #     # Hero section
    #     st.markdown("**Your complete behavioral transformation blueprint**")
    #     st.markdown("*Everything you need to understand your patterns and the path forward*")
        
    #     # Main sections
    #     self.render_pattern_cost_analysis(assessment_data)
    #     self.render_detailed_pattern_insights(assessment_data)
    #     self.render_aha_moment_bridge(assessment_data)
        
    #     # Digital insights if applicable
    #     if assessment_data.get('is_digital_native'):
    #         self.render_digital_insights(assessment_data)
        
    #     self.render_transformation_roadmap(assessment_data)
    #     self.render_why_hypnotherapy_works(assessment_data)
    #     self.render_investment_and_value(assessment_data)
    #     self.render_empowerment_section(assessment_data)
    #     self.render_next_steps_and_access(assessment_data)


# Factory function for easy import
def create_behavioral_blueprint():
    """Factory function to create behavioral blueprint component"""
    return BehavioralBlueprint()


# Usage example for integration with assessment
def render_blueprint_for_assessment(assessment_data):
    """Render blueprint using assessment data"""
    blueprint = create_behavioral_blueprint()
    blueprint.render_complete_blueprint(assessment_data)


# Standalone blueprint for testing/preview
def render_sample_blueprint():
    """Render sample blueprint with mock data for testing"""
    sample_data = {
        'pattern_scores': {1: 6.5, 2: 4.2, 5: 3.8},
        'assessment_responses': {
            10: {
                'response': 'I want to feel confident in social situations and stop second-guessing myself constantly. I want to speak up in meetings and feel comfortable being myself.',
                'question_text': 'If this issue completely resolved, what would be different about your daily life?'
            }
        },
        'is_digital_native': True,
        'digital_despair_analysis': {
            'severity_level': 'MODERATE',
            'digital_despair_score': 58,
            'component_scores': {
                'reality_dissociation': 3.2,
                'ironic_detachment': 4.1,
                'attention_fragmentation': 2.8
            }
        },
        'completion_rate': 0.92,
        'contact_info': {
            'urgency': 'Very urgent - causing daily distress'
        }
    }
    
    blueprint = create_behavioral_blueprint()
    blueprint.render_complete_blueprint(sample_data)





# # Handles client-facing detailed blueprint + client communications
# # Behind paywall, can generate client emails and PDFs

# class BehavioralBlueprint:
    
#     def render_complete_blueprint(self, processed_results):
#         """Render detailed client-facing blueprint"""
        
#         # Use pre-calculated results for display
#         self._render_pattern_insights(processed_results['pattern_analysis'])
#         self._render_cost_analysis(processed_results['impact_metrics']) 
#         self._render_transformation_roadmap(processed_results['session_plan'])
#         self._render_next_steps(processed_results['contact_info'])
        
#         # Client communication options (behind paywall)
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("Email Blueprint"):
#                 self._send_client_email(processed_results)
#         with col2:
#             if st.button("Generate PDF Report"):
#                 self._generate_pdf_report(processed_results)
    
#     def _send_client_email(self, results):
#         """Send client-friendly version of blueprint"""
#         from utils.email_handler import ClientEmailHandler
        
#         email_handler = ClientEmailHandler()
#         email_handler.send_blueprint_to_client(results)
    
#     def _generate_pdf_report(self, results):
#         """Generate PDF version of blueprint"""
#         # PDF generation logic
#         pass
