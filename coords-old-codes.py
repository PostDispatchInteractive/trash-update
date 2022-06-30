import shapely
from shapely.geometry import shape, mapping, Polygon, Point, MultiPolygon
import shapefile
import csv
from csv import DictReader

def name_for_containing_geography(coord,sf):
	p = Point(coord)
	shp = shapefile.Reader(sf)
	all_shapes = shp.shapes()
	all_records = shp.records()
	for boundary, record in zip(all_shapes, all_records):
		if p.within(shape(boundary)):
			if p.within(shape(boundary)):
				if record[0] != "0":
					return record[0]
	else:
		return "NA"


# this is for finding parks, if we're using the combined neighborhood-park shapefile

			# if record[15] != "0":
				# return record[15]
			# else:
				# return record[8]

def parse_coord(coord_string):
	return tuple(map(float, coord_string.split(', ')))

def neighborhoods(data,sf):

	with open(data) as infile:
		with open('csb-1112-62722-combined-cleaned-nhoods-old-codes.csv','w') as outfile:
			reader = csv.reader(infile)
			writer = csv.writer(outfile)
			header = next(reader)
			header.append('nhood')
			writer.writerow(header)
			for row in reader:
				coord = parse_coord(row[23])
				row.append(name_for_containing_geography(coord, sf))
				writer.writerow(row)

	print("done")

neighborhoods('csb-1112-62722-combined-coords-old-codes.csv', 'hoods.shp')