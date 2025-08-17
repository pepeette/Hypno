# """
# Navigation component for the Hypnotherapy website
# Handles main navigation menu creation and styling
# """
# import streamlit as st
# from streamlit_option_menu import option_menu
# from utils.config import AppConstants
# from utils.session_state import track_page_visit

# class Navigation:
#     """Main navigation component"""
    
#     def __init__(self):
#         self.options = AppConstants.NAVIGATION_OPTIONS
#         self.icons = AppConstants.NAVIGATION_ICONS
        
#     def create_menu(self) -> str:
#         """Create and return the main navigation menu"""
#         selected = option_menu(
#             menu_title=None,
#             options=self.options,
#             icons=self.icons,
#             default_index=0,
#             orientation="horizontal",
#             styles=self._get_navigation_styles()
#         )
        
#         # Track page visit for analytics
#         track_page_visit(selected)
        
#         return selected
    
#     def _get_navigation_styles(self) -> dict:
#         """Get navigation styling configuration"""
#         return {
#             "container": {
#                 "padding": "0",
#                 "margin": "0 0 2rem 0",
#                 "background-color": "transparent",
#                 "border-radius": "12px",
#                 "box-shadow": "0 2px 8px rgba(0,0,0,0.05)"
#             },
#             "nav-link": {
#                 "font-size": "1rem",
#                 "padding": "12px 20px",
#                 "transition": "all 0.3s ease",
#                 "border-radius": "8px",
#                 "margin": "0 4px",
#                 "color": "#556D7A",
#                 "font-weight": "500",
#                 "--hover-color": "#4CA1A3"
#             },
#             "nav-link-selected": {
#                 "background": "linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%)",
#                 "font-weight": "600",
#                 "color": "white",
#                 "border-bottom": "none",
#                 "transform": "translateY(-1px)",
#                 "box-shadow": "0 4px 12px rgba(76, 161, 163, 0.3)"
#             }
#         }
    
#     def create_breadcrumb(self, current_page: str, parent_page: str = None) -> None:
#         """Create breadcrumb navigation for sub-pages"""
#         breadcrumb_html = f"""
#         <div style="margin: 1rem 0; padding: 0.5rem 0; 
#                     border-bottom: 1px solid var(--border);">
#             <nav style="font-size: 0.9rem; color: var(--text-secondary);">
#         """
        
#         if parent_page:
#             breadcrumb_html += f"""
#                 <a href="#{parent_page.lower()}" 
#                    style="color: var(--accent); text-decoration: none;">
#                     {parent_page}
#                 </a>
#                 <span style="margin: 0 0.5rem;"> / </span>
#             """
        
#         breadcrumb_html += f"""
#                 <span style="color: var(--text-primary); font-weight: 600;">
#                     {current_page}
#                 </span>
#             </nav>
#         </div>
#         """
        
#         st.markdown(breadcrumb_html, unsafe_allow_html=True)

# class MobileNavigation:
#     """Mobile-specific navigation component"""
    
#     def __init__(self):
#         self.options = AppConstants.NAVIGATION_OPTIONS
#         self.icons = AppConstants.NAVIGATION_ICONS
    
#     def create_mobile_menu(self) -> str:
#         """Create mobile-optimized navigation menu"""
#         # Check if we're on mobile (simplified check)
#         mobile_styles = {
#             "container": {
#                 "padding": "0",
#                 "margin": "0 0 1rem 0",
#                 "background-color": "transparent"
#             },
#             "nav-link": {
#                 "font-size": "0.9rem",
#                 "padding": "8px 12px",
#                 "transition": "all 0.3s ease",
#                 "border-radius": "6px",
#                 "margin": "0 2px",
#                 "color": "#556D7A"
#             },
#             "nav-link-selected": {
#                 "background": "#4CA1A3",
#                 "font-weight": "600",
#                 "color": "white"
#             }
#         }
        
#         return option_menu(
#             menu_title=None,
#             options=self.options,
#             icons=self.icons,
#             default_index=0,
#             orientation="horizontal",
#             styles=mobile_styles
#         )

# class NavigationAnalytics:
#     """Track navigation analytics and user behavior"""
    
#     @staticmethod
#     def track_navigation_event(from_page: str, to_page: str):
#         """Track navigation between pages"""
#         if 'navigation_events' not in st.session_state:
#             st.session_state.navigation_events = []
        
