import base64
from pathlib import Path

import streamlit as st

from config.logging_config import setup_logging
from services.output_service import OutputService
from services.travel_planner_service import TravelPlannerService


setup_logging()

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide",
)


@st.cache_resource
def get_planner_service():
    return TravelPlannerService()


def build_user_request(
    destination: str,
    duration_days: int,
    interests: list[str],
    budget: str,
    travel_style: str,
) -> str:
    return (
        f"Plan a {duration_days} day trip to {destination}. "
        f"The trip should focus on: {', '.join(interests)}. "
        f"Budget: {budget}. "
        f"Travel style: {travel_style}."
    )


def get_background_image() -> str:
    image_path = Path("assets/background.jpg")

    if not image_path.exists():
        return ""

    encoded = base64.b64encode(image_path.read_bytes()).decode()

    return f"""
    background-image:
        linear-gradient(rgba(8, 12, 20, 0.72), rgba(8, 12, 20, 0.72)),
        url("data:image/jpg;base64,{encoded}");
    """


background_css = get_background_image()

st.markdown(
    f"""
    <style>
    .stApp {{
        {background_css}
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-color: #0b1020;
    }}

    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.94);
        border-right: 1px solid rgba(212, 175, 55, 0.35);
    }}

    .hero {{
        padding: 3rem 2.5rem;
        border-radius: 28px;
        background: linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.96),
            rgba(245, 239, 225, 0.92)
        );
        border: 1px solid rgba(212, 175, 55, 0.45);
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.28);
        margin-bottom: 1.8rem;
    }}

    .eyebrow {{
        color: #9a6b00;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.18rem;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }}

    .hero-title {{
        color: #101827;
        font-size: 3.4rem;
        line-height: 1.05;
        font-weight: 900;
        margin-bottom: 1rem;
    }}

    .hero-subtitle {{
        color: #3d4658;
        font-size: 1.15rem;
        line-height: 1.7;
        max-width: 760px;
    }}

    .metric-card {{
        padding: 1.4rem;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.94);
        border: 1px solid rgba(212, 175, 55, 0.35);
        box-shadow: 0 16px 45px rgba(0, 0, 0, 0.18);
        text-align: center;
        margin-bottom: 1rem;
    }}

    .metric-number {{
        font-size: 1.8rem;
        font-weight: 900;
        color: #101827;
    }}

    .metric-label {{
        font-size: 0.9rem;
        color: #7a5a12;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08rem;
    }}

    .section-card {{
        padding: 2rem;
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.96);
        border: 1px solid rgba(212, 175, 55, 0.32);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.24);
        margin-top: 1.5rem;
    }}

    .muted {{
        color: #687083;
        font-size: 0.95rem;
    }}

    div.stButton > button:first-child {{
        border-radius: 999px;
        font-weight: 800;
        padding: 0.7rem 1.2rem;
        background: linear-gradient(135deg, #c9a227, #f2d16b);
        color: #101827;
        border: 0;
    }}

    div.stDownloadButton > button:first-child {{
        border-radius: 999px;
        font-weight: 800;
        border: 1px solid #c9a227;
    }}

    h1, h2, h3 {{
        color: #101827;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


if "result" not in st.session_state:
    st.session_state.result = None

if "final_itinerary" not in st.session_state:
    st.session_state.final_itinerary = None


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Luxury AI Travel Concierge</div>
        <div class="hero-title">Plan smarter.<br>Travel beautifully.</div>
        <div class="hero-subtitle">
            Generate personalized travel itineraries using a professional multi-agent AI workflow.
            Your request is interpreted, structured, researched, and transformed into a polished travel guide.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown(
        '<div class="metric-card"><div class="metric-number">4</div><div class="metric-label">AI Agents</div></div>',
        unsafe_allow_html=True,
    )

with metric_col2:
    st.markdown(
        '<div class="metric-card"><div class="metric-number">LangGraph</div><div class="metric-label">Workflow</div></div>',
        unsafe_allow_html=True,
    )

with metric_col3:
    st.markdown(
        '<div class="metric-card"><div class="metric-number">Pydantic</div><div class="metric-label">Structured Outputs</div></div>',
        unsafe_allow_html=True,
    )

with metric_col4:
    st.markdown(
        '<div class="metric-card"><div class="metric-number">MD</div><div class="metric-label">Export</div></div>',
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.header("✈️ Trip Details")
    st.caption("Design your personalized itinerary.")

    destination = st.text_input("Destination", placeholder="Example: Tokyo, Paris, Bali")

    duration_days = st.number_input(
        "Trip duration in days",
        min_value=1,
        max_value=30,
        value=3,
        step=1,
    )

    interests = st.multiselect(
        "Interests",
        options=[
            "Fine dining",
            "Food",
            "Museums",
            "Nature",
            "History",
            "Anime",
            "Shopping",
            "Nightlife",
            "Architecture",
            "Beaches",
            "Adventure",
            "Luxury hotels",
            "Hidden gems",
            "Culture",
        ],
        default=["Food"],
    )

    budget = st.selectbox("Budget", options=["budget", "mid-range", "luxury"])

    travel_style = st.selectbox(
        "Travel style",
        options=["relaxed", "balanced", "fast-paced", "family-friendly", "romantic"],
    )

    generate_button = st.button("✨ Generate Luxury Itinerary", type="primary")

    st.divider()
    st.caption("Powered by LangGraph, OpenAI, Pydantic, and Streamlit.")


if generate_button:
    if not destination:
        st.error("Please enter a destination.")

    elif not interests:
        st.error("Please select at least one interest.")

    else:
        planner = get_planner_service()
        output_service = OutputService()

        user_request = build_user_request(
            destination=destination,
            duration_days=duration_days,
            interests=interests,
            budget=budget,
            travel_style=travel_style,
        )

        with st.status("Your AI concierge is planning your trip...", expanded=True) as status:
            st.write("✅ Preparing your request")
            st.write("🧠 Intake Agent: understanding the travel intent")
            st.write("🗺️ Planning Agent: designing the day-by-day structure")
            st.write("🔎 Research Agent: gathering destination information")
            st.write("✍️ Writing Agent: crafting the final itinerary")

            result = planner.generate_itinerary(user_request)

            st.session_state.result = result

            if result["status"] == "success":
                final_itinerary = result["final_itinerary"]
                st.session_state.final_itinerary = final_itinerary

                output_service.save_markdown(
                    filename="sample_itinerary.md",
                    content=final_itinerary,
                )

                status.update(
                    label="Your itinerary is ready.",
                    state="complete",
                    expanded=False,
                )

            else:
                status.update(
                    label="Trip generation failed.",
                    state="error",
                    expanded=True,
                )


if st.session_state.result is None:
    st.markdown(
        """
        <div class="section-card">
            <h2>Begin your journey</h2>
            <p class="muted">
                Enter your destination and preferences in the sidebar, then let the AI agents create your itinerary.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    result = st.session_state.result

    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    if result["status"] == "success":
        st.success("Your itinerary is ready.")

        final_itinerary = st.session_state.final_itinerary

        itinerary_tab, markdown_tab, debug_tab = st.tabs(
            ["Itinerary", "Raw Markdown", "Debug Info"]
        )

        with itinerary_tab:
            st.markdown(final_itinerary)

            st.download_button(
                label="Download Markdown Itinerary",
                data=final_itinerary,
                file_name="travel_itinerary.md",
                mime="text/markdown",
            )

        with markdown_tab:
            st.code(final_itinerary, language="markdown")

        with debug_tab:
            st.subheader("Workflow Status")
            st.write(result["status"])

            st.subheader("Trip Request")
            st.json(result["trip_request"])

            st.subheader("Itinerary Plan")
            st.json(result["itinerary_plan"])

            st.subheader("Research Results")
            st.json(result["research_results"])

            st.subheader("Errors")
            st.json(result["errors"])

    else:
        st.error("The workflow failed.")

        for error in result["errors"]:
            st.write(f"- {error}")

    st.markdown("</div>", unsafe_allow_html=True)