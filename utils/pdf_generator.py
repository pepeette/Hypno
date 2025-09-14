"""
Create utils/pdf_generator.py:
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from io import BytesIO
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

class PDFGenerator:
    """Generate comprehensive PDF reports from assessment data"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom styles for the PDF"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#273548'),
            alignment=TA_CENTER
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=18,
            textColor=colors.HexColor('#4CA1A3'),
            alignment=TA_LEFT
        ))
        
        # Pattern style
        self.styles.add(ParagraphStyle(
            name='PatternStyle',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=12,
            textColor=colors.HexColor('#273548'),
            alignment=TA_JUSTIFY
        ))
        
        # Insight style
        self.styles.add(ParagraphStyle(
            name='InsightStyle',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=10,
            textColor=colors.HexColor('#556D7A'),
            alignment=TA_JUSTIFY,
            leftIndent=20
        ))
    
    def generate_blueprint_pdf(self, assessment_data):
        """Generate comprehensive PDF blueprint"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build the story (content)
        story = []
        
        # Title page
        story.extend(self._create_title_page(assessment_data))
        story.append(PageBreak())
        
        # Executive summary
        story.extend(self._create_executive_summary(assessment_data))
        story.append(PageBreak())
        
        # Pattern analysis
        story.extend(self._create_pattern_analysis(assessment_data))
        story.append(PageBreak())
        
        # Digital analysis (if applicable)
        if assessment_data.get('is_digital_native'):
            story.extend(self._create_digital_analysis(assessment_data))
            story.append(PageBreak())
        
        # Transformation roadmap
        story.extend(self._create_transformation_roadmap(assessment_data))
        story.append(PageBreak())
        
        # Investment analysis
        story.extend(self._create_investment_analysis(assessment_data))
        story.append(PageBreak())
        
        # Next steps
        story.extend(self._create_next_steps(assessment_data))
        
        # Build PDF
        doc.build(story)
        
        # Return bytes
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes
    
    def _create_title_page(self, assessment_data):
        """Create title page"""
        story = []
        
        # Main title
        story.append(Paragraph("Behavioral Transformation Blueprint", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Subtitle
        contact_info = assessment_data.get('contact_info', {})
        user_name = contact_info.get('name', 'Valued Client')
        story.append(Paragraph(f"Personalized Analysis for {user_name}", self.styles['CustomSubtitle']))
        story.append(Spacer(1, 30))
        
        # Key metrics table
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        completion_rate = assessment_data.get('completion_rate', 1.0)
        
        metrics_data = [
            ['Metric', 'Value'],
            ['Patterns Identified', str(pattern_count)],
            ['Assessment Completion', f"{completion_rate*100:.0f}%"],
            ['Generated On', datetime.now().strftime("%B %d, %Y")],
        ]
        
        # Add digital metrics if applicable
        if assessment_data.get('is_digital_native'):
            digital_analysis = assessment_data.get('digital_despair_analysis', {})
            digital_score = digital_analysis.get('digital_despair_score', 0)
            severity = digital_analysis.get('severity_level', 'Unknown')
            
            metrics_data.extend([
                ['Digital Conditioning', f"{digital_score:.0f}% ({severity})"],
                ['Specialized Approach', 'Required' if severity in ['SEVERE', 'MODERATE'] else 'Standard']
            ])
        
        metrics_table = Table(metrics_data, colWidths=[3*inch, 2*inch])
        metrics_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4CA1A3')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(metrics_table)
        story.append(Spacer(1, 40))
        
        # Disclaimer
        disclaimer = """
        <b>Confidential Report</b><br/>
        This personalized analysis is based on your comprehensive behavioral assessment. 
        It contains sensitive psychological insights intended solely for your personal use and 
        transformation journey. Please keep this information confidential.
        """
        story.append(Paragraph(disclaimer, self.styles['InsightStyle']))
        
        return story
    
    def _create_executive_summary(self, assessment_data):
        """Create executive summary section"""
        story = []
        
        story.append(Paragraph("Executive Summary", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Key findings
        pattern_scores = assessment_data.get('pattern_scores', {})
        if pattern_scores:
            # Get pattern names
            patterns = {
                1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
                4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
                7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
            }
            
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            dominant_pattern = patterns.get(sorted_patterns[0][0], "Unknown")
            
            summary_text = f"""
            <b>Primary Pattern:</b> {dominant_pattern}<br/><br/>
            
            Your assessment reveals {len(pattern_scores)} significant behavioral patterns that are currently 
            impacting your daily life and relationships. The dominant pattern, {dominant_pattern}, 
            shows the highest intensity and is likely the primary focus for transformation.<br/><br/>
            
            <b>Transformation Outlook:</b> Based on your pattern constellation and assessment responses, 
            you show excellent readiness for rapid transformation through specialized hypnotherapy. 
            Your pattern recognition ability and completion of this comprehensive assessment demonstrates 
            the self-awareness necessary for successful change.<br/><br/>
            """
            
            # Add digital summary if applicable
            if assessment_data.get('is_digital_native'):
                digital_analysis = assessment_data.get('digital_despair_analysis', {})
                severity = digital_analysis.get('severity_level', 'Unknown')
                
                summary_text += f"""
                <b>Digital Conditioning:</b> Your assessment reveals {severity.lower()} level digital conditioning 
                patterns that require specialized therapeutic adaptations for optimal results. This is increasingly 
                common and highly treatable with proper approaches.<br/><br/>
                """
            
            summary_text += """
            <b>Recommended Approach:</b> 2-3 session rapid transformation hypnotherapy protocol 
            specifically designed for your pattern constellation. Expected timeline: 2-4 weeks 
            for complete transformation with high probability of lasting change.
            """
            
            story.append(Paragraph(summary_text, self.styles['PatternStyle']))
        
        return story
    
    def _create_pattern_analysis(self, assessment_data):
        """Create detailed pattern analysis section"""
        story = []
        
        story.append(Paragraph("Detailed Pattern Analysis", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        if not pattern_scores:
            story.append(Paragraph("No significant patterns detected.", self.styles['PatternStyle']))
            return story
        
        patterns = {
            1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
            4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
            7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
        }
        
        pattern_descriptions = {
            1: "Difficulty accepting or maintaining positive emotional states, often sabotaging happiness",
            2: "Recurring conflicts and power struggles in relationships and professional settings",
            3: "Default skepticism about others' intentions, maintaining protective emotional barriers",
            4: "Black-and-white thinking patterns that limit creative solutions and increase decision paralysis",
            5: "Self-worth closely tied to productivity and achievement, difficulty with rest or self-care",
            6: "Inconsistent sense of identity across different contexts, emotional exhaustion from persona management",
            7: "Prioritizing others' needs while neglecting self-care, leading to resentment and depletion",
            8: "Life choices driven by family expectations rather than personal desires, internal conflict",
            9: "Context-dependent loss of personal boundaries, inconsistent self-advocacy"
        }
        
        # Sort patterns by intensity
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns):
            pattern_name = patterns.get(pattern_id, f"Pattern {pattern_id}")
            description = pattern_descriptions.get(pattern_id, "Behavioral pattern requiring exploration")
            
            # Determine intensity
            if score >= 6:
                intensity = "High Intensity"
                color = "red"
            elif score >= 4:
                intensity = "Moderate Intensity"
                color = "orange"
            elif score >= 2:
                intensity = "Mild Intensity"
                color = "blue"
            else:
                intensity = "Emerging Pattern"
                color = "green"
            
            # Pattern header
            pattern_header = f"<b>{i+1}. {pattern_name}</b> - {intensity} (Score: {score:.1f}/10)"
            story.append(Paragraph(pattern_header, self.styles['CustomSubtitle']))
            
            # Pattern description
            story.append(Paragraph(description, self.styles['PatternStyle']))
            
            # Add space between patterns
            story.append(Spacer(1, 15))
        
        return story
    
    def _create_digital_analysis(self, assessment_data):
        """Create digital conditioning analysis section"""
        story = []
        
        story.append(Paragraph("Digital Conditioning Analysis", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        digital_analysis = assessment_data.get('digital_despair_analysis', {})
        if not digital_analysis:
            return story
        
        severity = digital_analysis.get('severity_level', 'Unknown')
        score = digital_analysis.get('digital_despair_score', 0)
        
        analysis_text = f"""
        <b>Digital Conditioning Level:</b> {severity} ({score:.0f}% score)<br/><br/>
        
        Your assessment reveals significant digital conditioning patterns that require specialized 
        therapeutic approaches. This is not a pathology but rather an adaptation to digital 
        environments that now requires updating for optimal real-world functioning.<br/><br/>
        
        <b>Key Findings:</b><br/>
        """
        
        # Add component analysis
        components = digital_analysis.get('component_scores', {})
        component_names = {
            'reality_dissociation': 'Online vs Offline Authenticity Gap',
            'binary_success_pressure': 'Extraordinary Achievement Pressure',
            'ironic_detachment': 'Emotional Protection Through Cynicism',
            'algorithmic_dependency': 'Social Media Emotional Regulation',
            'nihilistic_worldview': 'Hopelessness and Meaning Crisis',
            'hope_avoidance': 'Resistance to Optimism',
            'attention_fragmentation': 'Digital Attention Conditioning'
        }
        
        for comp, score in components.items():
            if comp in component_names and score >= 2:
                name = component_names[comp]
                level = "High" if score >= 4 else "Moderate"
                analysis_text += f"• {name}: {level} impact<br/>"
        
        analysis_text += f"""<br/>
        <b>Therapeutic Implications:</b><br/>
        {severity} level digital conditioning requires specialized hypnotherapy adaptations including 
        modified session structure, collaborative language patterns, and integration approaches 
        that honor your digital competencies while expanding real-world confidence.
        """
        
        story.append(Paragraph(analysis_text, self.styles['PatternStyle']))
        
        return story
    
    def _create_transformation_roadmap(self, assessment_data):
        """Create transformation roadmap section"""
        story = []
        
        story.append(Paragraph("Your Transformation Roadmap", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Calculate session plan
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        digital_analysis = assessment_data.get('digital_despair_analysis', {})
        digital_severity = digital_analysis.get('severity_level', 'MINIMAL') if digital_analysis else 'MINIMAL'
        
        # Determine approach
        if pattern_count >= 5 or digital_severity in ['SEVERE', 'MODERATE']:
            sessions = "2-3 sessions"
            timeline = "3-4 weeks"
            success_rate = 85
        elif pattern_count >= 3:
            sessions = "2 sessions"
            timeline = "2-3 weeks"
            success_rate = 88
        else:
            sessions = "2 sessions"
            timeline = "2 weeks"
            success_rate = 92
        
        roadmap_text = f"""
        <b>Recommended Protocol:</b> {sessions} over {timeline}<br/>
        <b>Success Probability:</b> {success_rate}%<br/><br/>
        
        <b>Session 1: Deep Pattern Analysis & Rapport Building (90 minutes)</b><br/>
        • Complete behavioral sequence mapping<br/>
        • Unconscious belief identification<br/>
        • Protective function analysis<br/>
        • Initial positive programming<br/>
        • Therapeutic alliance establishment<br/><br/>
        
        <b>Session 2: Core Transformation & Neural Rewiring (90 minutes)</b><br/>
        • Direct pattern interruption using theta brainwave states<br/>
        • Installation of new empowering response patterns<br/>
        • Integration of authentic identity<br/>
        • Future scenario testing<br/>
        • Positive programming anchoring<br/><br/>
        """
        
        if sessions == "2-3 sessions":
            roadmap_text += """
            <b>Session 3: Integration & Mastery (60 minutes - if needed)</b><br/>
            • Advanced pattern reinforcement<br/>
            • Fine-tuning of responses<br/>
            • Resolution of any remaining resistance<br/>
            • Long-term stability anchoring<br/><br/>
            """
        
        roadmap_text += """
        <b>Expected Timeline for Results:</b><br/>
        • 24-48 hours: Initial shifts in awareness and automatic responses<br/>
        • Week 1: New response patterns beginning to feel natural<br/>
        • Week 2-3: Integration and stabilization of new patterns<br/>
        • Month 1+: Complete integration and continued evolution<br/>
        """
        
        story.append(Paragraph(roadmap_text, self.styles['PatternStyle']))
        
        return story
    
    def _create_investment_analysis(self, assessment_data):
        """Create investment analysis section"""
        story = []
        
        story.append(Paragraph("Investment Analysis", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        # Calculate costs
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        
        # Estimated costs of not changing (conservative)
        annual_cost = pattern_count * 3000  # Lost opportunities, stress costs, etc.
        five_year_cost = annual_cost * 5
        
        investment_text = f"""
        <b>Cost of Not Changing (5-year projection):</b><br/>
        • Lost opportunities: ${pattern_count * 2000 * 5:,}<br/>
        • Stress-related costs: ${pattern_count * 1500 * 5:,}<br/>
        • Relationship impact: ${min(pattern_count * 800 * 5, 25000):,}<br/>
        • <b>Total estimated impact: ${five_year_cost:,}</b><br/><br/>
        
        <b>Transformation Investment:</b><br/>
        • Standard package (2 sessions): $3,000<br/>
        • Complete package (3 sessions): $4,000<br/>
        • Success rate: 85-92%<br/>
        • Satisfaction guarantee included<br/><br/>
        
        <b>Return on Investment:</b><br/>
        • Investment: $3,000-4,000<br/>
        • 5-year savings: ${five_year_cost:,}<br/>
        • ROI: {((five_year_cost - 4000) / 4000 * 100):,.0f}%<br/>
        • Break-even time: 2-6 months typically<br/><br/>
        
        <b>Value Beyond Pattern Resolution:</b><br/>
        • Enhanced decision-making clarity<br/>
        • Increased confidence and self-advocacy<br/>
        • Improved relationship satisfaction<br/>
        • Greater resilience to stress<br/>
        • Access to unconscious creativity<br/>
        • Deeper self-understanding<br/>
        • Increased energy from eliminating internal conflicts<br/>
        """
        
        story.append(Paragraph(investment_text, self.styles['PatternStyle']))
        
        return story
    
    def _create_next_steps(self, assessment_data):
        """Create next steps section"""
        story = []
        
        story.append(Paragraph("Your Next Steps", self.styles['CustomTitle']))
        story.append(Spacer(1, 20))
        
        contact_info = assessment_data.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            contact_timeline = "within 24 hours"
        else:
            contact_timeline = "within 48-72 hours"
        
        next_steps_text = f"""
        <b>Immediate Actions:</b><br/><br/>
        
        <b>1. Clinical Review (24-48 hours)</b><br/>
        Our licensed therapist will analyze your comprehensive assessment and design your 
        personalized transformation protocol. Given your assessment results, you're on our 
        contact list for {contact_timeline}.<br/><br/>
        
        <b>2. Personal Consultation ({contact_timeline})</b><br/>
        We'll reach out via your preferred method to schedule your first transformation 
        session and answer any questions about your personalized approach.<br/><br/>
        
        <b>3. Transformation Session 1 (Within 1 week)</b><br/>
        Your personalized hypnotherapy protocol begins, targeting your specific pattern 
        constellation for maximum effectiveness.<br/><br/>
        
        <b>What to Prepare:</b><br/>
        • Notice your patterns in action without trying to change them<br/>
        • See patterns as outdated protection rather than personal flaws<br/>
        • Consider what life would look like with patterns resolved<br/>
        • Stay open to change being easier than previous experiences<br/><br/>
        
        <b>Contact Information:</b><br/>
        • Website: hypnotherapy.streamlit.app<br/>
        • Direct scheduling: calendly.com/laetitiasheppard/discovery<br/>
        • Email: Reply to any assessment communication<br/><br/>
        
        <b>Your Guarantee:</b><br/>
        • If not satisfied after 2 sessions, receive complimentary 3rd session<br/>
        • If still not satisfied, receive full refund<br/>
        • 95% of clients never need to use this guarantee<br/>
        """
        
        story.append(Paragraph(next_steps_text, self.styles['PatternStyle']))
        
        return story
