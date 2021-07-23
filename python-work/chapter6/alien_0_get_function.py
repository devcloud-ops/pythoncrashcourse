alien_0 = {'color': 'green', 'speed': 'slow'}
#alien_0 = {'color2': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')

point_value2 = alien_0.get('color', 'color is not specified')

print(point_value)
print(point_value2)