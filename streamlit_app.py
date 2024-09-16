import streamlit as st

# Define sector options
sector_options = {
    'Fintech': 1, 'Ed-tech': 2, 'Agri-tech': 3, 'Logistics': 4, 'EV': 5, 'BPC': 6, 
    'Apparels': 7, 'Healthcare': 8, 'F&B': 9, 'Solar Energy': 10, 'SaaS': 11, 
    'Proptech': 12, 'Stationary and Gifting': 13, 'Insurance': 14, 'Gaming': 15, 
    'Media and Content': 16, 'HR Tech': 17, 'Hospitality': 18, 'Network and Cloud': 19, 
    'Travel': 20, 'Metals and Mining': 21
}
stage_options={
    'Pre-seed':1, 'Pre-Series A':2, 'Series A':3, 'Series B':4, 'Series C':5, 'Series D':6, 'Series E':7
}

st.title("Startup Information Form")

# Input fields
name = st.text_input('Please enter the name of your startup:')
sector = st.selectbox('Please select the primary sector your startup falls under:', options=list(sector_options.keys()))
stage = st.selectbox('Please select the primary sector your startup falls under:', options=list(stage_options.keys()))
funds = st.text_input('How much money have you fundraised?')
purpose = st.text_input('What is your purpose for raising money?')
prior = st.selectbox('Have you raised any external funding before, including bank loans?', ['Yes', 'No'])

if prior == 'Yes':
    amount = st.text_input("Amount of funds raised till date:")
    date = st.text_input('When did you raise this money? MM-YYYY: ')
    mode = st.text_input('Mode of funds')
    loan = st.text_input('Amount of loans taken out: ')
    ei = st.text_input('Please enter your equity investment: ')
    
out_loan = st.text_input('What is the outstanding loan amount as of the last balance sheet? ')
share_equity = st.text_input('What is the shareholder\'s equity in the company? ')
MIE = st.text_input("What is the existing Monthly Interest Expense? ")
Inst_invest = st.selectbox("Is there an institutional investor in the company?", ['Yes', 'No'])
P_promoter = st.number_input("What is the % of promoter holding in the company?", min_value=0.0, max_value=100.0)
Revenue = st.number_input("What was your revenue in the last fiscal year or LTM? Please enter just a number. ")
Rec_Rev = st.text_input("What was the monthly recurring revenue/ average monthly revenue?")
EBIT = st.text_input("What was the EBIT margin (%) of the company in the LTM? Please enter without percent symbol. ")
Phys_asset = st.text_input("Does the company/promoter own any physical assets that can be used as collateral for financing? ")
cash_burn = st.text_input("What is monthly cash burn? ")
in_hand = st.text_input("What is the amount of capital available at the moment in hand? ")
flow = st.text_input("What is the monthly operating cash flow?")
net_profit = st.number_input('What is your net profit?', format="%f")
NCE = st.number_input('What are you non-cash expenses?', format="%f")
Inc_rec = st.number_input('What was the increase in trade receivables and other current assets?', format="%f")
Dec_pay = st.number_input('What was the decrease in trade payables and other current liabilities?', format="%f")

