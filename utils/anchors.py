"""
Anchor utilities for creating navigation links and table of contents
Shared across all pages for consistent anchor link functionality
"""
import streamlit as st

class AnchorUtils:
    """Utility class for creating anchor links and navigation elements"""
    
    @staticmethod
    def create_anchor_header(text, anchor_id, level=2):
        """
        Create a header with an anchor link
        
        Args:
            text (str): Header text content
            anchor_id (str): Unique ID for the anchor (should be URL-safe)
            level (int): Header level (1, 2, or 3)
        """
        # Define header styling based on level
        if level == 1:
            tag = "h1"
            font_size = "2.2rem"
            margin_top = "2.5rem"
        elif level == 2:
            tag = "h2"
            font_size = "1.8rem"
            margin_top = "2rem"
        else:
            tag = "h3"
            font_size = "1rem"
            margin_top = "1.5rem"
            
        # Create the anchor link HTML with consistent styling
        anchor_html = f"""
        <{tag} id="{anchor_id}" style="
            font-size: {font_size};
            color: #273548;
            margin-top: {margin_top};
            margin-bottom: 1rem;
            font-weight: 600;
            scroll-margin-top: 100px;
            line-height: 1.2;
        ">
            <a href="#{anchor_id}" style="
                color: inherit;
                text-decoration: none;
                position: relative;
                display: inline-block;
            " 
            onmouseover="this.style.textDecoration='underline'; this.style.color='#4CA1A3';"
            onmouseout="this.style.textDecoration='none'; this.style.color='#273548';">
                {text}
            </a>
        </{tag}>
        """
        st.markdown(anchor_html, unsafe_allow_html=True)
    
    @staticmethod
    def create_table_of_contents(sections, title="Quick navigation"):
        """
        Create a table of contents with anchor links
        
        Args:
            sections (list): List of dicts with 'id' and 'title' keys
            title (str): TOC section title
        """
        toc_html = f"""
        <div style="
            background: white; 
            border: 1px solid #CBD5E1; 
            border-radius: 12px; 
            padding: 1.5rem; 
            margin: 2rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        ">
            <h3 style="
                color: #273548; 
                margin-bottom: 1rem; 
                font-size: 1.1rem;
                font-weight: 600;
            ">{title}</h3>
            <ul style="
                list-style: none; 
                padding: 0; 
                margin: 0;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 0.5rem;
            ">
        """
        
        for section in sections:
            toc_html += f"""
                <li style="margin: 0.3rem 0;">
                    <a href="#{section['id']}" style="
                        color: #4CA1A3;
                        text-decoration: none;
                        font-size: 0.95rem;
                        transition: all 0.2s ease;
                        display: block;
                        padding: 0.25rem 0;
                        border-radius: 4px;
                    "
                    onmouseover="this.style.color='#3B7A7A'; this.style.backgroundColor='rgba(76, 161, 163, 0.05)';"
                    onmouseout="this.style.color='#4CA1A3'; this.style.backgroundColor='transparent';">
                        {section['title']}
                    </a>
                </li>
            """
        
        toc_html += """
            </ul>
        </div>
        """
        
        st.markdown(toc_html, unsafe_allow_html=True)
    
    @staticmethod
    def add_smooth_scroll_css():
        """Add CSS for smooth scrolling and anchor behavior"""
        st.markdown("""
        <style>
        html {
            scroll-behavior: smooth;
        }
        
        /* Ensure anchors have proper spacing from top */
        [id] {
            scroll-margin-top: 100px;
        }
        
        /* Style for anchor links on hover - applies globally */
        a[href^="#"]:hover {
            text-decoration: underline !important;
            color: #4CA1A3 !important;
        }
        
        /* Smooth transition for all anchor interactions */
        a[href^="#"] {
            transition: all 0.2s ease;
        }
        
        /* Ensure TOC is responsive */
        @media (max-width: 768px) {
            .toc-grid {
                grid-template-columns: 1fr !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def create_anchor_link_button(text, anchor_id, button_type="secondary"):
        """
        Create a button that scrolls to an anchor
        
        Args:
            text (str): Button text
            anchor_id (str): Target anchor ID
            button_type (str): 'primary' or 'secondary'
        """
        button_style = "primary" if button_type == "primary" else "secondary"
        
        # JavaScript to handle smooth scrolling
        scroll_js = f"""
        <script>
        function scrollToAnchor(anchorId) {{
            const element = document.getElementById(anchorId);
            if (element) {{
                element.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                // Update URL without triggering page reload
                history.pushState(null, null, '#' + anchorId);
            }}
        }}
        </script>
        """
        
        if button_type == "primary":
            button_html = f"""
            {scroll_js}
            <button onclick="scrollToAnchor('{anchor_id}')" style="
                background: #4CA1A3;
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: background 0.2s ease;
                width: 100%;
                margin: 0.5rem 0;
            "
            onmouseover="this.style.background='#3B7A7A'"
            onmouseout="this.style.background='#4CA1A3'">
                {text}
            </button>
            """
        else:
            button_html = f"""
            {scroll_js}
            <button onclick="scrollToAnchor('{anchor_id}')" style="
                background: white;
                color: #273548;
                border: 2px solid #CBD5E1;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: all 0.2s ease;
                width: 100%;
                margin: 0.5rem 0;
            "
            onmouseover="this.style.borderColor='#4CA1A3'; this.style.color='#4CA1A3'"
            onmouseout="this.style.borderColor='#CBD5E1'; this.style.color='#273548'">
                {text}
            </button>
            """
        
        st.markdown(button_html, unsafe_allow_html=True)
    
    @staticmethod
    def create_section_divider(anchor_id=None):
        """
        Create a visual section divider with optional anchor
        
        Args:
            anchor_id (str, optional): Anchor ID for the divider
        """
        if anchor_id:
            divider_html = f"""
            <div id="{anchor_id}" style="
                margin: 3rem 0 2rem 0;
                height: 1px;
                background: linear-gradient(90deg, transparent, #CBD5E1, transparent);
                scroll-margin-top: 100px;
            "></div>
            """
        else:
            divider_html = """
            <div style="
                margin: 3rem 0 2rem 0;
                height: 1px;
                background: linear-gradient(90deg, transparent, #CBD5E1, transparent);
            "></div>
            """
        
        st.markdown(divider_html, unsafe_allow_html=True)

class PageAnchorConfig:
    """Configuration class for page-specific anchor setups"""
    
    # Method page anchors
    METHOD_PAGE_SECTIONS = [
        {"id": "hero", "title": "The transformation method"},
        {"id": "method-explanation", "title": "How neuroplasticity works"},
        {"id": "session-1", "title": "Session 1: Pattern analysis"},
        {"id": "session-2", "title": "Session 2: Neural rewiring"},
        {"id": "session-3", "title": "Session 3: Reinforcement"},
        {"id": "investment", "title": "Transformation packages"},
        {"id": "standard-package", "title": "Standard program"},
        {"id": "complete-package", "title": "Complete transformation"},
        {"id": "faq", "title": "Questions & answers"}
    ]
    
    # Home page anchors (example)
    HOME_PAGE_SECTIONS = [
        {"id": "hero", "title": "Welcome"},
        {"id": "how-it-works", "title": "How it works"},
        {"id": "testimonials", "title": "Success stories"},
        {"id": "book-now", "title": "Get started"}
    ]
    
    # Blog page anchors (example)
    BLOG_PAGE_SECTIONS = [
        {"id": "latest", "title": "Latest posts"},
        {"id": "categories", "title": "Categories"},
        {"id": "featured", "title": "Featured articles"}
    ]
    
    # Success page anchors (example)
    SUCCESS_PAGE_SECTIONS = [
        {"id": "testimonials", "title": "Client testimonials"},
        {"id": "case-studies", "title": "Case studies"},
        {"id": "statistics", "title": "Success statistics"}
    ]

# Convenience functions for common anchor patterns
def quick_toc(page_name):
    """Quick table of contents for predefined pages"""
    sections_map = {
        "method": PageAnchorConfig.METHOD_PAGE_SECTIONS,
        "home": PageAnchorConfig.HOME_PAGE_SECTIONS,
        "blog": PageAnchorConfig.BLOG_PAGE_SECTIONS,
        "success": PageAnchorConfig.SUCCESS_PAGE_SECTIONS
    }
    
    if page_name in sections_map:
        AnchorUtils.create_table_of_contents(sections_map[page_name])
    else:
        st.warning(f"No predefined sections for page: {page_name}")

def setup_page_anchors():
    """Setup anchor CSS and basic configuration for any page"""
    AnchorUtils.add_smooth_scroll_css()
