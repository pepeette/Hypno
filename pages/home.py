"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
"""
"""
Complete Home page component - Streamlit-native, no complex divs
Uses Streamlit components properly for better compatibility
"""
import streamlit as st

class HomePage:
    """Home page component using Streamlit-native elements"""
    
    def __init__(self):
        self._rendered = False
    
    def render(self):
        """Render complete home page using Streamlit components"""
        if self._rendered:
            return
        
        # Hero section with single div
        self._render_hero()
        
        # Stats section using metrics
        self._render_stats()
        
        # Authority section
        self._render_authority()
        
        # Why it works section
        self._render_why_it_works()
        
        # Testimonials section
        self._render_testimonials()
        
        # Assessment quiz
        self._render_assessment()
        
        # Final CTA
        self._render_final_cta()
        
        self._rendered = True
    
    def _render_hero(self):
        """Render hero section with single div"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 12px; padding: 3rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white; margin-bottom: 1rem; font-size: 2.2rem;">
                Transform Your Life in Just 2 Sessions
            </h1>
            <p style="color: white; font-size: 1.2rem; margin-bottom: 2rem; line-height: 1.5;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits.<br>
                <strong>85% success rate</strong> in our proven 2-session method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Button below hero
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", type="primary", use_container_width=True):
                st.success("✨ Great choice! Scroll down to start your assessment.")
                # Auto-scroll would require JavaScript, so we'll use a success message instead
    
    def _render_stats(self):
        """Render statistics using Streamlit metrics"""
        st.markdown("### 🏆 Proven Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Success Rate", 
                value="85%", 
                delta="In just 2 sessions",
                help="Complete transformation rate"
            )
        
        with col2:
            st.metric(
                label="Lives Transformed", 
                value="500+", 
                delta="Since 2014",
                help="Successful client transformations"
            )
        
        with col3:
            st.metric(
                label="Experience", 
                value="10+ Years", 
                delta="Professional practice",
                help="Licensed clinical hypnotherapist"
            )
    
    def _render_authority(self):
        """Render authority and credibility section"""
        st.markdown("---")
        st.markdown("### 🎓 Professional Expertise")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                        border-radius: 8px; border: 1px solid rgba(76, 161, 163, 0.2);">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎓</div>
                <strong>Certified</strong><br>
                <small>Clinical Hypnotherapist</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                        border-radius: 8px; border: 1px solid rgba(76, 161, 163, 0.2);">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔬</div>
                <strong>Science-Based</strong><br>
                <small>Neuroplasticity Methods</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                        border-radius: 8px; border: 1px solid rgba(76, 161, 163, 0.2);">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌍</div>
                <strong>International</strong><br>
                <small>Bangkok & Online</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                        border-radius: 8px; border: 1px solid rgba(76, 161, 163, 0.2);">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔒</div>
                <strong>Licensed</strong><br>
                <small>Fully Insured</small>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_why_it_works(self):
        """Render explanation section"""
        st.markdown("---")
        st.markdown("## 🧠 Why Our Method Works When Others Don't")
        
        # Key differentiator
        st.info("""
        **The Breakthrough Difference:** Traditional methods rely on conscious willpower (which fails 95% of the time). 
        Our method works directly with your subconscious programming - where lasting change actually happens.
        """)
        
        # Comparison columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ❌ Traditional Methods")
            st.markdown("- Target conscious mind (5% of decisions)")
            st.markdown("- Rely on willpower")
            st.markdown("- Require ongoing sessions for months/years")
            st.markdown("- High relapse rates (60-80%)")
            st.error("**Problem:** You're fighting your own programming")
        
        with col2:
            st.markdown("### ✅ Our Hypnotherapy Method")
            st.markdown("- Direct access to subconscious (95% of decisions)")
            st.markdown("- Rewire neural pathways permanently")
            st.markdown("- Just 2 sessions for lasting change")
            st.markdown("- 85% permanent success rate")
            st.success("**Result:** Your programming supports your goals")
    
    def _render_testimonials(self):
        """Render testimonials using expanders"""
        st.markdown("---")
        st.markdown("## 💬 Real Transformation Stories")
        
        # Testimonial 1
        with st.expander("🌟 Banking Director, Singapore - Anxiety Breakthrough"):
            st.markdown("*'Finally broke free from old patterns – 2 sessions changed everything.'*")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**The Challenge:**")
                st.markdown("- Performance anxiety affecting career")
                st.markdown("- Years of failed attempts with other methods")
                st.markdown("- Considering career change due to stress")
            
            with col2:
                st.markdown("**The Transformation:**")
                st.markdown("- ⏱️ 2 sessions over 10 days")
                st.markdown("- 🎯 Anxiety completely eliminated")
                st.markdown("- 🚀 Promoted within 6 months")
                st.markdown("- 💪 New confidence in presentations")
        
        # Testimonial 2
        with st.expander("🎓 Medical Student, Morocco - Study Success"):
            st.markdown("*'I was struggling with my studies abroad... now doing my specialization internship.'*")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**The Challenge:**")
                st.markdown("- Overwhelming study stress")
                st.markdown("- Concentration and focus problems")
                st.markdown("- Considering dropping out of medical school")
            
            with col2:
                st.markdown("**The Transformation:**")
                st.markdown("- ⏱️ 2 sessions in 1 week")
                st.markdown("- 🎯 Focus and confidence restored")
                st.markdown("- 🚀 Now excelling in internship")
                st.markdown("- 📚 Stress became manageable")
        
        # Testimonial 3
        with st.expander("🚭 Executive - Smoking Freedom"):
            st.markdown("*'My husband was a heavy smoker for 20 years... No more addiction.'*")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**The Challenge:**")
                st.markdown("- 20-year smoking habit")
                st.markdown("- 2 packs per day (40 cigarettes)")
                st.markdown("- All previous methods failed")
            
            with col2:
                st.markdown("**The Transformation:**")
                st.markdown("- ⏱️ 2 sessions in 3 days")
                st.markdown("- 🎯 Completely smoke-free")
                st.markdown("- 💰 Saved 30,000+ THB")
                st.markdown("- 🏃 Health dramatically improved")
    
    def _render_assessment(self):
        """Render simple assessment form"""
        st.markdown("---")
        st.markdown("## 🎯 30-Second Suitability Assessment")
        st.markdown("Discover your readiness for transformation with our science-based assessment:")
        
        with st.form("suitability_assessment"):
            # Question 1
            st.markdown("#### 🎯 What would you most like to change or improve?")
            goal = st.selectbox(
                "Choose your primary goal:",
                [
                    "Select one...",
                    "Quit smoking",
                    "Reduce anxiety", 
                    "Improve sleep",
                    "Break bad habits",
                    "Build confidence",
                    "Other"
                ],
                key="goal_select"
            )
            
            # Question 2
            st.markdown("#### ⏰ How long have you been dealing with this challenge?")
            duration = st.selectbox(
                "Choose the timeframe:",
                [
                    "Select one...",
                    "Less than 6 months",
                    "6 months to 2 years",
                    "More than 2 years",
                    "Many years"
                ],
                key="duration_select"
            )
            
            # Question 3
            st.markdown("#### 🚀 How ready are you to make this change happen?")
            readiness = st.selectbox(
                "Choose your readiness level:",
                [
                    "Select one...",
                    "Just exploring options",
                    "Somewhat ready",
                    "Very ready - I'm committed",
                    "Desperate for change"
                ],
                key="readiness_select"
            )
            
            # Submit button
            submitted = st.form_submit_button(
                "📊 Get My Suitability Score", 
                type="primary", 
                use_container_width=True
            )
            
            if submitted:
                # Check if all questions answered
                if goal == "Select one..." or duration == "Select one..." or readiness == "Select one...":
                    st.error("Please answer all questions to get your personalized score.")
                else:
                    # Calculate score and display results
                    score = self._calculate_score(goal, duration, readiness)
                    self._display_results(score, goal, duration, readiness)
    
    def _calculate_score(self, goal, duration, readiness):
        """Calculate suitability score based on responses"""
        score = 0
        
        # Goal scoring (0-40 points)
        goal_scores = {
            "Quit smoking": 40,
            "Reduce anxiety": 35,
            "Improve sleep": 30,
            "Break bad habits": 35,
            "Build confidence": 30,
            "Other": 25
        }
        score += goal_scores.get(goal, 0)
        
        # Duration scoring (0-30 points)
        duration_scores = {
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30,
            "Many years": 25
        }
        score += duration_scores.get(duration, 0)
        
        # Readiness scoring (0-30 points)
        readiness_scores = {
            "Just exploring options": 10,
            "Somewhat ready": 20,
            "Very ready - I'm committed": 30,
            "Desperate for change": 25
        }
        score += readiness_scores.get(readiness, 0)
        
        return min(score, 100)
    
    def _display_results(self, score, goal, duration, readiness):
        """Display comprehensive assessment results"""
        
        # Score display with appropriate styling
        if score >= 85:
            st.success(f"🌟 **Your Suitability Score: {score}%** - Excellent candidate!")
            message = "You're an excellent candidate for our 2-session method!"
            color = "#22c55e"
        elif score >= 70:
            st.success(f"✅ **Your Suitability Score: {score}%** - Very good fit!")
            message = "You're a very good fit for our transformation program."
            color = "#65a30d"
        elif score >= 55:
            st.warning(f"🎯 **Your Suitability Score: {score}%** - Good potential!")
            message = "You have good potential with our targeted approach."
            color = "#eab308"
        else:
            st.info(f"💬 **Your Suitability Score: {score}%** - Let's discuss your situation!")
            message = "A discovery call will help us understand how best to help you."
            color = "#4CA1A3"
        
        st.markdown(f"**{message}**")
        
        # Results breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📊 Your Assessment Profile:**")
            st.markdown(f"🎯 **Primary Goal:** {goal}")
            st.markdown(f"⏰ **Challenge Duration:** {duration}")
            st.markdown(f"🚀 **Readiness Level:** {readiness}")
        
        with col2:
            st.markdown("**💡 Personalized Insights:**")
            insights = self._get_insights(goal, duration, readiness)
            for insight in insights:
                st.markdown(f"✓ {insight}")
        
        # Recommendation section
        st.markdown("---")
        st.markdown("**🎯 Recommended Next Step:**")
        
        # Action buttons based on score
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📞 Free Discovery Call", key="results_discovery", use_container_width=True):
                st.success("✨ Excellent choice! We'll contact you within 24 hours to schedule your free consultation.")
                st.balloons()
        
        with col2:
            if score >= 70:
                if st.button("⚡ Book Sessions Now", key="results_book", use_container_width=True, type="primary"):
                    st.success("🚀 Amazing! You're ready to begin your transformation journey. Check your email for next steps.")
                    st.balloons()
            else:
                if st.button("💬 Get Personal Guidance", key="results_guidance", use_container_width=True):
                    st.success("👍 Great! A discovery call will help us create the perfect approach for your specific situation.")
        
        # Additional information based on score
        if score >= 85:
            st.info("💫 **Excellent Match:** Your profile indicates you're an ideal candidate for rapid transformation. Most clients with your profile achieve their goals in exactly 2 sessions.")
        elif score >= 70:
            st.info("⭐ **Strong Potential:** Your assessment suggests very good compatibility with our method. We're confident we can help you achieve lasting change.")
        elif score >= 55:
            st.info("🎯 **Good Foundation:** While your score shows potential, a discovery call will help us understand your specific situation and customize our approach.")
        else:
            st.info("🤝 **Let's Connect:** Every situation is unique. A brief consultation will help us determine the best path forward for your specific goals and circumstances.")
    
    def _get_insights(self, goal, duration, readiness):
        """Generate personalized insights based on assessment responses"""
        insights = []
        
        # Goal-based insights
        if "smoking" in goal.lower():
            insights.append("Smoking cessation has our highest success rate (90%+)")
            insights.append("Most clients never crave cigarettes again after 2 sessions")
        elif "anxiety" in goal.lower():
            insights.append("Anxiety often resolves quickly with our root-cause approach")
            insights.append("You'll learn to feel naturally calm in triggering situations")
        elif "sleep" in goal.lower():
            insights.append("Sleep improvements often happen after just one session")
            insights.append("We address both physical and mental sleep barriers")
        elif "habits" in goal.lower():
            insights.append("Habit change works by rewiring automatic behavioral patterns")
            insights.append("New positive habits will feel natural and effortless")
        elif "confidence" in goal.lower():
            insights.append("Confidence building through subconscious reprogramming is highly effective")
            insights.append("You'll develop unshakeable self-assurance from within")
        
        # Duration-based insights
        if "Many years" in duration:
            insights.append("Long-standing patterns often respond very well to hypnotherapy")
        elif "months" in duration:
            insights.append("You're at an ideal time for rapid transformation")
        elif "More than 2 years" in duration:
            insights.append("Your brain is ready to create new, healthier neural pathways")
        
        # Readiness-based insights
        if "committed" in readiness.lower():
            insights.append("Your commitment level indicates excellent potential for success")
        elif "desperate" in readiness.lower():
            insights.append("Your high motivation is a key predictor of success")
        elif "exploring" in readiness.lower():
            insights.append("A discovery call will help you understand the process better")
        
        # Ensure we have at least 3 insights
        default_insights = [
            "Hypnotherapy works by accessing your subconscious programming",
            "Changes happen at a neural level, making them permanent",
            "Most clients report feeling different immediately after session 1",
            "Our method has an 85% success rate in just 2 sessions",
            "You'll receive personalized techniques designed for your specific situation"
        ]
        
        # Add default insights if we don't have enough
        for default_insight in default_insights:
            if len(insights) >= 3:
                break
            if default_insight not in insights:
                insights.append(default_insight)
        
        return insights[:3]  # Return exactly 3 insights
    
    def _render_final_cta(self):
        """Render final call to action section"""
        st.markdown("---")
        
        # CTA section with single div
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    border-radius: 12px; padding: 3rem 2rem; text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem; font-size: 2rem;">
                Ready to Transform Your Life?
            </h2>
            <p style="color: white; font-size: 1.2rem; margin-bottom: 2rem; line-height: 1.5;">
                Join hundreds of people who have already transformed their lives with our proven method.<br>
                Your success story could be next.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons using Streamlit columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True, type="primary"):
                st.success("✨ Excellent choice! A discovery call is the perfect first step to understand your unique situation.")
        
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                st.success("🔬 Great! Understanding our science-backed approach helps build confidence in the process.")
        
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True, type="primary"):
                st.success("🚀 Amazing! You're ready to begin your transformation journey. Let's make it happen.")

# Factory function for creating the HomePage
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