# Computations
if st.button('Calculate Results'):
    st.write('RECCOMENDATIONS FOR YOU:')
    D_E_Ratio = float(out_loan) / float(share_equity) if share_equity else 0
    ICR = (float(EBIT) * float(Revenue)) / (float(MIE) * float(amount)) if MIE and amount else 0
    Runway = float(in_hand) / float(cash_burn) if cash_burn else 0
    NWC = Inc_rec + Dec_pay
    OCF = net_profit + NCE - NWC
    OCF2R = OCF / float(Rec_Rev) if Rec_Rev else 0

    # Display computations
    st.write(f'D:E Ratio: {D_E_Ratio}')
    st.write(f'ICR: {ICR}')
    st.write(f'Runway: {Runway}')
    st.write(f'Net Working Capital: {NWC}')
    st.write(f'OCF: {OCF}')
    st.write(f'Operating Cash Flow to Revenue: {OCF2R}')

    # Scoring
    score = 0
    if int(Revenue) < 20000000:
        score += 1
    elif int(Revenue) >= 20000000 and int(Revenue) < 100000000:
        score += 2
    elif int(Revenue) >= 100000000 and int(Revenue) < 250000000:
        score += 3
    elif int(Revenue) >= 250000000 and int(Revenue) < 500000000:
        score += 4
    elif int(Revenue) >= 500000000:
        score += 5

    if int(EBIT) < 2:
        score += 1
    elif int(EBIT) >= 2 and int(EBIT) < 5:
        score += 2
    elif int(EBIT) >= 5 and int(EBIT) < 10:
        score += 3
    elif int(EBIT) >= 10 and int(EBIT) < 20:
        score += 4
    elif int(EBIT) >= 20:
        score += 5

    if D_E_Ratio > 2:
        score += 1
    if D_E_Ratio < 2:
        score += 5

    if ICR < 1:
        score += 1
    elif ICR > 1:
        score += 5

    if OCF >= 0 and OCF < 20:
        score += 1
    elif OCF >= 20 and OCF < 40:
        score += 2
    elif OCF >= 40 and OCF < 60:
        score += 3
    elif OCF >= 60 and OCF < 80:
        score += 4
    elif OCF >= 80:
        score += 5

    if P_promoter >= 50 and P_promoter < 65:
        score += 1
    elif P_promoter >= 65 and P_promoter < 80:
        score += 2
    elif P_promoter >= 80:
        score += 3

    if Inst_invest == 'Yes':
        score += 1
    else:
        score += 2

    st.write(f'Score: {score}')

    # Display recommended distribution based on score
    if score == 5:
        st.write('Your recommended distribution for gaining capital is: \n 14.3% SAFE \n 14.3% Sweat equity \n 11.25% Equity Shares \n 11.25% Preference Shares \n 12% Convertible Preference Shares \n 16% Debentures \n 12% Convertible debentures \n 12% Convertible note \n 17% Unsecured loan \n 17% secured loan \n 13% Venture Debt \n 10% Revenue Based Financing \n 11% Crowdfunding \n 14.3% Grants')
    elif score == 6:
        st.write('Your recommended distribution for gaining capital is: \n 14.3% SAFE \n 14.3% Sweat equity \n 11.25% Equity Shares \n 11.25% Preference Shares \n 12% Convertible Preference Shares \n 10% Debentures \n 12% Convertible debentures \n 12% Convertible note \n 10% Unsecured loan \n 10% secured loan \n 5% Venture Debt \n 10% Revenue Based Financing \n 15% Crowdfunding \n 14.3% Grants')
    elif score == 7:
        st.write('Your recommended distribution for gaining capital is: \n 14.3% SAFE \n 14.3% Sweat equity \n 11.25% Equity Shares \n 11.25% Preference Shares \n 12% Convertible Preference Shares \n 16% Debentures \n 12% Convertible debentures \n 12% Convertible note \n 17% Unsecured loan \n 17% secured loan \n 13% Venture Debt \n 10% Revenue Based Financing \n 11% Crowdfunding \n 14.3% Grants')

    # Sector scoring
def scoring(var_name, method):
    if var_name==0:
        st.write(f'{method} is not applicable.')
    elif var_name == 100:
        st.write(f'{method} has a high likelihood of working.')
    elif var_name == 120:
        st.write(f'{method} has a moderately high likelihood of working.')
    elif var_name == 140:
        st.write(f'{method} has a slightly higher than average likelihood of working.')
    elif var_name == 160:
        st.write(f'{method} has a slightly lower than average likelihood of working.')
    elif var_name == 180:
        st.write(f'{method} has a moderately low likelihood of working')
    else:
        st.write(f'{method} is not applicable.')
    return('')

SPrisk = SAFE_sector = ven_deb = unsec_ln = sec_ln = eq_stage = cnvt_pref = deb_stage = cnvt_deb = cnvt_note = R_B_F = lease_asset = crowdfnd = grnt = sweat_sector = 0

