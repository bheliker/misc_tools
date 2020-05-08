def plotGPXfile(filepath):
    import folium, gpxpy

    tableau20_rgb = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
    tableau20_hex = []
    for i in range(len(tableau20_rgb)):    
        tableau20_hex.append('#%02x%02x%02x' % (tableau20_rgb[i])) 

    attr = ('Tiles &copy;')
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}'

    m = folium.Map(location=[0,0], tiles=tiles, attr=attr, zoom_start=10)

    with open(filepath,'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

        points = []
        for idx, track in enumerate(gpx.tracks):
            for segment in track.segments:        
                segment_points = []
                for point in segment.points:
                    segment_points.append(tuple([point.latitude, point.longitude]))
                points.extend(segment_points)
                line = folium.PolyLine(segment_points, color=tableau20_hex[idx%20], weight=3, opacity=1,tooltip=track.name).add_to(m)

    m.fit_bounds([[min(p[0] for p in points), min(p[1] for p in points)], [max(p[0] for p in points), max(p[1] for p in points)]])

    return m