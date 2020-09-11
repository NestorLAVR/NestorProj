import matplotlib
matplotlib.use('Agg')   
import json
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import io
import urllib, base64


def VisualizeData(firstparametr ,secondparametr, visual, agregation):
    df = pd.DataFrame(columns=['Segment', 'Values'])

    headers = {
        'x-api-key': 'n7sxzihgdlkp0axb6676c88niug43b10gr1xqilr',
    }

    params = (
        ('segment', secondparametr),
    )
    responsetext =  'https://api.applicationinsights.io/v1/apps/4ef874d8-f7e4-4672-89e3-ac7ad678c238/metrics/' + firstparametr
    response = requests.get(
        responsetext,
        headers=headers, params=params) #получение данных по URL

    mydata = json.loads(response.text) #сохранение ответа на запрос

    mvalues = mydata["value"]
    msegments = mvalues["segments"] #сегменты запроса

    for msegment in msegments:
        if len(msegment[secondparametr])>12:
            msegment[secondparametr]=msegment[secondparametr][0:10] + ".."
        df.loc[len(df)] = [msegment[secondparametr], msegment[firstparametr][agregation]] #запись данных в датафрейм
    if visual == 'bars':
        ypos = np.arange(len(df['Segment'])) #создание численного массива для гистобар
        plt.rc('xtick', labelsize=5)
        plt.rc('ytick', labelsize=6)
        plt.xticks(ypos, df['Segment']) #привязка городов к значениям численного массива

        plt.bar(ypos, df['Values'], color='#4B0082')
    elif visual == 'pie':
        plt.pie(df['Values'], labels=df['Segment'])

    fig = plt.gcf()     #передача графика в фигуру
    # convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', )
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.clf()
    return uri