# Sector-specific settings
if sector == 'Fintech':
    SPrisk = 140
    SAFE_sector = 140
    if stage == 'Rights issue':
        eq_stage = 100
    elif stage == 'Series A':
        ven_deb = 160
        crowdfnd = 160
        unsec_ln = 160
        sec_ln = 160
        lease_asset = 160
        grnt = 180
        eq_stage = 160
        cnvt_pref = 100
        deb_stage = 180
        cnvt_deb = 100
        cnvt_note = 100
    elif stage in ['Series B', 'Series C', 'Series D', 'Series E']:
        ven_deb = 140
        unsec_ln = 120
        sec_ln = 140
        eq_stage = 180
        cnvt_pref = 100
        deb_stage = 140
        cnvt_deb = 100
        cnvt_note = 100
    elif stage == 'Series B':
        R_B_F = 160
        crowdfnd = 140
        lease_asset = 140
    elif stage == 'Pre-series A':
        R_B_F = 140
        unsec_ln = 180
        eq_stage = 140
        cnvt_pref = 100
        deb_stage = 180
        cnvt_deb = 100
        cnvt_note = 100
    elif stage == 'Pre-seed':
        unsec_ln = 160
        eq_stage = 120
        cnvt_pref = 100
        deb_stage = 200
        cnvt_deb = 100
        cnvt_note = 100

elif sector == '2':
    SPrisk = 180
    SAFE_sector = 140

elif sector == '3':
    SPrisk = 180
    unsec_ln = 180
    SAFE_sector = 180

elif sector == '4':
    SPrisk = 180
    SAFE_sector = 140

elif sector == '5':
    SPrisk = 180
    lease_asset = 160

elif sector == '6':
    SPrisk = 140
    R_B_F = 140
    unsec_ln = 160
    sweat_sector = 160

elif sector == '7':
    SPrisk = 140
    R_B_F = 140
    sweat_sector = 180
    sec_ln = 140

elif sector == '8':
    SPrisk = 160
    sec_ln = 160
    lease_asset = 160

elif sector == '9':
    SPrisk = 160
    sec_ln = 140
    R_B_F = 160
    sweat_sector = 160

elif sector == '10':
    SPrisk = 140
    ven_deb = 160
    R_B_F = 180
    lease_asset = 140
    sweat_sector = 180

elif sector == '11':
    SPrisk = 120
    R_B_F = 160

elif sector == '12':
    SPrisk = 140

elif sector == '13':
    SPrisk = 120
    unsec_ln = 180
    ven_deb = 180
    sweat_sector = 180
    SAFE_sector = 180

elif sector == '14':
    SPrisk = 160

elif sector == '15':
    SPrisk = 200
    unsec_ln = 180

elif sector == '16':
    SPrisk = 180

elif sector == '17':
    SPrisk = 180
    unsec_ln = 160

elif sector == '18':
    SPrisk = 180
    ven_deb = 180
    lease_asset = 160
    unsec_ln = 160

elif sector == '19':
    SPrisk = 160

elif sector == '20':
    SPrisk = 180

elif sector == '21':
    SPrisk = 160

# Risk level
if SPrisk == 120:
    st.write('Your sector is at a relatively low risk')
elif SPrisk == 140:
    st.write('Your sector is at a moderately low risk')
elif SPrisk == 160:
    st.write('Your sector is at a slightly above average risk level')
elif SPrisk == 180:
    st.write('Your sector is at a high risk level.')
elif SPrisk == 200:
    st.write('Your sector is at a very high risk level.')
elif SPrisk == 100:
    st.write('Your sector is at a low risk level.')

# Display scoring results
st.write(scoring(SAFE_sector, 'SAFE'))
st.write(scoring(sweat_sector, 'Sweat equity'))
st.write(scoring(eq_stage, 'Equity Shares'))
st.write(scoring(cnvt_pref, 'Convertible Preference Shares'))
st.write(scoring(deb_stage, 'Debentures'))
st.write(scoring(cnvt_deb, 'Convertible Debentures'))
st.write(scoring(cnvt_note, 'Convertible Note'))
st.write(scoring(unsec_ln, 'Unsecured Loan'))
st.write(scoring(sec_ln, 'Secured Loan'))
st.write(scoring(ven_deb, 'Venture Debt'))
st.write(scoring(R_B_F, 'RBF'))
st.write(scoring(lease_asset, 'Lease Assets'))
st.write(scoring(crowdfnd, 'Crowdfunding'))
st.write(scoring(grnt, 'Grants'))
