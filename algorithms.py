BEGIN search
    INPUT Artist as artist_name
    THEN userSearch = artist_name
    GET 'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    OUTPUT arists['userSearch']


#BEGIN Search
    #INPUT Artist AS artist_name OR artist_name = INPUT Artist
    artist_name = requests.form['artist']
    #VAR url = 'https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s={artist_name}'
    URL = f'https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s={artist_name}'
    #VAR response = GET artist_data from url
    response = requests.get(URL)
    #VAR data = format response
    data = response.json()
    #DISPLAY data AS results.html
    return render_template('results.html', artist=artist_name, albums=albums)
#END Search