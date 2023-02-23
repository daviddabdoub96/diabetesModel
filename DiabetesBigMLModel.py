def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/63f7a7d58f679a1d3b8d7f17

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] at UCI[*] Machine Learning Repository[*]
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI: http://cml.ics.uci.edu/
        [*]Machine Learning Repository: http://archive.ics.uci.edu/ml/index.html
    """
    if (glucose is None):
        return u'false'
    if (glucose > 127):
        if (bmi is None):
            return u'true'
        if (bmi > 30.17976):
            if (glucose > 157):
                if (insulin is None):
                    return u'true'
                if (insulin > 629):
                    return u'false'
                if (insulin <= 629):
                    if (diabetes_pedigree is None):
                        return u'true'
                    if (diabetes_pedigree > 0.32285):
                        if (age is None):
                            return u'true'
                        if (age > 44):
                            if (diabetes_pedigree > 1.1565):
                                return u'false'
                            if (diabetes_pedigree <= 1.1565):
                                if (age > 50):
                                    return u'true'
                                if (age <= 50):
                                    if (bmi > 37.25):
                                        return u'true'
                                    if (bmi <= 37.25):
                                        return u'false'
                        if (age <= 44):
                            return u'true'
                    if (diabetes_pedigree <= 0.32285):
                        if (age is None):
                            return u'true'
                        if (age > 37):
                            if (age > 56):
                                if (bmi > 34.85):
                                    return u'true'
                                if (bmi <= 34.85):
                                    return u'false'
                            if (age <= 56):
                                return u'true'
                        if (age <= 37):
                            if (blood_pressure is None):
                                return u'true'
                            if (blood_pressure > 69):
                                if (bmi > 45.6):
                                    return u'false'
                                if (bmi <= 45.6):
                                    if (skinfold is None):
                                        return u'true'
                                    if (skinfold > 9):
                                        return u'true'
                                    if (skinfold <= 9):
                                        return u'false'
                            if (blood_pressure <= 69):
                                return u'false'
            if (glucose <= 157):
                if (age is None):
                    return u'true'
                if (age > 30):
                    if (diabetes_pedigree is None):
                        return u'true'
                    if (diabetes_pedigree > 0.43188):
                        if (age > 44):
                            return u'true'
                        if (age <= 44):
                            if (insulin is None):
                                return u'true'
                            if (insulin > 306):
                                return u'false'
                            if (insulin <= 306):
                                if (bmi > 39.65):
                                    if (bmi > 40.9):
                                        return u'true'
                                    if (bmi <= 40.9):
                                        return u'false'
                                if (bmi <= 39.65):
                                    return u'true'
                    if (diabetes_pedigree <= 0.43188):
                        if (bmi > 45.55):
                            return u'true'
                        if (bmi <= 45.55):
                            if (blood_pressure is None):
                                return u'false'
                            if (blood_pressure > 71):
                                if (blood_pressure > 92):
                                    return u'true'
                                if (blood_pressure <= 92):
                                    if (pregnancies is None):
                                        return u'false'
                                    if (pregnancies > 8):
                                        return u'false'
                                    if (pregnancies <= 8):
                                        if (bmi > 30.85):
                                            if (bmi > 32.45):
                                                if (diabetes_pedigree > 0.256):
                                                    return u'true'
                                                if (diabetes_pedigree <= 0.256):
                                                    if (bmi > 33.1):
                                                        return u'false'
                                                    if (bmi <= 33.1):
                                                        return u'true'
                                            if (bmi <= 32.45):
                                                return u'false'
                                        if (bmi <= 30.85):
                                            return u'true'
                            if (blood_pressure <= 71):
                                return u'true'
                if (age <= 30):
                    if (blood_pressure is None):
                        return u'false'
                    if (blood_pressure > 61):
                        if (insulin is None):
                            return u'false'
                        if (insulin > 260):
                            return u'false'
                        if (insulin <= 260):
                            if (bmi > 41.7):
                                if (blood_pressure > 85):
                                    return u'true'
                                if (blood_pressure <= 85):
                                    if (bmi > 42.7):
                                        return u'false'
                                    if (bmi <= 42.7):
                                        return u'true'
                            if (bmi <= 41.7):
                                if (diabetes_pedigree is None):
                                    return u'false'
                                if (diabetes_pedigree > 1.1415):
                                    return u'true'
                                if (diabetes_pedigree <= 1.1415):
                                    if (bmi > 38.05):
                                        return u'false'
                                    if (bmi <= 38.05):
                                        if (diabetes_pedigree > 0.57):
                                            return u'false'
                                        if (diabetes_pedigree <= 0.57):
                                            if (diabetes_pedigree > 0.4875):
                                                return u'true'
                                            if (diabetes_pedigree <= 0.4875):
                                                if (bmi > 37.65):
                                                    return u'true'
                                                if (bmi <= 37.65):
                                                    if (skinfold is None):
                                                        return u'false'
                                                    if (skinfold > 30):
                                                        if (bmi > 32.4):
                                                            if (blood_pressure > 68):
                                                                return u'false'
                                                            if (blood_pressure <= 68):
                                                                return u'true'
                                                        if (bmi <= 32.4):
                                                            return u'true'
                                                    if (skinfold <= 30):
                                                        return u'false'
                    if (blood_pressure <= 61):
                        return u'true'
        if (bmi <= 30.17976):
            if (glucose > 145):
                if (age is None):
                    return u'true'
                if (age > 25):
                    if (age > 61):
                        return u'false'
                    if (age <= 61):
                        if (age > 41):
                            if (pregnancies is None):
                                return u'true'
                            if (pregnancies > 9):
                                if (bmi > 27.25):
                                    return u'false'
                                if (bmi <= 27.25):
                                    return u'true'
                            if (pregnancies <= 9):
                                return u'true'
                        if (age <= 41):
                            if (blood_pressure is None):
                                return u'false'
                            if (blood_pressure > 74):
                                return u'false'
                            if (blood_pressure <= 74):
                                if (glucose > 163):
                                    return u'true'
                                if (glucose <= 163):
                                    if (bmi > 28.65):
                                        return u'false'
                                    if (bmi <= 28.65):
                                        if (blood_pressure > 67):
                                            return u'true'
                                        if (blood_pressure <= 67):
                                            return u'false'
                if (age <= 25):
                    return u'false'
            if (glucose <= 145):
                if (insulin is None):
                    return u'false'
                if (insulin > 132):
                    return u'false'
                if (insulin <= 132):
                    if (bmi > 28.15):
                        if (bmi > 28.55):
                            if (glucose > 135):
                                return u'false'
                            if (glucose <= 135):
                                return u'true'
                        if (bmi <= 28.55):
                            return u'true'
                    if (bmi <= 28.15):
                        if (blood_pressure is None):
                            return u'false'
                        if (blood_pressure > 73):
                            return u'false'
                        if (blood_pressure <= 73):
                            if (diabetes_pedigree is None):
                                return u'false'
                            if (diabetes_pedigree > 0.437):
                                return u'false'
                            if (diabetes_pedigree <= 0.437):
                                if (pregnancies is None):
                                    return u'false'
                                if (pregnancies > 5):
                                    return u'false'
                                if (pregnancies <= 5):
                                    if (bmi > 23.45):
                                        return u'true'
                                    if (bmi <= 23.45):
                                        return u'false'
    if (glucose <= 127):
        if (age is None):
            return u'false'
        if (age > 28):
            if (bmi is None):
                return u'false'
            if (bmi > 26.2625):
                if (glucose > 89):
                    if (diabetes_pedigree is None):
                        return u'false'
                    if (diabetes_pedigree > 0.62075):
                        if (pregnancies is None):
                            return u'true'
                        if (pregnancies > 7):
                            return u'true'
                        if (pregnancies <= 7):
                            if (glucose > 96):
                                if (skinfold is None):
                                    return u'true'
                                if (skinfold > 47):
                                    return u'false'
                                if (skinfold <= 47):
                                    if (glucose > 105):
                                        if (glucose > 108):
                                            if (diabetes_pedigree > 0.85):
                                                return u'true'
                                            if (diabetes_pedigree <= 0.85):
                                                if (blood_pressure is None):
                                                    return u'true'
                                                if (blood_pressure > 66):
                                                    if (blood_pressure > 73):
                                                        if (blood_pressure > 89):
                                                            return u'false'
                                                        if (blood_pressure <= 89):
                                                            return u'true'
                                                    if (blood_pressure <= 73):
                                                        return u'false'
                                                if (blood_pressure <= 66):
                                                    return u'true'
                                        if (glucose <= 108):
                                            return u'false'
                                    if (glucose <= 105):
                                        return u'true'
                            if (glucose <= 96):
                                return u'false'
                    if (diabetes_pedigree <= 0.62075):
                        if (age > 54):
                            return u'false'
                        if (age <= 54):
                            if (skinfold is None):
                                return u'false'
                            if (skinfold > 27):
                                if (glucose > 102):
                                    if (diabetes_pedigree > 0.2):
                                        if (pregnancies is None):
                                            return u'false'
                                        if (pregnancies > 1):
                                            if (pregnancies > 5):
                                                if (glucose > 120):
                                                    if (diabetes_pedigree > 0.5385):
                                                        return u'true'
                                                    if (diabetes_pedigree <= 0.5385):
                                                        return u'false'
                                                if (glucose <= 120):
                                                    return u'true'
                                            if (pregnancies <= 5):
                                                return u'false'
                                        if (pregnancies <= 1):
                                            return u'true'
                                    if (diabetes_pedigree <= 0.2):
                                        return u'false'
                                if (glucose <= 102):
                                    return u'false'
                            if (skinfold <= 27):
                                if (blood_pressure is None):
                                    return u'true'
                                if (blood_pressure > 83):
                                    if (diabetes_pedigree > 0.3955):
                                        if (bmi > 31.45):
                                            return u'true'
                                        if (bmi <= 31.45):
                                            return u'false'
                                    if (diabetes_pedigree <= 0.3955):
                                        return u'false'
                                if (blood_pressure <= 83):
                                    if (age > 34):
                                        if (pregnancies is None):
                                            return u'true'
                                        if (pregnancies > 4):
                                            if (age > 39):
                                                if (glucose > 107):
                                                    if (glucose > 118):
                                                        if (diabetes_pedigree > 0.2315):
                                                            return u'false'
                                                        if (diabetes_pedigree <= 0.2315):
                                                            return u'true'
                                                    if (glucose <= 118):
                                                        return u'true'
                                                if (glucose <= 107):
                                                    if (skinfold > 12):
                                                        return u'true'
                                                    if (skinfold <= 12):
                                                        return u'false'
                                            if (age <= 39):
                                                return u'true'
                                        if (pregnancies <= 4):
                                            return u'true'
                                    if (age <= 34):
                                        if (pregnancies is None):
                                            return u'false'
                                        if (pregnancies > 6):
                                            return u'true'
                                        if (pregnancies <= 6):
                                            if (skinfold > 13):
                                                return u'false'
                                            if (skinfold <= 13):
                                                if (blood_pressure > 65):
                                                    if (bmi > 28.55):
                                                        return u'false'
                                                    if (bmi <= 28.55):
                                                        return u'true'
                                                if (blood_pressure <= 65):
                                                    return u'true'
                if (glucose <= 89):
                    if (bmi > 29.9):
                        return u'false'
                    if (bmi <= 29.9):
                        if (skinfold is None):
                            return u'false'
                        if (skinfold > 30):
                            return u'true'
                        if (skinfold <= 30):
                            if (diabetes_pedigree is None):
                                return u'false'
                            if (diabetes_pedigree > 0.9955):
                                return u'true'
                            if (diabetes_pedigree <= 0.9955):
                                return u'false'
            if (bmi <= 26.2625):
                return u'false'
        if (age <= 28):
            if (bmi is None):
                return u'false'
            if (bmi > 30.33846):
                if (insulin is None):
                    return u'false'
                if (insulin > 172):
                    return u'false'
                if (insulin <= 172):
                    if (diabetes_pedigree is None):
                        return u'false'
                    if (diabetes_pedigree > 0.48765):
                        if (bmi > 32.175):
                            if (bmi > 38.65):
                                if (blood_pressure is None):
                                    return u'false'
                                if (blood_pressure > 79):
                                    if (bmi > 44.1):
                                        return u'false'
                                    if (bmi <= 44.1):
                                        return u'true'
                                if (blood_pressure <= 79):
                                    return u'false'
                            if (bmi <= 38.65):
                                if (skinfold is None):
                                    return u'false'
                                if (skinfold > 29):
                                    if (blood_pressure is None):
                                        return u'true'
                                    if (blood_pressure > 61):
                                        if (blood_pressure > 86):
                                            return u'false'
                                        if (blood_pressure <= 86):
                                            if (bmi > 36.7):
                                                if (bmi > 37.4):
                                                    return u'true'
                                                if (bmi <= 37.4):
                                                    return u'false'
                                            if (bmi <= 36.7):
                                                return u'true'
                                    if (blood_pressure <= 61):
                                        if (blood_pressure > 51):
                                            return u'false'
                                        if (blood_pressure <= 51):
                                            return u'true'
                                if (skinfold <= 29):
                                    if (age > 26):
                                        if (insulin > 107):
                                            return u'false'
                                        if (insulin <= 107):
                                            if (glucose > 95):
                                                return u'true'
                                            if (glucose <= 95):
                                                return u'false'
                                    if (age <= 26):
                                        return u'false'
                        if (bmi <= 32.175):
                            return u'false'
                    if (diabetes_pedigree <= 0.48765):
                        if (bmi > 45.35):
                            return u'true'
                        if (bmi <= 45.35):
                            if (diabetes_pedigree > 0.28612):
                                return u'false'
                            if (diabetes_pedigree <= 0.28612):
                                if (blood_pressure is None):
                                    return u'false'
                                if (blood_pressure > 55):
                                    if (skinfold is None):
                                        return u'false'
                                    if (skinfold > 30):
                                        return u'false'
                                    if (skinfold <= 30):
                                        if (blood_pressure > 72):
                                            if (age > 25):
                                                return u'false'
                                            if (age <= 25):
                                                if (diabetes_pedigree > 0.178):
                                                    return u'true'
                                                if (diabetes_pedigree <= 0.178):
                                                    return u'false'
                                        if (blood_pressure <= 72):
                                            return u'false'
                                if (blood_pressure <= 55):
                                    if (blood_pressure > 47):
                                        return u'true'
                                    if (blood_pressure <= 47):
                                        return u'false'
            if (bmi <= 30.33846):
                if (pregnancies is None):
                    return u'false'
                if (pregnancies > 7):
                    return u'true'
                if (pregnancies <= 7):
                    if (diabetes_pedigree is None):
                        return u'false'
                    if (diabetes_pedigree > 0.65467):
                        if (bmi > 23.25):
                            return u'false'
                        if (bmi <= 23.25):
                            return u'true'
                    if (diabetes_pedigree <= 0.65467):
                        return u'false'
