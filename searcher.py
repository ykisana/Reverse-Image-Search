import numpy as np
import csv


class Searcher:
    def __init__(self, index_path):
        # store index path
        self.index_path = index_path

    def search(self, query_features, limit=10):
        # dictionary of results
        # limit is maximum number of results returned
        results = {}

        # open index file
        with open(self.index_path) as file:
            # csv reader initialization
            reader = csv.reader(file)

            # loop over rows of index
            for row in reader:
                # parse out image ID and features
                # compute chi-squared distance between images
                features = [float(x) for x in row[1:]]
                distance = self.chisq_distance(features, query_features)

                # update results in dictionary
                results[row[0]] = distance

            # close reader
            file.close()

        # sort results by distance
        results = sorted((v, k) for (k, v) in results.items())

        # return results (sorted and limited)
        return results[:limit]

    def chisq_distance(self, hist_a, hist_b, eps=1e-10):
        # compute chi-squared distance
        distance = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                                 for (a, b) in zip(hist_a, hist_b)])

        return distance
