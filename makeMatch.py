import pandas
def imageName(df, index):
    index = index[0]
    return df.at[index,'image_location']
def chooseMatch(data):
    #data = [likelihood_name[face.anger_likelihood], likelihood_name[face.joy_likelihood], likelihood_name[face.surprise_likelihood], likelihood_name[face.sorrow_likelihood]]
    df = pandas.read_csv('./data.csv',encoding="utf-8-sig")
    df2 = df[((df['anger']==data[0]) & (df['joy']==data[1])) & ((df['surprise']==data[2]) & (df['sorrow']==data[3]))]
    if(not df2.empty):
        return imageName(df,df.index[((df['anger']==data[0]) & (df['joy']==data[1])) & ((df['surprise']==data[2]) & (df['sorrow']==data[3]))])
    df2 = df[((df['joy']==data[1]) & ((df['surprise']==data[2]) & (df['sorrow']==data[3])))]
    if(not df2.empty):
        return imageName(df,df.index[((df['joy']==data[1]) & ((df['surprise']==data[2]) & (df['sorrow']==data[3])))])
    df2 = df[df['sorrow']==data[3]]
    if(not df2.empty):
        return imageName(df,df.index[(df['sorrow']==data[3])])
