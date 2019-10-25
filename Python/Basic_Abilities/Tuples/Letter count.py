#Lab 7
#Exercise 1
#October 30th, 2018
#Aiden Stevenson Bradwell

def histogram(string):
      histograms = {}
      for c in string:
            histograms[c] = histograms.get(c,0) + 1
      return histograms



string = input("Please enter a sentence:   ")
histograms = histogram(string)
sorted_histogram = list(histograms.items())
sorted_histogram.sort()
print(sorted_histogram)
