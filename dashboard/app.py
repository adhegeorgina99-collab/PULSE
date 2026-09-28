import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path


# ============================================================
# PULSE — INDUSTRIAL EQUIPMENT CONDITION MONITORING SYSTEM
# ============================================================

st.set_page_config(
    page_title="PULSE",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PAGE STYLE
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #061426;
    }

    [data-testid="stHeader"] {
        background: #061426;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1600px;
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    .pulse-title {
        font-size: 42px;
        font-weight: 800;
        color: #F5F9FF;
        margin: 0;
    }

    .pulse-subtitle {
        font-size: 15px;
        color: #A9BED5;
        margin-top: -5px;
    }

    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #F4F8FF;
        margin: 8px 0;
    }

    div[data-testid="stMetric"] {
        background: #0A1B30;
        border: 1px solid #16456E;
        border-radius: 12px;
        padding: 14px;
    }

    div[data-testid="stMetricLabel"] {
        color: #AFC3DA !important;
    }

    div[data-testid="stMetricValue"] {
        color: #F4F8FF !important;
    }

    .live {
        color: #22E6A1;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA LOCATION
# ============================================================

CSV_FILE = (
    Path(__file__).resolve().parent.parent
    / "Data"
    / "equipment_readings.csv"
)


# ============================================================
# LIVE DASHBOARD
# ============================================================

@st.fragment(run_every="5s")
def dashboard():

    # ========================================================
    # LOAD DATA
    # ========================================================

    try:
        df = pd.read_csv(CSV_FILE)
    except Exception as e:
        st.error(f"Could not load PULSE data: {e}")
        return


    # ========================================================
    # CLEAN COLUMNS
    # ========================================================

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    required = [
        "timestamp",
        "equipment_id",
        "pressure_bar",
        "temperature_c",
        "vibration_mm_s",
        "flow_rate_l_min",
        "status"
    ]


    missing = [
        col for col in required
        if col not in df.columns
    ]


    if missing:
        st.error(
            "Missing columns: " + ", ".join(missing)
        )
        return


    # ========================================================
    # TIMESTAMP
    # ========================================================

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["timestamp"]
    ).copy()


    # ========================================================
    # STATUS
    # ========================================================

    df["status"] = (
        df["status"]
        .astype(str)
        .str.upper()
        .str.strip()
    )


    # ========================================================
    # SORT READINGS
    # ========================================================

    df = (
        df
        .sort_values("timestamp")
        .reset_index(drop=True)
    )


    # IMPORTANT:
    # Every reading gets its own sequence number.
    # This makes the trend show every reading separately,
    # even when many readings were generated on the same day.

    df["reading_number"] = range(
        1,
        len(df) + 1
    )


    # ========================================================
    # BASIC VALUES
    # ========================================================

    latest = df.iloc[-1]

    equipment_count = df[
        "equipment_id"
    ].nunique()

    normal_count = (
        df["status"] == "NORMAL"
    ).sum()

    warning_count = (
        df["status"] == "WARNING"
    ).sum()

    critical_count = (
        df["status"] == "CRITICAL"
    ).sum()

    total_readings = len(df)

    alert_count = (
        warning_count +
        critical_count
    )


    normal_percent = (
        normal_count / total_readings * 100
        if total_readings else 0
    )

    warning_percent = (
        warning_count / total_readings * 100
        if total_readings else 0
    )

    critical_percent = (
        critical_count / total_readings * 100
        if total_readings else 0
    )


    # ========================================================
    # HEADER
    # ========================================================

    header_left, header_right = st.columns(
        [3, 1],
        vertical_alignment="center"
    )


    with header_left:

        st.markdown(
            '<div class="pulse-title">⚡ PULSE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="pulse-subtitle">'
            'Industrial Equipment Condition Monitoring System'
            '</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Monitor  •  Detect  •  Protect"
        )


    with header_right:

        st.markdown(
            '<div class="live">🟢 LIVE</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Updated: "
            + latest["timestamp"].strftime(
                "%d %b %Y, %H:%M:%S"
            )
        )


    st.divider()


    # ========================================================
    # SYSTEM OVERVIEW
    # ========================================================

    st.markdown(
        '<div class="section-title">System Overview</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:
        st.metric(
            "⚙️ Total Equipment",
            equipment_count,
            "Active",
            border=True
        )


    with c2:
        st.metric(
            "🟢 Normal",
            normal_count,
            f"{normal_percent:.1f}%",
            border=True
        )


    with c3:
        st.metric(
            "🟡 Warning",
            warning_count,
            f"{warning_percent:.1f}%",
            border=True
        )


    with c4:
        st.metric(
            "🔴 Critical",
            critical_count,
            f"{critical_percent:.1f}%",
            border=True
        )


    with c5:
        st.metric(
            "🚨 Total Alerts",
            alert_count,
            "Warning + Critical",
            border=True
        )


    st.write("")


    # ========================================================
    # STATUS / LIVE METRICS / ALERTS
    # ========================================================

    left, middle, right = st.columns(
        [1.05, 2.1, 1.05]
    )


    # ========================================================
    # STATUS DISTRIBUTION
    # ========================================================

    with left:

        with st.container(border=True):

            st.subheader(
                "Equipment Status Distribution"
            )


            pie = go.Figure(
                data=[
                    go.Pie(
                        labels=[
                            "Normal",
                            "Warning",
                            "Critical"
                        ],
                        values=[
                            normal_count,
                            warning_count,
                            critical_count
                        ],
                        hole=0.62,
                        marker=dict(
                            colors=[
                                "#13D98B",
                                "#FFBE32",
                                "#FF4054"
                            ]
                        ),
                        textinfo="percent",
                        textfont=dict(
                            color="white"
                        )
                    )
                ]
            )


            pie.update_layout(
                height=280,
                margin=dict(
                    l=0,
                    r=0,
                    t=5,
                    b=0
                ),
                paper_bgcolor="#081A2E",
                plot_bgcolor="#081A2E",
                showlegend=True,
                legend=dict(
                    font=dict(
                        color="#DDE9F5"
                    )
                ),
                annotations=[
                    dict(
                        text=(
                            f"<b>{total_readings}</b>"
                            "<br>Readings"
                        ),
                        x=0.5,
                        y=0.5,
                        showarrow=False,
                        font=dict(
                            color="white",
                            size=15
                        )
                    )
                ]
            )


            st.plotly_chart(
                pie,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )


    # ========================================================
    # LIVE MONITORING
    # ========================================================

    with middle:

        with st.container(border=True):

            st.subheader(
                "Live Monitoring Metrics"
            )


            m1, m2 = st.columns(2)


            with m1:

                st.metric(
                    "🌡️ Temperature",
                    f"{latest['temperature_c']:.2f} °C",
                    border=True
                )


            with m2:

                st.metric(
                    "📈 Pressure",
                    f"{latest['pressure_bar']:.2f} bar",
                    border=True
                )


            m3, m4 = st.columns(2)


            with m3:

                st.metric(
                    "〰️ Vibration",
                    f"{latest['vibration_mm_s']:.2f} mm/s",
                    border=True
                )


            with m4:

                st.metric(
                    "💧 Flow Rate",
                    f"{latest['flow_rate_l_min']:.2f} L/min",
                    border=True
                )


    # ========================================================
    # ALERT TREND
    # ========================================================

    with right:

        with st.container(border=True):

            st.subheader(
                "Alerts Trend"
            )


            alert_df = df.copy()


            daily = (
                alert_df
                .groupby(
                    alert_df["timestamp"].dt.date
                )
                .agg(
                    Normal=(
                        "status",
                        lambda x:
                        (x == "NORMAL").sum()
                    ),
                    Warning=(
                        "status",
                        lambda x:
                        (x == "WARNING").sum()
                    ),
                    Critical=(
                        "status",
                        lambda x:
                        (x == "CRITICAL").sum()
                    )
                )
                .reset_index()
            )


            fig_alert = go.Figure()


            fig_alert.add_trace(
                go.Bar(
                    x=daily["timestamp"],
                    y=daily["Normal"],
                    name="Normal",
                    marker_color="#13D98B"
                )
            )


            fig_alert.add_trace(
                go.Bar(
                    x=daily["timestamp"],
                    y=daily["Warning"],
                    name="Warning",
                    marker_color="#FFBE32"
                )
            )


            fig_alert.add_trace(
                go.Bar(
                    x=daily["timestamp"],
                    y=daily["Critical"],
                    name="Critical",
                    marker_color="#FF4054"
                )
            )


            fig_alert.update_layout(
                barmode="stack",
                height=280,
                margin=dict(
                    l=35,
                    r=5,
                    t=10,
                    b=35
                ),
                paper_bgcolor="#081A2E",
                plot_bgcolor="#081A2E",
                font=dict(
                    color="#AFC3DA"
                ),
                yaxis=dict(
                    title="Readings"
                ),
                showlegend=True,
                legend=dict(
                    orientation="h",
                    y=-0.25
                )
            )


            st.plotly_chart(
                fig_alert,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )


    # ========================================================
    # TREND FUNCTION
    # ========================================================

    def make_trend(
        column,
        title,
        y_title,
        color
    ):

        fig = go.Figure()


        fig.add_trace(
            go.Scatter(
                x=df["reading_number"],
                y=df[column],
                mode="lines+markers",
                line=dict(
                    color=color,
                    width=2.5,
                    shape="linear"
                ),
                marker=dict(
                    color=color,
                    size=4
                ),
                customdata=df[
                    "timestamp"
                ].dt.strftime(
                    "%d %b %Y %H:%M:%S"
                ),
                hovertemplate=(
                    "Reading %{x}<br>"
                    + y_title
                    + ": %{y:.2f}<br>"
                    + "Time: %{customdata}"
                    + "<extra></extra>"
                )
            )
        )


        fig.update_layout(
            title=dict(
                text=title,
                font=dict(
                    size=14,
                    color="#EAF2FF"
                )
            ),
            height=245,
            margin=dict(
                l=45,
                r=10,
                t=45,
                b=35
            ),
            paper_bgcolor="#081A2E",
            plot_bgcolor="#081A2E",
            font=dict(
                color="#AFC3DA"
            ),
            xaxis=dict(
                title="Reading",
                showgrid=True,
                gridcolor=(
                    "rgba(120,170,210,0.10)"
                ),
                zeroline=False
            ),
            yaxis=dict(
                title=y_title,
                showgrid=True,
                gridcolor=(
                    "rgba(120,170,210,0.10)"
                ),
                zeroline=False
            ),
            showlegend=False,
            hovermode="closest"
        )


        return fig


    # ========================================================
    # EQUIPMENT TRENDS
    # ========================================================

    st.markdown(
        '<div class="section-title">Equipment Trends</div>',
        unsafe_allow_html=True
    )


    t1, t2, t3, t4 = st.columns(4)


    with t1:

        with st.container(border=True):

            st.plotly_chart(
                make_trend(
                    "temperature_c",
                    "Temperature Trend",
                    "°C",
                    "#FF7043"
                ),
                use_container_width=True,
                config={
                    "displayModeBar": False
                },
                key="temperature_trend"
            )


    with t2:

        with st.container(border=True):

            st.plotly_chart(
                make_trend(
                    "pressure_bar",
                    "Pressure Trend",
                    "bar",
                    "#38AFFF"
                ),
                use_container_width=True,
                config={
                    "displayModeBar": False
                },
                key="pressure_trend"
            )


    with t3:

        with st.container(border=True):

            st.plotly_chart(
                make_trend(
                    "vibration_mm_s",
                    "Vibration Trend",
                    "mm/s",
                    "#A878FF"
                ),
                use_container_width=True,
                config={
                    "displayModeBar": False
                },
                key="vibration_trend"
            )


    with t4:

        with st.container(border=True):

            st.plotly_chart(
                make_trend(
                    "flow_rate_l_min",
                    "Flow Rate Trend",
                    "L/min",
                    "#00D5D8"
                ),
                use_container_width=True,
                config={
                    "displayModeBar": False
                },
                key="flow_trend"
            )


    # ========================================================
    # BOTTOM SECTION
    # ========================================================

    st.write("")


    b1, b2, b3 = st.columns(
        [1.2, 1.3, 0.9]
    )


    # ========================================================
    # EQUIPMENT RISK
    # ========================================================

    with b1:

        with st.container(border=True):

            st.subheader(
                "Equipment Risk Level"
            )


            current_status = str(
                latest["status"]
            ).upper()


            if current_status == "NORMAL":
                risk = 25
                risk_color = "#13D98B"

            elif current_status == "WARNING":
                risk = 55
                risk_color = "#FFBE32"

            else:
                risk = 85
                risk_color = "#FF4054"


            risk_fig = go.Figure()


            risk_fig.add_trace(
                go.Bar(
                    x=[risk],
                    y=[latest["equipment_id"]],
                    orientation="h",
                    marker_color=risk_color,
                    text=[f"{risk}%"],
                    textposition="outside"
                )
            )


            risk_fig.update_layout(
                height=190,
                margin=dict(
                    l=20,
                    r=30,
                    t=10,
                    b=30
                ),
                paper_bgcolor="#081A2E",
                plot_bgcolor="#081A2E",
                font=dict(
                    color="#AFC3DA"
                ),
                xaxis=dict(
                    range=[0, 100],
                    title="Risk Score (%)"
                ),
                yaxis=dict(
                    title=None
                ),
                showlegend=False
            )


            st.plotly_chart(
                risk_fig,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )


    # ========================================================
    # RECENT ALERTS
    # ========================================================

    with b2:

        with st.container(border=True):

            st.subheader(
                "Recent Alerts"
            )


            alerts = (
                df[
                    df["status"].isin(
                        ["WARNING", "CRITICAL"]
                    )
                ]
                .sort_values(
                    "timestamp",
                    ascending=False
                )
                .head(8)
            )


            if alerts.empty:

                st.success(
                    "No warning or critical readings."
                )

            else:

                alert_display = alerts[
                    [
                        "timestamp",
                        "equipment_id",
                        "status",
                        "pressure_bar",
                        "temperature_c",
                        "vibration_mm_s"
                    ]
                ].copy()


                alert_display["timestamp"] = (
                    alert_display["timestamp"]
                    .dt.strftime(
                        "%d %b %H:%M:%S"
                    )
                )


                alert_display.columns = [
                    "Time",
                    "Equipment",
                    "Status",
                    "Pressure",
                    "Temp.",
                    "Vibration"
                ]


                st.dataframe(
                    alert_display,
                    use_container_width=True,
                    hide_index=True
                )


    # ========================================================
    # SELECTED EQUIPMENT
    # ========================================================

    with b3:

        with st.container(border=True):

            st.subheader(
                "Selected Equipment Detail"
            )


            st.markdown(
                f"### {latest['equipment_id']}"
            )


            if current_status == "NORMAL":

                st.success(
                    "🟢 NORMAL"
                )

            elif current_status == "WARNING":

                st.warning(
                    "🟡 WARNING"
                )

            else:

                st.error(
                    "🔴 CRITICAL"
                )


            st.write(
                "**Last Updated:** "
                + latest["timestamp"].strftime(
                    "%d %b %Y %H:%M:%S"
                )
            )


            st.write(
                f"**Pressure:** "
                f"{latest['pressure_bar']:.2f} bar"
            )

            st.write(
                f"**Temperature:** "
                f"{latest['temperature_c']:.2f} °C"
            )

            st.write(
                f"**Flow Rate:** "
                f"{latest['flow_rate_l_min']:.2f} L/min"
            )

            st.write(
                f"**Vibration:** "
                f"{latest['vibration_mm_s']:.2f} mm/s"
            )


    # ========================================================
    # FOOTER
    # ========================================================

    st.divider()

    st.caption(
        "⚡ PULSE | Industrial Equipment Condition Monitoring System "
        "| Monitor • Detect • Protect | Live monitoring"
    )


# ============================================================
# START DASHBOARD
# ============================================================

dashboard()