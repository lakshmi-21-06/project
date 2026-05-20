import streamlit as st

st.set_page_config(page_title="Career Path Predictor", layout="centered")

st.title("🎯 Career Path Predictor")
st.subheader("Let's understand your interests and goals to suggest your best-fit career!")

# Step 1: Education Level
education = st.selectbox(
    "📘 What is your highest level of education?",
    ["High School", "Diploma", "Undergraduate", "Postgraduate", "PhD"]
)

# Step 2: Interests
interests = st.multiselect(
    "🧠 What subjects or domains interest you?",
    [
        "Math", "Science", "AI/ML", "Accounting", "Programming", "Design",
        "Writing", "Marketing", "Management", "Psychology", "Economics",
        "Biology", "History", "Politics", "Entrepreneurship", "Cybersecurity",
        "Robotics", "Cloud Computing", "Philosophy", "Animation", "Content Creation"
    ]
)

# Step 3: Job Preference
job_type = st.radio(
    "💼 What kind of job are you aiming for?",
    ["Government", "Corporate", "Startup/Small Business", "Freelancer", "Remote/Flexible"]
)

# Step 4: Skills
skills = st.multiselect(
    "🛠️ What skills do you currently have?",
    [
        "Python", "C/C++", "Java", "SQL", "HTML/CSS", "JavaScript",
        "Data Analysis", "Excel", "Communication", "Public Speaking",
        "Web Development", "Machine Learning", "Time Management",
        "Teamwork", "Leadership", "Critical Thinking", "UX/UI Design",
        "Cloud Platforms (AWS/Azure)", "Graphic Design", "Problem Solving",
        "Social Media Management", "Writing", "Video Editing", "Networking"
    ]
)

# Step 5: Experience (optional)
experience = st.slider("📆 How many years of experience do you have in any field?", 0, 10, 0)

# Roadmaps and Resources Dictionary
career_roadmaps = {
    "AI/ML Engineer": {
        "roadmap": [
            "Learn Python and Math (Linear Algebra, Statistics)",
            "Study Machine Learning algorithms",
            "Get hands-on with projects using Scikit-learn, TensorFlow, or PyTorch",
            "Learn Data Engineering Basics",
            "Explore Deep Learning & NLP",
            "Contribute to open-source or research",
            "Understand deployment using Flask, Docker, or cloud platforms"
        ],
        "resources": [
            "Coursera ML by Andrew Ng",
            "fast.ai Practical Deep Learning",
            "Kaggle Competitions and Datasets",
            "Books: 'Hands-On ML with Scikit-Learn, Keras, and TensorFlow'",
            "Google Cloud ML Tools"
        ]
    },
    "Web Developer": {
        "roadmap": [
            "Learn HTML, CSS, JavaScript",
            "Master a JS framework like React or Vue",
            "Learn backend with Node.js, Express, or Django",
            "Practice building full-stack apps",
            "Learn Git, APIs, and basic DevOps",
            "Deploy apps using Netlify, Vercel, or Heroku"
        ],
        "resources": [
            "freeCodeCamp",
            "The Odin Project",
            "MDN Web Docs",
            "Frontend Mentor Projects",
            "Scrimba Courses"
        ]
    },
    "Product Manager": {
        "roadmap": [
            "Understand basics of business and tech",
            "Learn product lifecycle and agile methodologies",
            "Build communication and leadership skills",
            "Practice creating product roadmaps",
            "Work on mock product case studies",
            "Understand data analysis and user research",
            "Gain exposure to product tools (JIRA, Notion, Figma)"
        ],
        "resources": [
            "PM School (YouTube)",
            "Reforge Courses",
            "Product School Blogs",
            "Case Interview Books for PMs",
            "Mind the Product"
        ]
    },
    "Data Analyst": {
        "roadmap": [
            "Learn Excel, SQL, and basic statistics",
            "Study Python for Data Analysis (Pandas, Matplotlib)",
            "Understand Data Cleaning and Visualization",
            "Build dashboards using Power BI or Tableau",
            "Work on real datasets",
            "Learn to present insights effectively"
        ],
        "resources": [
            "Google Data Analytics Certificate",
            "Kaggle Notebooks",
            "DataCamp & Mode Analytics",
            "LeetCode SQL Practice",
            "Alex the Analyst (YouTube)"
        ]
    },
    "UI/UX Designer": {
        "roadmap": [
            "Learn design fundamentals (typography, color theory)",
            "Understand UX research methods",
            "Practice wireframing and prototyping",
            "Use tools like Figma, Adobe XD",
            "Design real app interfaces",
            "Build a portfolio",
            "Understand accessibility and responsive design"
        ],
        "resources": [
            "Figma Learn",
            "Coursera Google UX Design Certificate",
            "UX Crash Course by The Hipper Element",
            "Dribbble Projects",
            "Refactoring UI Book"
        ]
    }
}

# Submit Button
if st.button("🔍 Predict My Career Path"):
    st.subheader("🔎 Based on your inputs, here's our suggestion:")

    # Dummy predictions based on interests
    suggestions = []
    if "AI/ML" in interests or "Machine Learning" in skills:
        suggestions.append("AI/ML Engineer")
    if "Programming" in interests or "Web Development" in skills:
        suggestions.append("Web Developer")
    if "Management" in interests:
        suggestions.append("Product Manager")
    if "Data Analysis" in skills or "Math" in interests:
        suggestions.append("Data Analyst")
    if "Design" in interests or "UX/UI Design" in skills:
        suggestions.append("UI/UX Designer")

    if not suggestions:
        st.write("🤔 We couldn't determine a clear path. Try adding more interests or skills.")
    else:
        st.markdown("📝 *Roadmaps currently available for: AI/ML Engineer, Web Developer, Product Manager, Data Analyst, and UI/UX Designer.*")
        st.markdown("🔧 *More career guides are in progress and will be added soon!*")

        for role in suggestions:
            with st.expander(f"💼 {role}"):
                if role in career_roadmaps:
                    st.markdown("**Roadmap:**")
                    for step in career_roadmaps[role]["roadmap"]:
                        st.markdown(f"- {step}")
                    st.markdown("\n**Resources:**")
                    for res in career_roadmaps[role]["resources"]:
                        st.markdown(f"- {res}")
                else:
                    st.info("🚧 Roadmap for this role is coming soon! Stay tuned.")
