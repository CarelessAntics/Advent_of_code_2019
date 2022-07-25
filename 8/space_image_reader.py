#w: 25px, h: 6px
def createLayers(data, w, h):
	layers = []
	layerAmount = int(len(data)/(w*h))
	for z in range(layerAmount):
		yList = []
		for y in range(h):
			yList.append([int(x) for x in data[(z*h*w)+y*w : (z*h*w)+y*w+w]])
		layers.append(yList)

	return layers

def assignmentOne(layerData):
	layerZeroes = []
	layerOnes = []
	layerTwos = []
	for l in range(len(layerData)):
		layerZeroes.append(0)
		layerOnes.append(0)
		layerTwos.append(0)
		for y in layerData[l]:
			layerZeroes[l] += y.count(0)
			layerOnes[l] += y.count(1)
			layerTwos[l] += y.count(2)
	z = layerZeroes.index(min(layerZeroes))
	return layerOnes[z] * layerTwos[z]

def createImg(layerData):
	w = len(layerData[0][0])
	h = len(layerData[0])
	image = [[0 for x in range(w)] for y in range(h)]

	for l in reversed(layerData):
		iy = 0
		for y in l:
			ix = 0
			for x in y:
				if x != 2:
					image[iy][ix] = x	
				ix += 1
			iy += 1
	return image

def render(image):
	for y in image:
		for x in range(len(y)):
			if y[x] == 0:
				y[x] = ' '
			else y[x] == 1:
				y[x] = '#'
		print(''.join([str(e) for e in y]))
	return

def main():
	f = open("aoc_input_8_1.txt", "r")
	imageData = f.read()
	layers = createLayers(imageData, 25, 6)
	image = createImg(layers)
	render(image)

main()