#         event = {
#             'from_page': from_page,
#             'to_page': to_page,
#             'timestamp': st.session_state.get('current_time', 'unknown')
#         }
        
#         st.session_state.navigation_events.append(event)
    
#     @staticmethod
#     def get_most_visited_pages():
#         """Get analytics on most visited pages"""
#         visited_pages = st.session_state.get('page_visited', set())
#         return list(visited_pages)
    
#     @staticmethod
#     def get_navigation_flow():
#         """Get user navigation flow data"""
#         return st.session_state.get('navigation_events', [])

# class QuickActions:
#     """Quick action buttons for key user actions"""
    
#     @staticmethod
#     def render_floating_cta():
#         """Render floating call-to-action button"""
#         cta_html = """
#         <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
#             <a href="#discovery" 
#                style="display: flex; align-items: center; gap: 8px;
#                       background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
#                       color: white; text-decoration: none; padding: 12px 16px;
#                       border-radius: 25px; font-weight: 600; font-size: 0.9rem;
#                       box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4);
#                       transition: all 0.3s ease; animation: pulse 2s infinite;">
#                 <span>📞</span>
#                 <span>Free Call</span>
#             </a>
#         </div>
        
#         <style>
#         @keyframes pulse {
#             0% { box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }
#             50% { box-shadow: 0 4px 25px rgba(76, 161, 163, 0.6); }
#             100% { box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }
#         }
        
#         @media (max-width: 768px) {
#             .floating-cta {
#                 bottom: 10px;
#                 right: 10px;
#                 padding: 10px 14px;
#                 font-size: 0.8rem;
#             }
#         }
#         </style>
#         """
        
#         st.markdown(cta_html, unsafe_allow_html=True)
    
#     @staticmethod
#     def render_quick_nav_buttons():
#         """Render quick navigation buttons for key actions"""
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             if st.button("🎯 Take Quiz", key="quick_quiz", help="30-second assessment"):
#                 st.experimental_set_query_params(section="quiz")
        
#         with col2:
#             if st.button("📞 Free Call", key="quick_call", help="15-minute consultation"):
#                 st.experimental_set_query_params(section="discovery")
        
#         with col3:
#             if st.button("📅 Book Now", key="quick_book", help="Schedule sessions"):
#                 st.experimental_set_query_params(section="booking")

# def create_navigation():
#     """Factory function to create navigation instance"""
#     return Navigation()

# def create_mobile_navigation():
#     """Factory function to create mobile navigation instance"""
#     return MobileNavigation()

