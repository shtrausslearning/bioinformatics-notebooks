''' FUNCTIONS FOR PLOTTING KERAS HISTORY RESULTS '''
# function to plot keras history using plotly
# change metric_id to anything that was used in training
# plots training & validation curves as well as the difference b/w them

# Function to plot all metrics side by side (defined above)
def plot_keras_metric(history,title_id):

    # Palettes
    lst_color = ['#F55AA2','#323232','#004379','#032B52']
    metric_id = ['loss','auc'] # change your metrics to plot here
    fig = make_subplots(rows=1, cols=len(metric_id),subplot_titles=metric_id)

    jj=0;
    for metric in metric_id:     

        jj+=1
        fig.add_trace(go.Scatter(x=[i for i in range(1,cfg.n_epochs+1)],
                                 y=history.history[metric],
                                 name=f'train_{metric}',
                                 line=dict(color=lst_color[0]),mode='lines'),
                      row=1,col=jj)
        
        fig.add_trace(go.Scatter(x=[i for i in range(1,cfg.n_epochs+1)],
                                 y=history.history['val_'+metric],
                                 name=f'val_{metric}',
                                 line=dict(color=lst_color[1]),mode='lines'),
                      row=1,col=jj)

        # difference between training/validation metrics
        if(metric is not 'loss'):
            diff = abs(np.array(history.history[metric]) \
                       - np.array(history.history['val_'+metric]))
            fig.add_trace(go.Bar(x=[i for i in range(1,cfg.n_epochs+1)],
                                 y=diff,name='metric diff.',
                                 marker_color=lst_color[3],
                                 opacity=0.15,showlegend=False)
                          ,row=1,col=jj)

    # Plot Aesthetics
    fig.update_layout(yaxis=dict(range=[0,1]),yaxis_range=[0,1],margin=dict(b=10),
                      height=400,showlegend=False,template='plotly_white',
                      font=dict(family='sans-serif',size=14),
                      hovermode="x",title=f'<b>Training History</b> | {title_id}')
    
    fig['layout']['yaxis'].update(title='', range=[0,5], autorange=True,type='log')
    fig['layout']['yaxis2'].update(title='', range=[0, 1.1], autorange=False)    
    fig.show()
