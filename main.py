import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# matplotlib inline
# specify the style of graph we want
st.set_page_config(layout="centered", initial_sidebar_state="expanded")


plt.style.use('fivethirtyeight')


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

salaries = pd.read_csv('premier-player-23-24 - with salaries.csv')



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
good_finishers = good_finishers.reset_index()
del good_finishers['index']
good_assisters = regular_players_GA.sort_values('Ast - XAG', ascending = False).head(10)
good_assisters = good_assisters.reset_index()
del good_assisters['index']
bad_finishers = regular_players_GA.sort_values('Gls - XG', ascending = True).head(10)
bad_finishers = bad_finishers.reset_index()
del bad_finishers['index']
bad_assisters = regular_players_GA.sort_values('Ast - XAG', ascending = True).head(10)
bad_assisters = bad_assisters.reset_index()
del bad_assisters['index']
sort_by_finishing = regular_players_GA.sort_values('Gls - XG', ascending = False)
best_outisde_top6_finishers = sort_by_finishing[~sort_by_finishing['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
best_outisde_top6_finishers = best_outisde_top6_finishers[best_outisde_top6_finishers['Pos'].isin(['FW', 'MF,FW', 'FW,MF'])].head(12)
best_outisde_top6_finishers = best_outisde_top6_finishers.reset_index()
del best_outisde_top6_finishers['index']
progressive = players.copy()
progressive = progressive[['Player', 'Pos','Age', 'Min', 'PrgC', 'PrgP', 'PrgR', 'Team']]
progressive['Progressiveness'] = progressive['PrgC'] + progressive['PrgP'] + progressive['PrgR']
progressive['Progressiveness per 90'] = (progressive['Progressiveness'] / progressive['Min']) * 90
progressive_mid = (progressive['Pos'] == 'MF') & (progressive['Min'] > 300)
progressive_mid_only = progressive[progressive_mid] 
top_progressive_mid = progressive_mid_only.sort_values('Progressiveness per 90', ascending = False).head(12)
top_progressive_mid = top_progressive_mid.reset_index()
del top_progressive_mid['index']
worse_progressive_mid = progressive_mid_only.sort_values('Progressiveness per 90', ascending = True).head(12)
worse_progressive_mid = worse_progressive_mid.reset_index()
del worse_progressive_mid['index']
outsideTop6_Progmid = progressive_mid_only[~progressive_mid_only['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
top_outsideTop6_Progmid = outsideTop6_Progmid.sort_values('Progressiveness per 90', ascending=False).head(12)
top_outsideTop6_Progmid = top_outsideTop6_Progmid.reset_index()
del top_outsideTop6_Progmid['index']
top6_progmid = progressive_mid_only[progressive_mid_only['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
top6_progmid = top6_progmid.reset_index()
del top6_progmid['index']
worse_top6_progmid = top6_progmid.sort_values('Progressiveness per 90', ascending=True).head(12)
worse_top6_progmid = worse_top6_progmid.reset_index()
del worse_top6_progmid['index']
sort_by_assists = regular_players_GA.sort_values('Ast - XAG', ascending = True)
unlucky_assist_outside_top6 = sort_by_assists[~sort_by_assists['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])].head(12)
unlucky_assist_outside_top6 = unlucky_assist_outside_top6.reset_index()
del unlucky_assist_outside_top6['index']
Top_prog_mid = progressive_mid_only.sort_values('Progressiveness per 90', ascending=False)
Top_prog_mid = Top_prog_mid.reset_index()
del Top_prog_mid['index']
Top_young_prog_mid = Top_prog_mid['Age'] < 24
Top_young_progressive_midfield = Top_prog_mid[Top_young_prog_mid]
Top_young_progressive_midfield = Top_young_progressive_midfield.reset_index()
del Top_young_progressive_midfield['index']
Top_young_progressive_midfielder_outsideTop6 = Top_young_progressive_midfield[~Top_young_progressive_midfield['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
Top_young_progressive_midfielder_outsideTop6 = Top_young_progressive_midfielder_outsideTop6.head(12)
Top_young_progressive_midfielder_outsideTop6 = Top_young_progressive_midfielder_outsideTop6.reset_index()
del Top_young_progressive_midfielder_outsideTop6['index']
progressive_def = (progressive['Pos'] == 'DF') & (progressive['Min'] > 500)
progressive_def_only = progressive[progressive_def]
Top_progressive_def = progressive_def_only.sort_values('Progressiveness per 90', ascending=False)
Top_progressive_def = Top_progressive_def.reset_index()
del Top_progressive_def['index']
Top12_progressive_def = Top_progressive_def.head(12)
Top_progressive_Defenders_outsideTop6 = Top_progressive_def[~Top_progressive_def['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
Top_progressive_Defenders_outsideTop6 = Top_progressive_Defenders_outsideTop6.reset_index()
del Top_progressive_Defenders_outsideTop6['index']
Top12_progressive_Defenders_outsideTop6 = Top_progressive_Defenders_outsideTop6.head(12)
Top_prog_def = progressive_def_only.sort_values('Progressiveness per 90', ascending=False)
Top_young_prog_def = Top_prog_def['Age'] < 24
Top_young_progressive_defender = Top_prog_def[Top_young_prog_def]
Top_young_progressive_defender = Top_young_progressive_defender.reset_index()
del Top_young_progressive_defender['index']
Top12_young_progressive_defender = Top_young_progressive_defender.head(12)
Top_young_progressive_defender_outsideTop6 = Top_young_progressive_defender[~Top_young_progressive_defender['Team'].isin(['Arsenal', 'Manchester City', 'Chelsea', 'Liverpool', 'Tottenham Hotspur', 'Manchester United'])]
Top_young_progressive_defender_outsideTop6 = Top_young_progressive_defender_outsideTop6.reset_index()
del Top_young_progressive_defender_outsideTop6['index']
Top12_young_progressive_defender_outsideTop6 = Top_young_progressive_defender_outsideTop6.head(12)

# Step 1: Remove the '£' symbol and commas
salaries['Yearly Salary'] = salaries['Yearly Salary'].str.replace('£', '').str.replace(',', '')

# Step 2: Convert the cleaned string to integer
salaries['Yearly Salary'] = salaries['Yearly Salary'].astype(int)

salaries['Weekly Wage'] = salaries['Weekly Wage'].str.replace('£', '').str.replace(',', '')

# Step 2: Convert the cleaned string to integer
salaries['Weekly Wage'] = salaries['Weekly Wage'].astype(int)

top_salaries = salaries.sort_values(by='Yearly Salary', ascending=False)
top_salaries = top_salaries[['Player', 'Yearly Salary', 'Pos', 'Age', 'Min', 'Team']]
top_salaries = top_salaries.reset_index()
del top_salaries['index']
top12_salaries = top_salaries.head(30)
by_team = salaries.groupby('Team')
team_means = by_team[['Yearly Salary']].aggregate("mean").sort_values(by='Yearly Salary', ascending=False).round()
salaries_GA = salaries[['Player', 'Weekly Wage', 'Yearly Salary', 'Pos', 'Min', 'Gls', 'PK', 'Ast', 'G+A', 'xG','xG_90', 'xAG', 'xAG_90', 'xG+xAG_90', 'Team']]
salaries_xG = salaries_GA['xG']
salaries_xAG = salaries_GA['xAG']
salaries_xG_xAG = salaries_xG + salaries_xAG
salaries_GA['xG + xAG'] = salaries_xG_xAG
salaries_GA['Gls - XG'] = salaries['Gls'] - salaries['xG']
salaries_GA['Ast - XAG'] = salaries_GA['Ast'] - salaries_GA['xAG']
salaries_good_finishers = salaries_GA.sort_values('Gls - XG', ascending = False).head(10)
salaries_good_assisters = salaries_GA.sort_values('Ast - XAG', ascending = False).head(10)
salaries_bad_finishers = salaries_GA.sort_values('Gls - XG', ascending = True).head(10)
salaries_bad_assisters = salaries_GA.sort_values('Ast - XAG', ascending = True).head(10)
attacking = (salaries_GA['Pos'] == 'MF,FW') | (salaries_GA['Pos'] == 'FW,MF') | (salaries_GA['Pos'] == 'FW')
attacking_only = salaries_GA[attacking]
# Good finishing and assists combined
attacking_only['(Gls - XG) + xAG'] = (attacking_only['Gls - XG']) + (attacking_only['xAG'])
import plotly.graph_objects as go

salary_attacking_only_sorted = attacking_only.sort_values('Gls - XG', ascending = False)
salary_attacking_only_sorted = salary_attacking_only_sorted[['Player', 'Yearly Salary', 'Gls', 'Gls - XG', '(Gls - XG) + xAG']]

salary_attacking_only_sorted = salary_attacking_only_sorted[['Player',  'Yearly Salary', 'Gls','Gls - XG', '(Gls - XG) + xAG']].copy()

# Add 'Rank' column based on 'Gls - XG' column
salary_attacking_only_sorted.loc[:, 'Finisher Rank'] = salary_attacking_only_sorted['Gls - XG'].rank(method='min', ascending=False).astype(int)
salary_attacking_only_sorted.loc[:, 'overperform finishing + assists Rank'] = salary_attacking_only_sorted['(Gls - XG) + xAG'].rank(method='min', ascending=False).astype(int)
salary_attacking_only_sorted.loc[:, 'Wage Rank (out of 154 attackers)'] = salary_attacking_only_sorted['Yearly Salary'].rank(method='min', ascending=False).astype(int)
salary_attacking_only_sorted = salary_attacking_only_sorted.reset_index()
del salary_attacking_only_sorted['index']
salary_attacking_only_sortedtop10 = salary_attacking_only_sorted.head(10) 

regular_players_GA_ass_90 = regular_players_GA.sort_values(by='xAG_90', ascending=False)
regular_players_GA_ass_90 = regular_players_GA_ass_90[['Player', 'Pos', 'Min', 'Gls', 'Ast', 'xAG', 'xAG_90', 'Team']]
top_regular_players_GA_ass_90 = regular_players_GA_ass_90.reset_index()
del top_regular_players_GA_ass_90['index']
top_regular_players_GA_ass_90 = top_regular_players_GA_ass_90.head(30)



def MidProgressiveness(player):
   # player = input("Enter the player's name: ")
    players = pd.read_csv('premier-player-23-24.csv')
    progressive = players.copy()
    progressive = progressive[['Player', 'Pos', 'Min', 'PrgC', 'PrgP', 'PrgR']]
    progressive['Progressiveness'] = progressive['PrgC'] + progressive['PrgP'] + progressive['PrgR']
    progressive['Progressiveness per 90'] = (progressive['Progressiveness'] / progressive['Min']) * 90
    progressive_mid = (progressive['Pos'] == 'MF') & (progressive['Min'] > 300)
    progressive_mid_only = progressive[progressive_mid] 
    
    fig,ax = plt.subplots(1,1)
    ax = progressive_mid_only['Progressiveness per 90'].plot(kind='hist', fontsize=14, color='#00ABC8', bins=20)
    plt.xlabel('Progressiveness per 90mins', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    player_progressiveness = progressive_mid_only.loc[progressive_mid_only['Player'] == player, 'Progressiveness per 90']
    if player_progressiveness.empty:
        print("Please enter a player's full name in quotes e.g. 'Declan Rice'")
        return  # Exit the function if the player is not found
    
    plt.plot(player_progressiveness, 2 , 'o', markersize = 10,color = 'red', label = f'{player} Progressiveness' )
    plt.title(f' {player} Progressiveness (Midfielders only)'  ,y=1.05, fontsize=14)
    ax.legend(loc='upper right', fontsize=12)
    return st.pyplot(fig)


def DefProgressiveness(player):
   # player = input("Enter the player's name: ")
    players = pd.read_csv('premier-player-23-24.csv')
    progressive = players.copy()
    progressive = progressive[['Player', 'Pos', 'Min', 'PrgC', 'PrgP', 'PrgR']]
    progressive['Progressiveness'] = progressive['PrgC'] + progressive['PrgP'] + progressive['PrgR']
    progressive['Progressiveness per 90'] = (progressive['Progressiveness'] / progressive['Min']) * 90
    progressive_def = (progressive['Pos'] == 'DF') & (progressive['Min'] > 300)
    progressive_def_only = progressive[progressive_def] 
    
    fig,ax = plt.subplots(1,1)
    ax = progressive_def_only['Progressiveness per 90'].plot(kind='hist', fontsize=14, color='#00ABC8', bins=20)
    plt.xlabel('Progressiveness per 90mins', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    player_progressiveness = progressive_def_only.loc[progressive_def_only['Player'] == player, 'Progressiveness per 90']
    if player_progressiveness.empty:
        print("Please enter a player's full name in quotes e.g. 'Andrew Robertson'")
        return  # Exit the function if the player is not found
    
    plt.plot(player_progressiveness, 2 , 'o', markersize = 10,color = 'red', label = f'{player} Progressiveness' )
    plt.title(f' {player} Progressiveness (Defenders only)'  ,y=1.05, fontsize=14)
    ax.legend(loc='upper right', fontsize=12)
    return st.pyplot(fig)


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
    'Gls = Goals | xG = Expected Goals | xG_90 = Expected goals per 90minutes'
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
    'Gls = Goals | xG = Expected Goals | xG_90 = Expected goals per 90minutes'
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
     st.markdown('## These are the players with more assists than expected (overperform x_AG)')
     'Ast = Assists | xAG = Expected Assists | xAG_90 = Expected assists per 90minutes'
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
     'These players got more assists than expected' 
     ' Their stats look better due to good finishing from their teammate '
     ' '
     st.markdown('## These are the top assisters (Highest expected assits per 90 minutes)')
     top_regular_players_GA_ass_90
     


  elif Attacking_output == 'Unlucky assisters':
     'These are the Unlucky assisters - They should have had more assists from the chances they created'
     'Ast = Assists | xAG = Expected Assists | xAG_90 = Expected assists per 90minutes'
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
     'Gls = Goals | PK = Penalties scored | Ast = Assists | G+A = Goals+Assists | xG = Expected goals | xG_90 = Expected goals per 90 minutes | xAG = Expected Assists | xAG_90 = Expected assists per 90minutes | Gls - XG = Goals scored above expected (indication of good finishing) | Ast - XAG = Assits above expected (indication of teammate finishing of your chances created)'
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
     'Gls = Goals | PK = Penalties scored | Ast = Assists | G+A = Goals+Assists | xG = Expected goals | xG_90 = Expected goals per 90 minutes | xAG = Expected Assists | xAG_90 = Expected assists per 90minutes | Gls - XG = Goals scored above expected (indication of good finishing) | Ast - XAG = Assits above expected (indication of teammate finishing of your chances created)' 
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
     'These players should have had more assists'
     'Their teammates did not score chances they would be expected to from these players chances created'

elif choose_option == 'Progressiveness':
  Progressiveness = st.sidebar.selectbox(
    'Choose a Position',
    ['Progressiveness','Progressive Midfielders','Progressive Defenders'])
  if Progressiveness == 'Progressiveness':
    'Please choose a visualisation you wish to see'
  elif Progressiveness == 'Progressive Midfielders':
     Midfielders = st.sidebar.selectbox(
        'Choose a Progressive analysis option',
        ['Top Progressive Midfielders','Least Progressive Midfielders','Progressive Midfielder comparisons', 'Top Progressive Midfielders OUTSIDE top 6','Least Progressive Midfielders IN top 6', 'Top Young progressive midfielders', 'Top Young progressive midfielders OUTSIDE top 6'])
     if Midfielders == 'Top Progressive Midfielders':
        'These are the top progressive midfielders - Progressive carries, passes and runs per 90minutes'
        top_progressive_mid
        # Create a figure with two subplots side by side
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

        # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for good finishers on the first subplot (axes[0])
        axes.bar(top_progressive_mid['Player'], top_progressive_mid['Progressiveness per 90'], color=colors)
        axes.set_title('Top progressive Midfielders', pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)
        axes.set_ylabel('Progressiveness per 90 mins')

        # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

      

     elif Midfielders == 'Least Progressive Midfielders':
        'These are the least progressive midfielders - Progressive carries, passes and runs per 90minutes'
        worse_progressive_mid
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

        # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        axes.set_ylabel('Progressiveness per 90mins')

         # Plot data for bad finishers on the second subplot (axes[1])
        axes.bar(worse_progressive_mid['Player'], worse_progressive_mid['Progressiveness per 90'], color=colors2)
        axes.set_title('Least progressive midfielders', pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)

         # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)



     elif Midfielders == 'Progressive Midfielder comparisons':
        enter_player = st.sidebar.text_input("Enter a player e.g., Declan Rice - see full midfield player list (right)")
        try:
         st.header('Midfielder Progressiveness compared to other midfielders')
         progressive_mid_only['Player']
         MidProgressiveness(enter_player)
        except Exception as e:
         st.write("Enter a full  player name e.g, Kevin De Bruyne ")
         print(e)  


     elif Midfielders == 'Top Progressive Midfielders OUTSIDE top 6':
        " These are the top progressive midfielsers outside the traditional 'top 6'"
        'Progressiveness per 90 = Progressive Carries, passes and runs per 90 minutes'
        top_outsideTop6_Progmid
        # Create a figure with two subplots side by side
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

         # Plot data for good finishers on the first subplot (axes[0])
        axes.bar(top_outsideTop6_Progmid['Player'], top_outsideTop6_Progmid['Progressiveness per 90'], color=colors)
        axes.set_title('Top progressive Midfielders OUTSIDE top 6', pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)
        axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)


     elif Midfielders == 'Least Progressive Midfielders IN top 6':
        " These are the least progressive midfielsers in the traditional 'top 6'" 
        'Progressiveness per 90 = Progressive Carries, passes and runs per 90 minutes' 
        worse_top6_progmid
        # Create a figure with two subplots side by side
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
        axes.bar(worse_top6_progmid['Player'], worse_top6_progmid['Progressiveness per 90'], color=colors2)
        axes.set_title('Least progressive midfielders IN Top 6', pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)
        axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

     elif Midfielders == 'Top Young progressive midfielders OUTSIDE top 6':
        " These are the most progressive young midfielsers (under 24) outside the traditional 'top 6'"  
        'Progressiveness per 90 = Progressive Carries, passes and runs per 90 minutes'
        Top_young_progressive_midfielder_outsideTop6
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
        axes.bar(Top_young_progressive_midfielder_outsideTop6['Player'], Top_young_progressive_midfielder_outsideTop6['Progressiveness per 90'], color=colors)
        axes.set_title("Most progressive young midfielders outside 'Top 6'", pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)
        axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)


     else:
        'These the the top young progressive midfielders (under 24)'  
        'Progressiveness per 90 = Progressive Carries, passes and runs per 90 minutes'
        Top12_young_progressive_midfield = Top_young_progressive_midfield.head(12)
        Top12_young_progressive_midfield
        fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
        colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
        colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
        axes.bar(Top12_young_progressive_midfield['Player'], Top12_young_progressive_midfield['Progressiveness per 90'], color=colors)
        axes.set_title("Most progressive young midfielders ", pad=30)
        axes.tick_params(axis='x', rotation=90)
        axes.set_xlabel('Player', labelpad=20)
        axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

        st.markdown('<p style="color: red;"> In the 2024-25 season gravenberch and Smith Rowe have both excelled and became one of the most influential players for their teams</p>', unsafe_allow_html=True)




    
  elif Progressiveness == 'Progressive Defenders':
    Defenders = st.sidebar.selectbox(
      'Choose a Progressive analysis option',
      ['Top Progressive Defenders', 'Top Progressive Defenders OUTSIDE top 6', 'Defender Progressiveness comparison', 'Top Young progressive defenders', 'Top Young progressive defenders OUTSIDE top 6'])
    if Defenders == 'Top Progressive Defenders':
       'These are the top progressive defenders'
       'Pos = Position | Min = Minutes Played | PrgC = progressive carries | PrgP = progressive passes | PrgR = progressive runs | Progressiveness = PrgC + PrgP + PrgR | Progressiveness per 90 = progressive carries, passes and runs per 90 minutes'
       Top12_progressive_def
       fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
       colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
       colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
       axes.bar(Top12_progressive_def['Player'], Top12_progressive_def['Progressiveness per 90'], color=colors)
       axes.set_title('Most progressive Defenders per 90', pad=30)
       axes.tick_params(axis='x', rotation=90)
       axes.set_xlabel('Player', labelpad=20)
       axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
       plt.tight_layout()
       plt.show()
       st.pyplot(fig)




    
    elif Defenders == 'Top Progressive Defenders OUTSIDE top 6':
       " These are the top progressive defenders outside the traditional 'top 6'"
       'Pos = Position | Min = Minutes Played | PrgC = progressive carries | PrgP = progressive passes | PrgR = progressive runs | Progressiveness = PrgC + PrgP + PrgR | Progressiveness per 90 = progressive carries, passes and runs per 90 minutes'
       Top12_progressive_Defenders_outsideTop6
       fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
       colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
       colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
       axes.bar(Top12_progressive_Defenders_outsideTop6['Player'], Top12_progressive_Defenders_outsideTop6['Progressiveness per 90'], color=colors)
       axes.set_title("Most progressive Defenders per 90 - outside 'top 6'", pad=30)
       axes.tick_params(axis='x', rotation=90)
       axes.set_xlabel('Player', labelpad=20)
       axes.set_ylabel('Progressiveness per 90')

        # Adjust layout to make room for rotated labels
       plt.tight_layout()
       plt.show()
       st.pyplot(fig)



    
    elif Defenders == 'Top Young progressive defenders':
       'These are the top young progressive defenders (under 24)'
       'Pos = Position | Min = Minutes Played | PrgC = progressive carries | PrgP = progressive passes | PrgR = progressive runs | Progressiveness = PrgC + PrgP + PrgR | Progressiveness per 90 = progressive carries, passes and runs per 90 minutes'
       Top12_young_progressive_defender
       fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
       colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
       colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
       axes.bar(Top12_young_progressive_defender['Player'], Top12_young_progressive_defender['Progressiveness per 90'], color=colors)
       axes.set_title("Most progressive Young defenders Defenders per 90mins", pad=30)
       axes.tick_params(axis='x', rotation=90)
       axes.set_xlabel('Player', labelpad=20)
       axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
       plt.tight_layout()
       plt.show()
       st.pyplot(fig)

       
    elif Defenders == 'Top Young progressive defenders OUTSIDE top 6':
       " These are the top progressive young defenders outside the traditional 'top 6'" 
       'Pos = Position | Min = Minutes Played | PrgC = progressive carries | PrgP = progressive passes | PrgR = progressive runs | Progressiveness = PrgC + PrgP + PrgR | Progressiveness per 90 = progressive carries, passes and runs per 90 minutes' 
       Top12_young_progressive_defender_outsideTop6

       fig, axes = plt.subplots(1, 1, figsize=(9, 7))

         # Create a color map (adjust np.linspace to match the number of bars)
       colors = plt.cm.Greens(np.linspace(0.5, 9, len(progressive_mid_only['Player'])))
       colors2 = plt.cm.Reds(np.linspace(0.5, 6, len(progressive_mid_only['Player'])))

        # Plot data for bad finishers on the second subplot (axes[1])
       axes.bar(Top12_young_progressive_defender_outsideTop6['Player'], Top12_young_progressive_defender_outsideTop6['Progressiveness per 90'], color=colors)
       axes.set_title("Most progressive Young defenders Defenders outside 'top 6' ", pad=30)
       axes.tick_params(axis='x', rotation=90)
       axes.set_xlabel('Player', labelpad=20)
       axes.set_ylabel('Progressiveness per 90mins')

        # Adjust layout to make room for rotated labels
       plt.tight_layout()
       plt.show()
       st.pyplot(fig)

    elif Defenders == 'Defender Progressiveness comparison':
        enter_player = st.sidebar.text_input("Enter a player e.g., Neco Williams - see full Defender player list (right)")
        try:
         st.header('Defender Progressiveness compared to other Defenders')
         progressive_def_only['Player']
         DefProgressiveness(enter_player)
        except Exception as e:
         st.write("Enter a full  player name e.g, Andrew Robertson ")
         print(e)  
         


  


elif choose_option == 'Salaries':
    Salaries = st.sidebar.selectbox(
    'Choose a Salary analysis option',
    ['Salaries','Top Salaries', 'Top Team Average salaries', 'Salary compared to G+A', 'Salary compared to finishing', 'salary compared to finishing + assists', 'salary compared to progressiveness (midfielders)'])
    if Salaries == 'Salaries':
       'Please choose an analysis you wish to see'
    elif Salaries == 'Top Salaries':
        'These are the top salaries'
        top12_salaries
        


    elif Salaries == 'Top Team Average salaries':
        'These are the teams with the highest average yearly salaries'
        team_means



    elif Salaries == 'Salary compared to G+A':
       
  
      fig = go.Figure()

# Add the scatter trace with hovertext
      fig.add_trace(go.Scatter(
      x=attacking_only['Yearly Salary'],  # x-axis
      y=attacking_only['G+A'],  # y-axis
      mode='markers',  # Points
      marker=dict(
        size=12,  # Point size
        color='#cb1dd1',  # Point color
        opacity=0.8,  # Transparency
        line=dict(width=1, color='black')  # Edge properties
    ),
      text=attacking_only['Player'],  # Player name for hovertext
      customdata=attacking_only['Min'],  # Adding Minutes Played as custom data
      hovertemplate=
      '<b>%{text}</b><br><br>' +  # Player name
      'Yearly Salary: %{x}<br>' +  # Show yearly salary
      'Goals + Assists: %{y}<br>' +  # Show G+A
      'Minutes Played: %{customdata}<extra></extra>'  # Show Minutes Played from customdata
   ))

   # Customize the layout
      fig.update_layout(
      title='Attacking Players only: Yearly Salary and Goals+Assists',  # Title
      xaxis_title='Yearly Salary',  # x-axis label
      yaxis_title='Goals + Assists',  # y-axis label
      width=1000,  # Width
      height=800  # Height
   )

      st.plotly_chart(fig)  # Display the plotly chart


    elif Salaries == 'Salary compared to finishing':
       'Salaries compared to finishing level (overachive xG)'
       'High Gls - XG = good finishing - score more than expected from the quality of chances they got'
       salary_attacking_only_sortedtop10 = salary_attacking_only_sortedtop10[['Player', 'Yearly Salary', 'Gls', 'Gls - XG', 'Finisher Rank', 'Wage Rank (out of 154 attackers)']]
       salary_attacking_only_sortedtop10

       st.markdown('#### None of the top 10 finishers are even in the top 10 of wages')
       st.markdown('### All these players would have a case to ask for an improved contract - especially; Adebayo, Mateta and Hee chan')

       salary_attacking_only_sorted_wages = salary_attacking_only_sorted.sort_values(by='Wage Rank (out of 154 attackers)').head(15)
       salary_attacking_only_sorted_wages = salary_attacking_only_sorted_wages[['Player', 'Yearly Salary', 'Gls', 'Gls - XG', 'Finisher Rank', 'Wage Rank (out of 154 attackers)']]
       salary_attacking_only_sorted_wages

       st.markdown('#### Can see that the top Wages for attackers are not the best finishers or the best finishers + expected assists.')
       st.markdown('### Sancho, Martial, Mount and Fati especially are on extremely high wages for their output.')
       st.markdown('##### Perhaps Surprisingly, Haaland and Salah are very near the bottom of the finishers list - they both should have scored more goals according to their xG (expected goals).')
  

     

    elif Salaries == 'salary compared to finishing + assists':
       'Salaries compared to finishing level (overachive xG) and expected assists'
       st.markdown('### Only using finishing is unfair on attacking players that are not out and out forwards.')
       st.markdown('### Here we use (Gls - XG) + xAG. This is a combination of good finishing (Gls - XG) plus expected assists.')
       st.markdown('### We use expected assists over actual assists as actual assists can be distorted due to good / poor finishing')

       salary_attacking_only_sorted_att = salary_attacking_only_sorted.sort_values(by='(Gls - XG) + xAG', ascending=False).head(15)
       salary_attacking_only_sorted_att[['Player', 'Yearly Salary', 'Gls - XG', '(Gls - XG) + xAG', 'overperform finishing + assists Rank', 'Wage Rank (out of 154 attackers)']]
       
       st.markdown('#### Looking at good finishing plus expected assists together Palmer, Bailey, Olise, Gordon, McNeil and Mateta all have a strong case to get a higher wage.')
      
       st.markdown('<p style="color: red;">Interestingly - in the 2024 season Palmer got a big 9 year contract and Olise got a big move to Bayern Munich</p>', unsafe_allow_html=True)
       

       
       



    elif Salaries == 'salary compared to progressiveness (midfielders)':
       'Midfielders salaries compared to their progressiveness rank '   
       'Progressiveness per 90 = progressive carries, passes and runs per 90 minutes'

       salaries_progressive = salaries.copy()
       salaries_progressive = salaries_progressive[['Player', 'Yearly Salary', 'Pos','Age', 'Min', 'PrgC', 'PrgP', 'PrgR', 'Team']]      
       salaries_progressive['Progressiveness'] = salaries_progressive['PrgC'] + salaries_progressive['PrgP'] + salaries_progressive['PrgR']
       salaries_progressive['Progressiveness per 90'] = (salaries_progressive['Progressiveness'] / salaries_progressive['Min']) * 90
       salaries_progressive_mid = (salaries_progressive['Pos'] == 'MF') & (salaries_progressive['Min'] > 300)
       salaries_progressive_mid_only = salaries_progressive[salaries_progressive_mid] 
       salaries_top_progressive_mid = salaries_progressive_mid_only.sort_values('Progressiveness per 90', ascending = False)
       salaries_top_progressive_mid.loc[:, 'Wage Rank (out of 73)'] = salaries_top_progressive_mid['Yearly Salary'].rank(method='min', ascending=False).astype(int)
       salaries_top_progressive_mid.loc[:, 'Midfield Progressive rank'] = salaries_top_progressive_mid['Progressiveness per 90'].rank(method='min', ascending=False).astype(int)
       top_progressive_mid_salaries = salaries_top_progressive_mid.sort_values('Progressiveness per 90', ascending = False).head(12)
       top_progressive_mid_salaries[['Player', 'Yearly Salary', 'Age', 'Team', 'Progressiveness per 90', 'Wage Rank (out of 73)', 'Midfield Progressive rank']]

       st.markdown('### The top progressive midfielders do have some of the highest midfield salaries eg De Bruyne, Odegaard, Maddison, Rodri, Enzo, Gravenberch are all in the top 10 wages as well as top 12 progressiveness')
       st.markdown('<p style="color: red;">In the 2024-25 Season: <br>Lo Celso has started very well for Real Betis scoring 3 in 3 games <br> <br> Gravenberch has been one of the standout players in the premier league <br> <br> Smith Rowe has been one of Fulhams best players </p>', unsafe_allow_html=True)
       
 

        
else:
   'Please Choose an Option'