"""
Enhanced Navigation component with better visual design and user experience
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils.config import AppConstants
from utils.session_state import track_page_visit

class EnhancedNavigation:
    """Enhanced navigation component with modern design"""
    
    def __init__(self):
        self.options = AppConstants.NAVIGATION_OPTIONS
        self.icons = AppConstants.NAVIGATION_ICONS
        
    def create_menu(self) -> str:
        """Create enhanced navigation menu with modern styling"""
        # Add logo/brand section before menu
        self._render_brand_header()
        
        selected = option_menu(
            menu_title=None,
            options=self.options,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=self._get_enhanced_navigation_styles()
        )
        
        # Track page visit for analytics
        track_page_visit(selected)
        
        # Add navigation hints
        self._render_navigation_hints(selected)
        
        return selected
    
    def _render_brand_header(self):
        """Render brand header with logo and tagline"""
        brand_html = """
        <div style="text-align: center; margin: 1rem 0 2rem 0; padding: 1.5rem 0;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 0.5rem;">
                <div style="font-size: 2.5rem;">🧠</div>
                <div>
                    <h1 style="color: var(--accent); margin: 0; font-size: 1.8rem; font-weight: 700;">
                        Laetitia Sheppard
                    </h1>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem; font-weight: 500;">
                        Clinical Hypnotherapist • Bangkok & Online
                    </p>
                </div>
            </div>
            <div style="max-width: 600px; margin: 0 auto;">
                <p style="color: var(--text-secondary); font-size: 1rem; margin: 0; font-weight: 500;">
                    Transform your life in just 2 sessions with science-backed hypnotherapy
                </p>
            </div>
        </div>
        """
        
        st.markdown(brand_html, unsafe_allow_html=True)
    
    def _get_enhanced_navigation_styles(self) -> dict:
        """Get enhanced navigation styling configuration"""
        return {
            "container": {
                "padding": "0.5rem 1rem",
                "margin": "0 0 2rem 0",
                "background": "linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)",
                "border-radius": "15px",
                "box-shadow": "0 4px 20px rgba(0,0,0,0.08)",
                "border": "1px solid #e2e8f0"
            },
            "nav-link": {
                "font-size": "1rem",
                "padding": "12px 24px",
                "transition": "all 0.3s ease",
                "border-radius": "10px",
                "margin": "0 6px",
                "color": "#556D7A",
                "font-weight": "500",
                "position": "relative",
                "text-align": "center"
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%)",
                "font-weight": "600",
                "color": "white",
                "border": "none",
                "transform": "translateY(-2px)",
                "box-shadow": "0 6px 20px rgba(76, 161, 163, 0.3)",
                "border-radius": "10px"
            },
            "menu-icon": {
                "margin-right": "8px",
                "font-size": "1.1rem"
            }
        }
    
    def _render_navigation_hints(self, selected_page: str):
        """Render helpful navigation hints"""
        hints = {
            "Home": "🏠 Start your transformation journey",
            "Method": "🔬 Discover our proven 2-session approach", 
            "Success": "⭐ Read real client transformation stories",
            "Blog": "📚 Learn about hypnotherapy and wellness",
            "Book Now": "📅 Schedule your sessions or discovery call"
        }
        
        hint = hints.get(selected_page, "")
        if hint:
            hint_html = f"""
            <div style="text-align: center; margin: -1rem 0 2rem 0;">
                <p style="color: var(--text-secondary); font-size: 0.9rem; 
                          background: rgba(76, 161, 163, 0.05); padding: 0.5rem 1rem;
                          border-radius: 20px; display: inline-block; font-weight: 500;">
                    {hint}
                </p>
            </div>
            """
            st.markdown(hint_html, unsafe_allow_html=True)
    
    def create_breadcrumb(self, current_page: str, parent_page: str = None) -> None:
        """Create enhanced breadcrumb navigation"""
        breadcrumb_html = f"""
        <div style="margin: 1rem 0; padding: 1rem; background: var(--card-bg);
                    border-radius: var(--radius-sm); border: 1px solid var(--border);">
            <nav style="font-size: 0.9rem; color: var(--text-secondary); display: flex; align-items: center;">
                <a href="#home" style="color: var(--accent); text-decoration: none; font-weight: 500;">
                    🏠 Home
                </a>
        """
        
        if parent_page:
            breadcrumb_html += f"""
                <span style="margin: 0 0.8rem; color: var(--border);">→</span>
                <a href="#{parent_page.lower()}" 
                   style="color: var(--accent); text-decoration: none; font-weight: 500;">
                    {parent_page}
                </a>
            """
        
        breadcrumb_html += f"""
                <span style="margin: 0 0.8rem; color: var(--border);">→</span>
                <span style="color: var(--text-primary); font-weight: 600;">
                    {current_page}
                </span>
            </nav>
        </div>
        """
        
        st.markdown(breadcrumb_html, unsafe_allow_html=True)

class MobileOptimizedNavigation:
    """Mobile-optimized navigation component"""
    
    def __init__(self):
        self.options = AppConstants.NAVIGATION_OPTIONS
        self.icons = AppConstants.NAVIGATION_ICONS
    
    def create_mobile_menu(self) -> str:
        """Create mobile-optimized navigation menu"""
        mobile_styles = {
            "container": {
                "padding": "0.3rem 0.5rem",
                "margin": "0 0 1.5rem 0",
                "background": "linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)",
                "border-radius": "12px",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.06)",
                "border": "1px solid #e2e8f0"
            },
            "nav-link": {
                "font-size": "0.85rem",
                "padding": "8px 12px",
                "transition": "all 0.3s ease",
                "border-radius": "8px",
                "margin": "0 3px",
                "color": "#556D7A",
                "font-weight": "500"
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%)",
                "font-weight": "600",
                "color": "white",
                "transform": "translateY(-1px)",
                "box-shadow": "0 3px 10px rgba(76, 161, 163, 0.3)"
            },
            "menu-icon": {
                "margin-right": "6px",
                "font-size": "0.9rem"
            }
        }
        
        return option_menu(
            menu_title=None,
            options=self.options,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=mobile_styles
        )

class NavigationAnalytics:
    """Enhanced navigation analytics and user behavior tracking"""
    
    @staticmethod
    def track_user_journey(from_page: str, to_page: str, time_spent: float = 0):
        """Track detailed user journey through the site"""
        if 'user_journey' not in st.session_state:
            st.session_state.user_journey = []
        
        journey_event = {
            'from_page': from_page,
            'to_page': to_page,
            'time_spent': time_spent,
            'timestamp': st.session_state.get('current_time', 'unknown'),
            'session_id': st.session_state.get('session_id', 'unknown')
        }
        
        st.session_state.user_journey.append(journey_event)
    
    @staticmethod
    def get_popular_user_flows():
        """Analyze popular user navigation flows"""
        journey = st.session_state.get('user_journey', [])
        flows = {}
        
        for i in range(len(journey) - 1):
            flow = f"{journey[i]['from_page']} → {journey[i+1]['to_page']}"
            flows[flow] = flows.get(flow, 0) + 1
        
        return sorted(flows.items(), key=lambda x: x[1], reverse=True)
    
    @staticmethod
    def get_page_engagement_metrics():
        """Get page engagement metrics"""
        journey = st.session_state.get('user_journey', [])
        page_times = {}
        
        for event in journey:
            page = event['from_page']
            time_spent = event.get('time_spent', 0)
            if page not in page_times:
                page_times[page] = []
            page_times[page].append(time_spent)
        
        # Calculate average time per page
        avg_times = {}
        for page, times in page_times.items():
            if times:
                avg_times[page] = sum(times) / len(times)
        
        return avg_times

class ProgressIndicator:
    """Progress indicator for multi-step processes"""
    
    @staticmethod
    def render_user_progress():
        """Render user progress through the conversion funnel"""
        # Define conversion steps
        steps = [
            ("Visit", "👁️"),
            ("Engage", "🎯"), 
            ("Assess", "📝"),
            ("Contact", "📞"),
            ("Book", "⚡")
        ]
        
        # Determine current step based on user actions
        current_step = ProgressIndicator._determine_current_step()
        
        progress_html = """
        <div style="background: var(--card-bg); border-radius: var(--radius-sm); 
                    padding: 1rem; margin: 1rem 0; border: 1px solid var(--border);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        """
        
        for i, (step_name, icon) in enumerate(steps):
            completed = i < current_step
            active = i == current_step
            
            step_class = "completed" if completed else ("active" if active else "pending")
            
            progress_html += f"""
            <div style="display: flex; flex-direction: column; align-items: center; 
                       opacity: {'1' if completed or active else '0.4'};">
                <div style="width: 40px; height: 40px; border-radius: 50%; 
                           background: {'var(--success)' if completed else ('var(--accent)' if active else 'var(--border)')};
                           color: {'white' if completed or active else 'var(--text-secondary)'};
                           display: flex; align-items: center; justify-content: center; 
                           font-size: 1.2rem; margin-bottom: 0.5rem;">
                    {'✓' if completed else icon}
                </div>
                <span style="font-size: 0.8rem; font-weight: 500; 
                           color: {'var(--success)' if completed else ('var(--accent)' if active else 'var(--text-secondary)')};">
                    {step_name}
                </span>
            </div>
            """
            
            if i < len(steps) - 1:
                progress_html += f"""
                <div style="flex: 1; height: 2px; margin: 0 1rem; 
                           background: {'var(--success)' if completed else 'var(--border)'};
                           margin-top: 20px;"></div>
                """
        
        progress_html += """
            </div>
        </div>
        """
        
        st.markdown(progress_html, unsafe_allow_html=True)
    
    @staticmethod
    def _determine_current_step():
        """Determine user's current step in the conversion process"""
        # Check session state for various completion indicators
        if st.session_state.get('booking_completed', False):
            return 5  # Book
        elif st.session_state.get('contact_initiated', False):
            return 4  # Contact
        elif st.session_state.get('quiz_completed', False):
            return 3  # Assess
        elif st.session_state.get('page_engagement', 0) > 30:  # 30+ seconds engagement
            return 2  # Engage
        else:
            return 1  # Visit

# Factory functions for easy import
def create_enhanced_navigation():
    """Factory function to create EnhancedNavigation instance"""
    return EnhancedNavigation()

def create_mobile_navigation():
    """Factory function to create MobileOptimizedNavigation instance"""
    return MobileOptimizedNavigation()

def create_progress_indicator():
    """Factory function to create ProgressIndicator instance"""
    return ProgressIndicator()
