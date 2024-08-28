from django.shortcuts import render
from home import models
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
# Create your views here.

def home(request):
    projects = models.Project.objects.order_by('rank', 'name')
    categories = models.Category.objects.order_by('rank', 'name')
    skill_categories = models.SkillCategory.objects.order_by('rank', 'name')
    skills = models.Skill.objects.order_by('-level', )

    # Prepare data for plots
    skill_plots_with_categories = []
    for category in skill_categories:
        category_skills = models.Skill.objects.filter(category=category).order_by('name')
        if category_skills:
            df = pd.DataFrame(list(category_skills.values('name', 'level')), columns=['name', 'level']).sort_values(['level', 'name'])
            
            if df['level'].max() > 5:
                df['level'] = df['level'].apply(lambda x: int(x / 20))
            
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=df['level'].tolist() + [df['level'].iloc[0]],  # Add first value to end of list
                theta=df['name'].tolist() + [df['name'].iloc[0]],  # Add first name to end of list
                mode='lines+markers',  # Explicitly set mode to lines and markers
                fill='toself',
                fillcolor='rgba(0, 124, 189, 0.2)',  # #007cbd with 20% opacity
                line=dict(color='#007cbd', width=2),
                marker=dict(
                    color='#003554',
                    size=8,
                    line=dict(
                        color='#007cbd',
                        width=2
                    )
                )
            ))
            fig.update_layout(
                coloraxis_showscale=False,
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5],
                        showline=False,
                        showgrid=True,
                        gridcolor='lightgrey',
                        tickfont=dict(size=12),
                    ),
                    angularaxis=dict(
                        showline=False,
                        showgrid=True,
                        gridcolor='lightgrey',
                        tickfont=dict(size=12),  # Increased font size for skill names
                        tickangle=0,  
                    ),
                ),
                showlegend=False,
                margin=dict(l=100, r=100, t=80, b=80),  # Increased margins
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                autosize=True,  # Allow the plot to be responsive
            )

            radar_html = fig.to_html(
                full_html=False,
                include_plotlyjs=False,
                config={
                    'responsive': True,
                    'displayModeBar': False,
                    'staticPlot': False,
                }
            )

            skill_plots_with_categories.append({
                'radar_plot': radar_html,
                'category': category
            })

    context = {
        'projects': projects,
        'categories': categories,
        'skill_categories': skill_categories,
        'skills': skills,
        'skill_plots_with_categories': skill_plots_with_categories
    }

    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')
