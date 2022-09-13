import candidate_class_ver1 as ccv1
import candidate_class_ver2 as ccv2


if __name__ == '__main__':
    Guido = ccv1.Candidate('Guido', 'van Rossum', 'guido@python.org',
                           ['Python', 'Django', 'JS'], 'Python', 'Senior')
    print(Guido.__dict__)
    print(Guido.full_name)
    # creating instances from a file in a directory
    candidates = ccv1.Candidate.generate_candidate('Candidates.csv')
    print(candidates)
    for obj in candidates:
        print(obj.full_name)
        print(obj.__dict__)
    # creating instances from a file by url
    candidates = ccv2.Candidate.generate_candidate('https://bitbucket.org/ivnukov/lesson2/raw/'
                                                   '4f59074e6fbb552398f87636b5bf089a1618da0a/'
                                                   'candidates.csv')
    print(candidates)
    for obj in candidates:
        print(obj.full_name)
        print(obj.__dict__)
