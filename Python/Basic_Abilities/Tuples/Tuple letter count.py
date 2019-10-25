#Lab 7
#Exercise 2
#October 30th, 2018
#Aiden Stevenson Bradwell




def histogram_create(tuplestring):
      histograms = {}
      for c in tuplestring:
            histograms[c] = histograms.get(c,0) + 1
      return histograms



spaces = input("Please enter a tuple, seperating each value with a commas:    ")
spaces = spaces.replace(',', ' ')
spaces = spaces.strip().split()
spaces = tuple(spaces)
histograms = histogram_create(spaces)
sorted_histogram = list(histograms.items())
sorted_histogram.sort()
print(sorted_histogram)
