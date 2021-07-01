import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    links = corpus[page]
    distribution = dict()

    # Initialize dict with random_choice probability for all pages.
    random_choice = (1 - damping_factor) / len(corpus)
    for page in corpus:
        distribution[page] = random_choice 

    # If current page has links, add probability to leading pages.
    if len(links) != 0:
        for link in links:
            distribution[link] += damping_factor / len(links)         

    return distribution



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    distribution = dict()

    # Initialize each key with 0
    for page in corpus:
        distribution[page] = 0
    
    # Initialize sampling in random page
    sample = random.choice(list(distribution.keys()))
  
    for _ in range(n):
        
        # Count how many times a page is visited (starting with the current one)
        distribution[sample] +=  1
        
        # Call transition model
        model = transition_model(corpus, sample, damping_factor)
        pages = list(model.keys())
        probabilities = list(model.values())

        # Get the next page based on the probabilities of visiting it
        sample = random.choices(pages, probabilities)[0]

    # Measure the distribution based on how many times the different pages where visited
    for page in distribution:
        distribution[page] = distribution[page] / n
    
    #SUM
    total = 0
    for page in distribution:
        total += distribution[page]

    print("SAMPLING ==>",total)

    return distribution




def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    distribution = dict()

    # Initialize each key with 1 / N. Where N is the total pages in corpus
    for page in corpus:
        distribution[page] = 1 / len(corpus)

    # Set de desired precision and initial difference
    precision_value = 0.001
    precision_achieved = False

    while precision_achieved == False:
        
        # Get a copy of the previous distribution
        previous_distribution = distribution.copy()
        
        for page in distribution:

            # Initialize second term of the formula
            target_prob = 0

            # Get the links of the current page
            links = []
            for current, targets in corpus.items():
                if page in targets or len(targets)==0:          
                    links.append(current)

            # A page that has no links at all is interpreted as having one link for every page in the corpus (including itself)
            if len(links) == 0:
                for page in corpus:
                    links.append(page)

            # Calculate probability of links
            for target in links:

                num_links = len(corpus[target])
                
                if num_links == 0:
                    num_links = len(corpus)

                target_prob += previous_distribution[target] / num_links 
                
                # Calculate probability for current page using background formula
                distribution[page] = (1 - damping_factor) / len(corpus) + damping_factor * target_prob
                
        # Check if desired precision is achieved
        check_difference = []
        for page in distribution:
            if abs(distribution[page] - previous_distribution[page]) < precision_value:
                check_difference.append(True)
            else:
                check_difference.append(False)

        # If precision is achieved for all pages, set it True
        if all(check_difference):
            precision_achieved = True

    #SUM
    total = 0
    for page in distribution:
        total += distribution[page]

    print("ITERATION ==>",total)

    return distribution


if __name__ == "__main__":
    main()
