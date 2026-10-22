
import streamlit as st


class BijliBillCalculator:
    """Calculate an estimated electricity bill using OOP."""

    def __init__(self, units, rate_per_unit, fixed_charges, tax_percent):
        self.units = units
        self.rate_per_unit = rate_per_unit
        self.fixed_charges = fixed_charges
        self.tax_percent = tax_percent

    def calculate_bill(self):
        self.energy_charges = self.units * self.rate_per_unit
        self.tax_amount = (
            self.energy_charges * self.tax_percent / 100
        )
        self.total_bill = (
            self.energy_charges
            + self.fixed_charges
            + self.tax_amount
        )
        return self.total_bill

    def get_breakdown(self):
        self.calculate_bill()
        return {
            "Units consumed": self.units,
            "Rate per unit": self.rate_per_unit,
            "Energy charges": self.energy_charges,
            "Fixed charges": self.fixed_charges,
            "Estimated tax": self.tax_amount,
            "Total bill": self.total_bill,
        }


# ---------- Page configuration ----------
st.set_page_config(
    page_title="Bijli Bill Calculator",
    page_icon="⚡",
    layout="wide",
)



# ---------- Refined Professional Blue Theme ----------
st.markdown(
    """
    <style>
    .stApp {
        background: #EAF0F7;
        color: #24364B;
        font-family: "Segoe UI", Arial, sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(234, 240, 247, 0.95);
    }

    [data-testid="stSidebar"] {
        background: #F8FAFD;
        border-right: 1px solid #D4DFEC;
    }

    [data-testid="stSidebar"] * {
        color: #24364B;
    }

    h1, h2, h3 {
        color: #183451 !important;
        font-family: "Segoe UI", Arial, sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.35px;
    }

    p, label, .stMarkdown {
        color: #40546B;
    }

    [data-testid="stMetric"] {
        background: #FDFEFF;
        border: 1px solid #D2DFED;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 3px 10px rgba(31, 57, 85, 0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #52677E !important;
    }

    [data-testid="stMetricValue"] {
        color: #246EB2 !important;
        font-weight: 700;
    }

    [data-testid="stMetricDelta"] {
        color: #40546B !important;
    }

    .stButton > button,
    .stDownloadButton > button,
    div[data-testid="stDownloadButton"] button {
        background-color: #286FAF !important;
        color: #FFFFFF !important;
        border: 1px solid #286FAF !important;
        border-radius: 8px !important;
        min-height: 44px;
        padding: 9px 18px;
        font-weight: 600;
        box-shadow: none;
    }

    /* Keep receipt button text visible */
    .stDownloadButton button *,
    div[data-testid="stDownloadButton"] button * {
        color: #FFFFFF !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover,
    div[data-testid="stDownloadButton"] button:hover {
        background-color: #1D568A !important;
        border-color: #1D568A !important;
        color: #FFFFFF !important;
    }

    .stButton > button:focus,
    .stDownloadButton > button:focus {
        outline: 2px solid #79B7ED !important;
        outline-offset: 2px;
    }

    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {
        background-color: #FFFFFF !important;
        color: #24364B !important;
        border-color: #C4D3E3 !important;
        border-radius: 7px;
    }

    [data-baseweb="select"] > div {
        background-color: #FFFFFF;
        border-color: #C4D3E3;
    }

    hr {
        border-color: #D2DFED;
    }

    [data-testid="stAlert"] {
        border-radius: 9px;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# ---------- Main application ----------
st.title("⚡ Bijli Bill Calculator")
st.caption("OBJECT-ORIENTED PROGRAMMING • ELECTRICITY BILL ESTIMATOR")

st.markdown(
    """
    Calculate your estimated electricity bill with a clear
    breakdown of energy charges, fixed charges, and tax.
    """
)

st.warning(
    "Educational estimate only: the sample rates below are not "
    "official electricity tariffs. Actual bills may include slab "
    "rates, surcharges, duties, adjustments, and other charges."
)

# ---------- User inputs ----------
st.sidebar.header("⚙️ Bill Settings")
st.sidebar.caption("Adjust these sample values for your estimate.")

units = st.sidebar.number_input(
    "Units consumed (kWh)",
    min_value=0,
    max_value=100000,
    value=200,
    step=10,
)

rate_per_unit = st.sidebar.number_input(
    "Rate per unit (Rs.)",
    min_value=0.0,
    max_value=10000.0,
    value=35.0,
    step=1.0,
)

fixed_charges = st.sidebar.number_input(
    "Fixed charges (Rs.)",
    min_value=0.0,
    max_value=1000000.0,
    value=500.0,
    step=50.0,
)

tax_percent = st.sidebar.number_input(
    "Estimated tax (%)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=1.0,
)

# ---------- Create object and calculate ----------
calculator = BijliBillCalculator(
    units=units,
    rate_per_unit=rate_per_unit,
    fixed_charges=fixed_charges,
    tax_percent=tax_percent,
)

total = calculator.calculate_bill()
bill = calculator.get_breakdown()

# ---------- Results ----------
st.subheader("Your Bill Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Units Consumed", f"{units:,.0f} kWh")

with col2:
    st.metric("Energy Charges", f"Rs. {bill['Energy charges']:,.2f}")

with col3:
    st.metric("Estimated Total", f"Rs. {total:,.2f}")

st.divider()
st.subheader("📄 Bill Breakdown")

display_rows = [
    ("Units consumed", f"{units:,.0f} kWh"),
    ("Rate per unit", f"Rs. {rate_per_unit:,.2f}"),
    ("Energy charges", f"Rs. {bill['Energy charges']:,.2f}"),
    ("Fixed charges", f"Rs. {fixed_charges:,.2f}"),
    (f"Estimated tax ({tax_percent:g}%)", f"Rs. {bill['Estimated tax']:,.2f}"),
    ("TOTAL PAYABLE (ESTIMATE)", f"Rs. {total:,.2f}"),
]

for label, amount in display_rows:
    left, right = st.columns([3, 1])
    left.write(label)
    right.markdown(f"**{amount}**")

st.divider()

# ---------- Downloadable bill ----------
receipt = f"""
BIJLI BILL CALCULATOR
Estimated Electricity Bill

Units Consumed: {units} kWh
Rate per Unit: Rs. {rate_per_unit:.2f}
Energy Charges: Rs. {bill['Energy charges']:.2f}
Fixed Charges: Rs. {fixed_charges:.2f}
Estimated Tax: Rs. {bill['Estimated tax']:.2f}

TOTAL ESTIMATED BILL: Rs. {total:.2f}

Note: This is an educational estimate, not an official utility bill.
"""

st.download_button(
    label="📥 Download Bill Receipt",
    data=receipt,
    file_name="bijli_bill_receipt.txt",
    mime="text/plain",
)

st.caption(
    "Built with Python, Streamlit, classes, objects, and methods."
)
