from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_profile(profile_text):

    prompt = f"""
You are an expert LinkedIn profile reviewer, recruiter,
ATS specialist and career optimization expert.

Analyze the LinkedIn profile text below.

Your goal is to help the candidate improve recruiter visibility
and profile quality.

IMPORTANT RULES:

1. Use ONLY information found in the uploaded LinkedIn profile.
2. Never invent experience, education, projects, achievements,
   certifications or existing skills.
3. "current" must represent information actually found in the profile.
4. "recommended" should show how the candidate could improve that section.
5. If a section is missing, set current to "Not provided".
6. If a section is already strong, do not unnecessarily rewrite it.
7. Scores must be integers from 0 to 100.
8. Recommendations must be realistic for the candidate's actual
   education, skills and experience.
9. Do not promise jobs or interviews. Recommendations are intended
   to improve profile quality and recruiter visibility.

Return ONLY valid JSON.

Do not include Markdown.
Do not include ```json.
Do not include explanations outside the JSON.

Use EXACTLY this JSON structure:

{{
    "overall_score": 0,

    "overall_summary": "",

    "section_scores": {{
        "headline": 0,
        "about": 0,
        "experience": 0,
        "skills": 0,
        "education": 0,
        "projects": 0
    }},

    "headline": {{
        "current": "",
        "recommended": "",
        "reason": "",
        "needs_change": true
    }},

    "about": {{
        "current": "",
        "recommended": "",
        "reason": "",
        "needs_change": true
    }},

    "experience": {{
        "current": "",
        "recommended": "",
        "reason": "",
        "needs_change": true
    }},

    "skills": {{
        "current": [],
        "recommended": [],
        "reason": "",
        "needs_change": true
    }},

    "education": {{
        "current": "",
        "recommended": "",
        "reason": "",
        "needs_change": true
    }},

    "projects": {{
        "current": "",
        "recommended": "",
        "reason": "",
        "needs_change": true
    }},

    "strengths": [
        "",
        "",
        ""
    ],

    "priority_improvements": [
        "",
        "",
        ""
    ],

    "recommended_jobs": [
        "",
        "",
        "",
        ""
    ]
}}

SCORING:

Headline:
Evaluate clarity, target role, professional positioning,
relevant keywords and recruiter search visibility.

About:
Evaluate professional introduction, skills, achievements,
career direction, readability and relevant keywords.

Experience:
Evaluate practical experience, responsibilities,
action verbs, measurable impact and relevance.

Skills:
Evaluate relevance, completeness and alignment with
the candidate's likely career direction.

Education:
Evaluate completeness, degree information,
field of study and relevance.

Projects:
Evaluate whether projects demonstrate practical skills,
technology usage, outcomes and career relevance.

For every section:

CURRENT:
Extract or summarize what is actually present in the profile.

RECOMMENDED:
Provide an improved version that the candidate could use on LinkedIn.

REASON:
Clearly explain why the change could improve profile quality
or recruiter visibility.

NEEDS_CHANGE:
Use true if meaningful improvement is recommended.
Use false if the current section is already strong.

LinkedIn Profile:

{profile_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2,

        response_format={
            "type": "json_object"
        }
    )

    result = response.choices[0].message.content

    return json.loads(result)
