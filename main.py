import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# matplotlib inline
# specify the style of graph we want
st.set_page_config(layout="centered", initial_sidebar_state="auto")


plt.style.use('fivethirtyeight')
st.title("Footballer Analysis ")

st.sidebar.markdown(
    "<h1 style='font-size:35px; color:#060f73;'>Premier League Footballer Data Analysis Visualisation</h1>", 
    unsafe_allow_html=True
)
st.sidebar.markdown(
    "<h1 style='font-size:20px; color:#060f73;'>2023-24 Season </h1>", 
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Target the sidebar */
    [data-testid="stSidebar"] {
        background-color: #dff5df;
    }
    </style>
    """,
    unsafe_allow_html=True
)




#st.sidebar.markdown("# Premier League Footballer Data analysis visualisation", font-size = 35, color = 'green')


players = pd.read_csv('premier-player-23-24.csv')

salary_data = pd.read_csv('premier-player-23-24 - with salaries.csv')



regular_players = players.copy()
regular = regular_players['Min'] > 500
regular_players = regular_players[regular]
regular_players_GA = regular_players[['Player', 'Pos', 'Min', 'Gls', 'PK', 'Ast', 'G+A', 'xG','xG_90', 'xAG', 'xAG_90', 'xG+xAG_90', 'Team']]
xG = regular_players_GA['xG']
xAG = regular_players_GA['xAG']
xG_xAG = xG + xAG
regular_players_GA['xG + xAG'] = xG_xAG
regular_players_GA['Gls - XG'] = regular_players_GA['Gls'] - regular_players_GA['xG']
regular_players_GA['Ast - XAG'] = regular_players_GA['Ast'] - regular_players_GA['xAG']
good_finishers = regular_players_GA.sort_values('Gls - XG', ascending = False).head(10)
good_assisters = regular_players_GA.sort_values('Ast - XAG', ascending = False).head(10)
bad_finishers = regular_players_GA.sort_values('Gls - XG', ascending = True).head(10)
bad_assisters = regular_players_GA.sort_values('Ast - XAG', ascending = True).head(10)
sort_by_finishing = regular_players_GA.sort_values('Gls - XG', ascending = False)
best_outisde_top6_finishers = sort_by_finishing[~sort_by_finishing['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
best_outisde_top6_finishers = best_outisde_top6_finishers[best_outisde_top6_finishers['Pos'].isin(['FW', 'MF,FW', 'FW,MF'])].head(12)
progressive = players.copy()
progressive = progressive[['Player', 'Pos','Age', 'Min', 'PrgC', 'PrgP', 'PrgR', 'Team']]
progressive['Progressiveness'] = progressive['PrgC'] + progressive['PrgP'] + progressive['PrgR']
progressive['Progressiveness per 90'] = (progressive['Progressiveness'] / progressive['Min']) * 90
progressive_mid = (progressive['Pos'] == 'MF') & (progressive['Min'] > 300)
progressive_mid_only = progressive[progressive_mid] 
top_progressive_mid = progressive_mid_only.sort_values('Progressiveness per 90', ascending = False).head(12)
worse_progressive_mid = progressive_mid_only.sort_values('Progressiveness per 90', ascending = True).head(12)
outsideTop6_Progmid = progressive_mid_only[~progressive_mid_only['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
top_outsideTop6_Progmid = outsideTop6_Progmid.sort_values('Progressiveness per 90', ascending=False).head(12)
top6_progmid = progressive_mid_only[progressive_mid_only['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
worse_top6_progmid = top6_progmid.sort_values('Progressiveness per 90', ascending=True).head(12)
sort_by_assists = regular_players_GA.sort_values('Ast - XAG', ascending = True)
unlucky_assist_outside_top6 = sort_by_assists[~sort_by_assists['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])].head(12)



choose_option = st.sidebar.selectbox(
    'Choose one option',
    ['Option', 'Attacking Output', 'Progressiveness', 'Salaries'])
if choose_option == 'Option':
   st.title('')
   st.write('#### Please choose an analysis option')
   st.write('')
elif choose_option == 'Attacking Output':
  Attacking_output = st.sidebar.selectbox(
    'Choose an attacking analysis option',
    ['Attacking Output','Top finishers','Worst Finishers', 'Top assisters','Unlucky assisters', 'Top finishers outside top 6', 'Unlucky assisters outside top 6'])
  if Attacking_output == 'Attacking Output':
    'Please choose a visualisation you wish to see'
  elif Attacking_output == 'Top finishers':
    'These are the top finishers'
    good_finishers[['Player', 'Team', 'Gls', 'xG', 'xG_90', 'Gls - XG']]
    fig, axes = plt.subplots(1, 1, figsize=(12, 7))

    # Create a color map (adjust np.linspace to match the number of bars)
    colors = plt.cm.cool(np.linspace(0, 1, len(good_finishers['Player'])))

    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(1, 1, figsize=(12, 8))

    # Create a color map (adjust np.linspace to match the number of bars)
    colors = plt.cm.cool(np.linspace(0, 1, len(good_finishers['Player'])))

    # Plot data for good finishers on the first subplot (axes[0])
    axes.bar(good_finishers['Player'], good_finishers['Gls - XG'], color=colors)
    axes.set_title('Top finishers (overperforming xG)', pad=30)
    axes.tick_params(axis='x', rotation=90)
    axes.set_xlabel('Player', labelpad=20)
    axes.set_ylabel('Goals above expected')

    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
        
  elif Attacking_output == 'Worst Finishers':
    'These are the worst finishers'  
    bad_finishers[['Player', 'Team', 'Gls', 'xG', 'xG_90', 'Gls - XG']]
    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(1, 1, figsize=(14, 8))

    # Create a color map (adjust np.linspace to match the number of bars)
    colors = plt.cm.cool(np.linspace(0, 1, len(good_finishers['Player'])))



    axes.bar(bad_finishers['Player'], bad_finishers['Gls - XG'], color=colors)
    axes.set_title('Bad finishers (underperforming xG)', pad=30)
    axes.tick_params(axis='x', rotation=90)
    axes.set_xlabel('Player', labelpad=20)
    axes.set_ylabel('Goals below expected')

    # Adjust layout to make room for rotated labels
    plt.tight_layout()

    plt.show()
    st.pyplot(fig)

  elif Attacking_output == 'Top assisters':
     'These are the top assisters'
     good_assisters[['Player', 'Team', 'Ast', 'xAG', 'xAG_90', 'Ast - XAG']]
     # Create a figure with two subplots side by side
     fig, axes = plt.subplots(1, 1, figsize=(10, 6))

     # Create a color map (adjust np.linspace to match the number of bars)
     colors = plt.cm.cool(np.linspace(0, 1, len(good_assisters['Player'])))

     # Plot data for good finishers on the first subplot (axes[0])
     axes.bar(good_assisters['Player'], good_assisters['Ast - XAG'], color=colors)
     axes.set_title('Top Assisters (overperforming xAG)', pad=30)
     axes.tick_params(axis='x', rotation=90)
     axes.set_xlabel('Player', labelpad=20)
     axes.set_ylabel('Assists above expected')

     # Adjust layout to make room for rotated labels
     plt.tight_layout()
     plt.show()
     st.pyplot(fig)


  elif Attacking_output == 'Unlucky assisters':
     'These are the Unlucky assisters - They should have had more assists from the chances they created'
     bad_assisters[['Player', 'Team', 'Ast', 'xAG', 'xAG_90', 'Ast - XAG']]
     # Create a figure with two subplots side by side
     fig, axes = plt.subplots(1, 1, figsize=(10, 6))

     # Create a color map (adjust np.linspace to match the number of bars)
     colors = plt.cm.cool(np.linspace(0, 1, len(good_assisters['Player'])))

     # Plot data for good finishers on the first subplot (axes[0])
     axes.bar(bad_assisters['Player'], bad_assisters['Ast - XAG'], color=colors)
     axes.set_title('Unlucky Assisters (underperforming xAG)', pad=30)
     axes.tick_params(axis='x', rotation=90)
     axes.set_xlabel('Player', labelpad=20)
     axes.set_ylabel('Assists below expected')

     # Adjust layout to make room for rotated labels
     plt.tight_layout()
     plt.show()
     st.pyplot(fig) 


  elif Attacking_output == 'Top finishers outside top 6':
     " These are the top finishers outside the traditional 'top 6'"   
     best_outisde_top6_finishers
     fig, axes = plt.subplots(1, 1, figsize=(10, 5))

     # Create a color map (adjust np.linspace to match the number of bars)
     colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
     colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

     # Plot data for good finishers on the first subplot (axes[0])
     axes.bar(best_outisde_top6_finishers['Player'], best_outisde_top6_finishers['Gls - XG'], color=colors)
     axes.set_title('Top Finishers outside Top 6 (overperforming xG)', pad=30)
     axes.tick_params(axis='x', rotation=90)
     axes.set_xlabel('Player', labelpad=20)
     axes.set_ylabel('Goals above expected (xG)')
     st.pyplot(fig)


  elif Attacking_output == 'Unlucky assisters outside top 6':
     " These are the unlucky assisters outside the traditional 'top 6'"   
     unlucky_assist_outside_top6
     fig, axes = plt.subplots(1, 1, figsize=(10, 5))

     # Create a color map (adjust np.linspace to match the number of bars)
     colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
     colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

     # Plot data for good finishers on the first subplot (axes[0])
     axes.bar(unlucky_assist_outside_top6['Player'], unlucky_assist_outside_top6['Ast - XAG'], color=colors2)
     axes.set_title('Unlucky Assisters outside Top 6 (Underperforming xAG)', pad=30)
     axes.tick_params(axis='x', rotation=90)
     axes.set_xlabel('Player', labelpad=20)
     axes.set_ylabel('Assists below expected (xAG)')
     st.pyplot(fig)  


elif choose_option == 'Progressiveness':
  Progressiveness = st.sidebar.selectbox(
    'Choose a Position',
    ['Progressiveness','Progressive Midfielders','Progressive Defenders'])
  if Progressiveness == 'Progressiveness':
    'Please choose a visualisation you wish to see'
  elif Progressiveness == 'Progressive Midfielders':
     Midfielders = st.sidebar.selectbox(
        'Choose a Progressive analysis option',
        ['Top Progressive Midfielders','Worst Progressive Midfielders','Progressive Midfielder comparisons', 'Top Progressive Midfielders OUTSIDE top 6','Least Progressive Midfielders IN top 6', 'Top Young progressive midfielders'])
     if Midfielders == 'Top Progressive Midfielders':
        'These are the top progressive midfielders'

     elif Midfielders == 'Worst Progressive Midfielders':
        'These are the least progressive midfielders'

     elif Midfielders == 'Progressive Midfielder comparisons':
        'This is midfielder comparisons'

     elif Midfielders == 'Top Progressive Midfielders OUTSIDE top 6':
        " These are the top progressive midfielsers outside the traditional 'top 6'"

     elif Midfielders == 'Least Progressive Midfielders IN top 6':
        " These are the least progressive midfielsers in the traditional 'top 6'"  
     else:
        'These the the top young progressive midfielders (under 24)'          
    
  elif Progressiveness == 'Progressive Defenders':
    Defenders = st.sidebar.selectbox(
      'Choose a Progressive analysis option',
      ['Top Progressive Defenders', 'Top Progressive Defenders OUTSIDE top 6', 'Top Young progressive defenders', 'Top Young progressive defenders OUTSIDE top 6'])
    if Defenders == 'Top Progressive Defenders':
       'These are the top progressive defenders'
    
    if Defenders == 'Top Progressive Defenders OUTSIDE top 6':
       " These are the top progressive defenders outside the traditional 'top 6'"
    
    if Defenders == 'Top Young progressive defenders':
       'These are the top young progressive defenders (under 24)'

    if Defenders == 'Top Young progressive defenders OUTSIDE top 6':
       " These are the top progressive young defenders outside the traditional 'top 6'"   

  


elif choose_option == 'Salaries':
    Salaries = st.sidebar.selectbox(
    'Choose a Salary analysis option',
    ['Salaries','Top Salaries', 'Top Team Average salaries', 'Salary compared to G+A', 'Salary compared to finishing', 'salary compared to finishing + assists', 'salary compared to progressiveness (midfielders)'])
    if Salaries == 'Salaries':
       'Please choose an analysis you wish to see'
    elif Salaries == 'Top Salaries':
        'These are the top salaries'
    elif Salaries == 'Top Team Average salaries':
        'These are the teams with the highest average yearly salaries'
    elif Salaries == 'Salary compared to G+A':
       'Salaries compared to goals and assists'
    elif Salaries == 'Salary compared to finishing':
       'Salaries compared to finishing level (overachive xG)'
    elif Salaries == 'salary compared to finishing + assists':
       'Salaries compared to finishing level (overachive xG) and expected assists'
    elif Salaries == 'salary compared to progressiveness (midfielders)':
       'Midfielders salaries compared to their progressiveness rank '         

        
else:
   'Please Choose an Option'


