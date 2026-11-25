"""EnergyWise - compact Streamlit dashboard for household energy estimates.

Run from the project directory with: python -m streamlit run app.py
The original CLI (main.py) and calculation modules are unchanged.
"""

from html import escape

import streamlit as st

from src.calculator import calculate_consumption_for_days
from src.electricity_prices import get_electricity_price


st.set_page_config(
    page_title="EnergyWise | Home Energy Dashboard",
    page_icon="\U0001F33F",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Design uses ordinary CSS and built-in Streamlit widgets. No JS required.
st.markdown(
    """
    <style>
    :root {
        --ink: #102F3D;
        --muted: #5C7A7A;
        --green: #087B67;
        --dark-green: #075E50;
        --line: #D8E9E4;
        --mint: #E9F6F2;
    }
    .stApp { background: #F8FCFA; color: var(--ink); }
    /* Single-page dashboard occupies the complete available viewport. */
    .block-container,
    [data-testid="stAppViewBlockContainer"] {
        width: 100% !important;
        max-width: none !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        padding: .25rem 1rem .45rem !important;
    }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    [data-testid="stHeader"] { display: none; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid var(--line);
        border-radius: 17px;
        background: #FFFFFF;
        box-shadow: 0 4px 18px rgba(12, 66, 54, .045);
    }
    [data-testid="stButton"] button,
    [data-testid="stFormSubmitButton"] button {
        border-radius: 9px;
        min-height: 2.22rem;
        font-weight: 600;
    }
    button[kind="primary"] { background: #087B67; border-color: #087B67; }
    button[kind="primary"]:hover { background: #05634F; border-color: #05634F; }
    [data-testid="stNumberInput"] input, [data-testid="stTextInput"] input {
        min-height: 2.2rem;
    }
    [data-testid="stWidgetLabel"] p { font-size: .79rem; }
    /* A single HTML block for the banner and summary avoids
       whitespace collisions between Markdown blocks. */
    /* Consistent 12px rhythm: banner -> metrics -> content cards. */
    .dashboard-top { margin-bottom: 12px; }
    /* The two dashboard columns each contain two stacked cards. */
    [data-testid="stColumn"] > [data-testid="stVerticalBlock"] {
        gap: 12px !important;
    }
    .brand-banner {
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        min-height: 60px;
        padding: 8px 17px;
        border-radius: 18px;
        background: linear-gradient(110deg, #FFFFFF 3%, #F2FBF8 53%, #D9F2EA 100%);
        border: 1px solid #DAEDE6;
        margin-bottom: 12px;
    }
    .brand-banner::after {
        content: ""; position: absolute; pointer-events: none;
        width: 320px; height: 190px; right: -45px; top: -107px;
        border-radius: 45%; transform: rotate(-17deg);
        background: rgba(77, 182, 148, .14);
    }
    .brand-banner::before {
        content: ""; position: absolute; pointer-events: none;
        width: 210px; height: 160px; right: 160px; bottom: -130px;
        border-radius: 50%; background: rgba(78, 183, 151, .10);
    }
    .brand-leaf {
        display: grid; place-items: center; flex-shrink: 0;
        width: 42px; height: 42px; margin-right: 10px;
        background: linear-gradient(135deg,#E4F9EC,#C4EBDB);
        color: #14785C; border-radius: 12px; font-size: 1.58rem;
    }
    .brand-title { font-size: 1.58rem; font-weight: 800; line-height: 1.1; color: #102F3D; }
    .brand-caption { font-size: .85rem; margin-top: 4px; color: #456870; }
    /* Appliance count stays available without a redundant Dashboard heading. */
    .intro-chip {
        margin-left: auto; z-index: 1; position: relative;
        color: #12755E; font-size: .73rem; font-weight: 700;
        border: 1px solid #CBE8DC; background: #EAF8F0;
        border-radius: 99px; padding: 5px 12px; white-space: nowrap;
    }
    .metric-row { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 12px; }
    .metric-box {
        display: flex; align-items: center; gap: 12px;
        height: 70px; padding: 8px 12px;
        border: 1px solid #D5EAE3; border-radius: 17px;
        background: linear-gradient(118deg,#E6F5F0,#F5FBF8);
    }
    .metric-box.highlight { background: linear-gradient(118deg,#E8F7E4,#F4FBEF); }
    .metric-icon { display: grid; place-items: center; flex-shrink: 0;
        width: 38px; height: 38px; background: #D3EEE4;
        border-radius: 50%; color: #0E7A62; font-size: 1.35rem; }
    .highlight .metric-icon { background: #DDF3D0; }
    .metric-label { color: #3D6463; font-size: .78rem; font-weight: 600; margin-bottom: 3px; }
    .metric-value { color: #112F3B; font-size: 1.53rem; font-weight: 800; line-height: 1.07; }
    .metric-footnote { color: #69837B; font-size: .72rem; }
    .panel-head { display: flex; align-items: center; gap: 7px;
        font-size: 1rem; font-weight: 800; color: var(--ink); margin: 0 0 5px; }
    .panel-head span { color: #087B67; }
    .panel-caption { color: #6C8380; font-size: .75rem; }
    .blank-state { background: #F1F8F5; border: 1px dashed #C9E1D7;
        border-radius: 11px; padding: 15px 10px; text-align: center;
        color: #67827B; font-size: .83rem; }
    .device-row { display: flex; justify-content: space-between; align-items: center;
        gap: 10px; min-height: 28px; padding: 5px 8px;
        border: 1px solid #E0EEE8; border-radius: 10px; background: #F5FAF8; }
    .device-name { font-weight: 700; color: #193A40; font-size: .82rem; }
    .device-detail { font-size: .71rem; color: #668078; }
    .device-price { padding: 3px 7px; color:#126447; background:#E3F6E9;
        border-radius: 7px; font-weight: 700; white-space: nowrap; font-size: .76rem; }
    .empty-small { padding: 11px 8px; color: #708881; font-size: .84rem; }
    .simple-chart { display: grid; grid-template-columns: 36px 1fr; height: 124px; gap: 8px; }
    .chart-axis { height: 92px; display: flex; flex-direction: column;
        justify-content: space-between; color:#82938F; font-size: .66rem; text-align: right; }
    .chart-body { height: 92px; display: flex; align-items: end;
        padding: 4px 15px 0; gap: 9px; border-bottom: 1px solid #C1D7CE;
        background: repeating-linear-gradient(to top, transparent 0,
                    transparent calc(25% - 1px), #EBF2EF calc(25% - 1px), #EBF2EF 25%);
    }
    .bar-item { flex: 1; min-width: 0; display: flex; flex-direction: column;
        align-items: center; justify-content: flex-end; height: 100%; }
    .bar-value { font-size: .69rem; color: #08664F; font-weight: 750;
        white-space: nowrap; margin-bottom: 3px; }
    .bar-column { width: min(100%, 88px); border-radius: 6px 6px 0 0;
        background: linear-gradient(180deg,#078B75,#08705B); }
    .chart-xlabels { display: flex; gap: 9px; padding: 4px 15px 0; }
    .chart-xlabels div { flex:1; min-width:0; text-align:center; font-size:.73rem;
        color: #476B64; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    .soft-result { border-radius: 9px; padding: 6px 8px;
        background: #E5F5E9; color: #14633D; font-size: .80rem; }
    .price-result { border-radius: 9px; padding: 6px 8px;
        background: #E7F6EE; color: #106C50; font-size: .81rem; font-weight: 750; }
    /* Measured inner breathing room below green result banners. */
    .result-bottom-space { display: block; height: 12px; }
    /* Keep appliance controls compact so the savings panel fits below. */
    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
        gap: .35rem;
    }
    .manage-item { padding: 4px 0; overflow-wrap: anywhere; }
    .manage-item strong { color: #173D43; font-size: .89rem; }
    .manage-meta { color: #5C7A7A; font-size: .79rem; line-height: 1.55; }
    .section-page-title { font-size: 1.65rem; font-weight:800; color:#123C42; }
    .section-page-subtitle { font-size: .85rem; color:#5E7B76; margin: 2px 0 10px; }
    @media (max-width: 1050px) {
        .metric-value {font-size: 1.42rem;}
        .metric-box {padding: 9px 11px; gap: 8px;}
    }
    @media (max-width: 680px) {
        .block-container,
        [data-testid="stAppViewBlockContainer"] {
            padding: .6rem .65rem .8rem !important;
        }
        .brand-title {font-size: 1.42rem;}
        .metric-row { grid-template-columns:1fr; }
        .intro-chip {display:none;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def initialize(key, value):
    """Set a default session-state value if the key is not already present."""
    if key not in st.session_state:
        st.session_state[key] = value


def new_id():
    """Return a unique numeric ID for a newly added appliance."""
    result = st.session_state["next_id"]
    st.session_state["next_id"] += 1
    return result


for field, initial in (
    ("appliances", []), ("next_id", 1), ("stored_mode", "Manual"),
    ("stored_manual", 0.30), ("stored_country", "Czech Republic"),
    ("eurostat_price", None), ("eurostat_country", None),
    ("eurostat_period", None), ("savings", None),
):
    initialize(field, initial)

# Keep the user's appliances when upgrading from an earlier app.py.
known_ids = [a["id"] for a in st.session_state["appliances"] if "id" in a]
st.session_state["next_id"] = max(
    st.session_state["next_id"], max(known_ids, default=0) + 1
)
for item in st.session_state["appliances"]:
    if "id" not in item:
        item["id"] = new_id()

COUNTRIES = {"Czech Republic": "CZ", "Germany": "DE", "France": "FR"}


def save_setting(from_widget, to_storage):
    """Copy a widget value to its persistent session-state setting."""
    st.session_state[to_storage] = st.session_state[from_widget]


def get_price():
    """Return the active price per kWh and whether it uses Eurostat euros."""
    if (
        st.session_state["stored_mode"] == "Eurostat"
        and st.session_state["eurostat_price"] is not None
        and st.session_state["stored_country"] == st.session_state["eurostat_country"]
    ):
        return st.session_state["eurostat_price"], True
    return st.session_state["stored_manual"], False


def money(amount, euro):
    """Format a monetary amount, adding EUR for Eurostat prices."""
    return f"EUR {amount:,.2f}" if euro else f"{amount:,.2f}"


def kwh_for_month(item, hours=None):
    """Estimate appliance consumption in kWh over a 30-day month."""
    hours = item["hours"] if hours is None else hours
    return calculate_consumption_for_days(item["power"], hours, 30)


def sig(item):
    """Return the appliance details used to validate a savings result."""
    return item["id"], item["power"], item["hours"]


@st.dialog("Add an appliance")
def appliance_dialog():
    """Show a form for adding an appliance to the current session."""
    with st.form("create_appliance"):
        name = st.text_input("Appliance name", placeholder="e.g. Air conditioner")
        a, b = st.columns(2)
        with a:
            power = st.number_input("Power (W)", min_value=1.0, value=100.0)
        with b:
            hours = st.number_input(
                "Daily usage (hours)", min_value=0.0,
                max_value=24.0, value=5.0, step=0.5,
            )
        submitted = st.form_submit_button("Add Appliance", type="primary")

    if submitted:
        if not name.strip():
            st.error("Please enter an appliance name.")
        else:
            st.session_state["appliances"].append({
                "id": new_id(), "name": name.strip(),
                "power": power, "hours": hours,
            })
            st.session_state["savings"] = None
            st.rerun()


def remove_device(device_id):
    """Remove an appliance by ID and clear the previous savings result."""
    st.session_state["appliances"] = [
        a for a in st.session_state["appliances"] if a["id"] != device_id
    ]
    st.session_state["savings"] = None
    st.session_state.pop("savings_device", None)
    st.rerun()


def chart_html(appliances, price):
    """Build HTML for a bar chart of the five highest appliance costs."""
    values = sorted(
        [(a["name"], kwh_for_month(a) * price) for a in appliances],
        key=lambda pair: pair[1], reverse=True,
    )[:5]
    maximum = max((v for _, v in values), default=0.0)
    scale = maximum if maximum > 0 else 1.0
    axis = "".join(
        f"<span>{scale * p:,.0f}</span>" for p in (1, .75, .5, .25, 0)
    )
    bars, labels = [], []
    for label, value in values:
        # Keep bars within the compact chart area.
        height = max(3, int(value / scale * 71))
        bars.append(
            '<div class="bar-item">'
            f'<div class="bar-value">{value:,.2f}</div>'
            f'<div class="bar-column" style="height:{height}px"></div>'
            '</div>'
        )
        labels.append(
            f'<div title="{escape(label, quote=True)}">{escape(label)}</div>'
        )
    return (
        '<div class="simple-chart">'
        f'<div class="chart-axis">{axis}</div>'
        '<div>'
        f'<div class="chart-body">{"".join(bars)}</div>'
        f'<div class="chart-xlabels">{"".join(labels)}</div>'
        '</div></div>'
    )


def savings_widget(devices, current_price, euro):
    """Display controls and results for reducing appliance usage hours."""
    st.markdown(
        '<div class="panel-head"><span>&#127807;</span> Potential Energy Savings</div>',
        unsafe_allow_html=True,
    )
    if not devices:
        st.markdown(
            '<div class="empty-small">Add an appliance to calculate your savings.</div>',
            unsafe_allow_html=True,
        )
        return

    a, b, c = st.columns([1.05, .95, .8], gap="small", vertical_alignment="bottom")
    with a:
        index = st.selectbox(
            "Appliance", range(len(devices)),
            format_func=lambda i: devices[i]["name"],
            key="savings_device",
        )
    selected = devices[index]
    with b:
        new_hours = st.number_input(
            "New hours/day", min_value=0.0,
            max_value=float(selected["hours"]),
            value=float(selected["hours"]), step=0.5,
            key=f"savings_hours_{selected['id']}",
        )
    with c:
        pressed = st.button(
            "Calculate", type="primary", use_container_width=True,
            key="compute_savings",
        )
    if pressed:
        st.session_state["savings"] = {
            "signature": sig(selected),
            "kwh": kwh_for_month(selected) - kwh_for_month(selected, new_hours),
        }
        st.rerun()

    record = st.session_state["savings"]
    saved_signature = (record.get("signature", record.get("appliance"))
                       if isinstance(record, dict) else None)
    if record is not None and saved_signature == sig(selected):
        st.markdown(
            '<div class="soft-result">&#10003; Potential monthly savings: '
            f'<strong>{escape(money(record["kwh"] * current_price, euro))}</strong></div>'
            '<div class="result-bottom-space" aria-hidden="true"></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="panel-caption">Compare a shorter daily use period to estimate savings.</div>',
            unsafe_allow_html=True,
        )


def price_widget():
    """Show manual and Eurostat electricity price selection controls."""
    st.markdown(
        '<div class="panel-head"><span>&#9889;</span> Electricity Price</div>',
        unsafe_allow_html=True,
    )
    initialize("_price_mode", st.session_state["stored_mode"])
    st.radio(
        "Price source", ["Manual", "Eurostat"], horizontal=True,
        key="_price_mode", label_visibility="collapsed",
        on_change=save_setting, args=("_price_mode", "stored_mode"),
    )
    if st.session_state["stored_mode"] == "Manual":
        initialize("_price_input", st.session_state["stored_manual"])
        st.number_input(
            "Price per kWh", min_value=0.0,
            format="%.4f", step=0.01, key="_price_input",
            on_change=save_setting,
            args=("_price_input", "stored_manual"),
        )
        st.markdown(
            f'<div class="price-result">{st.session_state["stored_manual"]:.4f} per kWh '
            '(custom price)</div>'
            '<div class="result-bottom-space" aria-hidden="true"></div>',
            unsafe_allow_html=True,
        )
    else:
        initialize("_country_input", st.session_state["stored_country"])
        c1, c2 = st.columns([1.7, 1], gap="small", vertical_alignment="bottom")
        with c1:
            st.selectbox(
                "Country", list(COUNTRIES), key="_country_input",
                on_change=save_setting,
                args=("_country_input", "stored_country"),
            )
        with c2:
            if st.button("Get Price", type="primary", use_container_width=True):
                try:
                    with st.spinner("Contacting Eurostat..."):
                        value, period = get_electricity_price(
                            COUNTRIES[st.session_state["stored_country"]]
                        )
                except Exception:  # API/network failures should not crash the UI.
                    value, period = None, None
                if value is None:
                    st.warning("Price unavailable. Using manual rate.")
                else:
                    st.session_state["eurostat_price"] = value
                    st.session_state["eurostat_country"] = st.session_state["stored_country"]
                    st.session_state["eurostat_period"] = period
                    st.rerun()
        price, available = get_price()
        if available:
            st.markdown(
                f'<div class="price-result">EUR {price:.4f}/kWh '
                f'&middot; {escape(str(st.session_state["eurostat_period"]))}</div>'
                '<div class="result-bottom-space" aria-hidden="true"></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="panel-caption">Select a country and retrieve its reference price.</div>',
                unsafe_allow_html=True,
            )


@st.dialog("All Appliances")
def manage_appliances_dialog():
    """Manage every device in a compact, readable dialog."""
    price, euro = get_price()
    devices = st.session_state["appliances"]
    if not devices:
        st.info("No appliances added yet.")
        return
    for item in devices:
        # The action column is wide enough for the complete Remove label.
        left, right = st.columns([3, 1.4], gap="small", vertical_alignment="center")
        with left:
            # HTML entities avoid the corrupted punctuation shown by some setups.
            st.markdown(
                '<div class="manage-item">'
                f'<strong>{escape(item["name"])}</strong>'
                f'<div class="manage-meta">{item["power"]:,.0f} W &nbsp;|&nbsp; '
                f'{item["hours"]:.1f} h/day</div>'
                f'<div class="manage-meta">{kwh_for_month(item):.2f} kWh/month '
                f'&nbsp;|&nbsp; {escape(money(kwh_for_month(item) * price, euro))}/month</div>'
                '</div>',
                unsafe_allow_html=True,
            )
        with right:
            if st.button("Remove", key=f"modal_remove_{item['id']}", use_container_width=True):
                remove_device(item["id"])


@st.dialog("Quick Appliance Calculator")
def quick_calculator_dialog():
    """Estimate usage for a device without adding it to the dashboard."""
    price, euro = get_price()
    power = st.number_input("Power (W)", min_value=1.0, value=100.0, key="quick_power")
    hours = st.number_input(
        "Usage (hours/day)", min_value=0.0, max_value=24.0,
        value=5.0, step=0.5, key="quick_hours",
    )
    usage = calculate_consumption_for_days(power, hours, 30)
    a, b = st.columns(2)
    a.metric("Monthly consumption", f"{usage:.2f} kWh")
    b.metric("Monthly cost", money(usage * price, euro))


def dashboard():
    """Render the single-page energy dashboard and its interactive panels."""
    devices = st.session_state["appliances"]
    unit_price, euro = get_price()
    consumption = sum(kwh_for_month(device) for device in devices)
    total_cost = consumption * unit_price
    saved = st.session_state["savings"]
    saved_signature = (saved.get("signature", saved.get("appliance"))
                       if isinstance(saved, dict) else None)
    valid = (isinstance(saved, dict) and isinstance(saved.get("kwh"), (int, float))
             and any(sig(d) == saved_signature for d in devices))
    savings_value = money(saved["kwh"] * unit_price, euro) if valid else "--"
    savings_description = "Based on your simulation" if valid else "Run the simulator below"

    # Banner and summary in one block: no redundant page title or subtitle.
    st.markdown(
        '<div class="dashboard-top">'
        '<div class="brand-banner">'
        '<div class="brand-leaf">&#127807;</div>'
        '<div><div class="brand-title">EnergyWise</div>'
        '<div class="brand-caption">Home Energy Calculator &amp; Savings Advisor</div></div>'
        f'<div class="intro-chip">{len(devices)} APPLIANCES</div>'
        '</div>'
        '<div class="metric-row">'
        '<div class="metric-box"><div class="metric-icon">&#9889;</div><div>'
        '<div class="metric-label">Monthly Consumption</div>'
        f'<div class="metric-value">{consumption:,.2f} kWh</div></div></div>'
        '<div class="metric-box"><div class="metric-icon">&#128176;</div><div>'
        '<div class="metric-label">Monthly Cost</div>'
        f'<div class="metric-value">{escape(money(total_cost, euro))}</div></div></div>'
        '<div class="metric-box highlight"><div class="metric-icon">&#127807;</div><div>'
        '<div class="metric-label">Potential Savings</div>'
        f'<div class="metric-value">{escape(savings_value)}</div>'
        f'<div class="metric-footnote">{savings_description}</div></div></div>'
        '</div></div>',
        unsafe_allow_html=True,
    )

    # Independent columns let the lower panels sit immediately below their
    # related upper panels; the taller appliance card no longer creates an
    # empty gap below the graph.
    col_left, col_right = st.columns([1.12, 1], gap="small")
    with col_left:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-head"><span>&#128200;</span> Monthly Cost by Appliance</div>',
                unsafe_allow_html=True,
            )
            if devices:
                st.markdown(chart_html(devices, unit_price), unsafe_allow_html=True)
            else:
                st.markdown(
                    '<div class="blank-state">Add an appliance to see your monthly cost chart.</div>',
                    unsafe_allow_html=True,
                )
        # Left, directly under the chart: price source and Eurostat data.
        with st.container(border=True):
            price_widget()

    with col_right:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-head"><span>&#128268;</span> My Appliances</div>',
                unsafe_allow_html=True,
            )
            if devices:
                for device in devices[:3]:
                    left, right = st.columns([7, 1], gap="small", vertical_alignment="center")
                    with left:
                        st.markdown(
                            '<div class="device-row">'
                            '<div>'
                            f'<div class="device-name">{escape(device["name"])}</div>'
                            f'<div class="device-detail">{device["power"]:,.0f} W '
                            f'&nbsp; | &nbsp; {device["hours"]:.1f} h/day</div>'
                            '</div>'
                            f'<div class="device-price">{escape(money(kwh_for_month(device)*unit_price, euro))}</div>'
                            '</div>', unsafe_allow_html=True,
                        )
                    with right:
                        if st.button("X", key=f"delete_dash_{device['id']}",
                                     help="Remove appliance", use_container_width=True):
                            remove_device(device["id"])
            else:
                st.markdown(
                    '<div class="empty-small">No appliances yet. Add one to start tracking.</div>',
                    unsafe_allow_html=True,
                )
            # Add breathing room between the device rows and their action buttons.
            # Scope this to nonempty lists so the empty state remains compact.
            if devices:
                st.markdown('<div style="height: 7px;" aria-hidden="true"></div>',
                            unsafe_allow_html=True)
            button_cols = st.columns([1.2, 1.4, 1] if len(devices) > 3 else [1, 1.2], gap="small")
            with button_cols[0]:
                if st.button("+ Add Appliance", type="primary", key="dash_add",
                             use_container_width=True):
                    appliance_dialog()
            with button_cols[1]:
                if st.button("Quick Calculator", key="dash_quick",
                             use_container_width=True):
                    quick_calculator_dialog()
            if len(devices) > 3:
                with button_cols[2]:
                    if st.button("View All", key="dash_view_all", use_container_width=True):
                        manage_appliances_dialog()

        # Right, directly under the appliance list: saving simulator.
        with st.container(border=True):
            savings_widget(devices, unit_price, euro)



# All functionality is available on the dashboard. No top or side navigation.
dashboard()

