#!/usr/bin/env python
# coding: UTF-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.preprocessing import StandardScaler, MinMaxScaler, label_binarize
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from scipy import interp

class ML():
    def preProcessing(self, X):
        #X = StandardScaler().fit_transform(X)
        X = MinMaxScaler().fit_transform(X)

        return pd.DataFrame(X)

    def pca(self, X, n_components=2):
        pca = PCA(n_components = n_components)
        X   = pca.fit_transform(X)

        return pd.DataFrame(X)

    def cca(self, X1, X2, n_components=2):
        cca    = CCA(n_components = n_components)
        X1, X2 = cca.fit_transform(X1,X2)

        '''
        from scipy.stats import pearsonr
        print("Correlation Coefficient")
        for i in range(n_components):
            print("{0}:{1:.3f}".format(i, pearsonr(cca.x_scores_[:,i], cca.y_scores_[:,i])[0]))
        print("")
        print("")
        np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
        print("X1 loadings")
        print(cca.x_loadings_.T)
        print("")
        print("X2 loadings")
        print(cca.y_loadings_.T)
        '''

        return pd.DataFrame(X1)

    def lda(self, X, y, n_components=2):
        lda = LDA(n_components=n_components)
        X   = lda.fit_transform(X, y)

        return pd.DataFrame(X)

    def svm(self, X, y):
        print  '---SVM--'

        feature_names = X.columns.values
        class_names   = np.unique(y)
        print  'Feature names:', feature_names
        print  'Class names:', class_names

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        X_combined = np.vstack((X_train, X_test))
        y_combined = np.hstack((y_train, y_test))
        print  'Train samples:', len(X)*0.7
        print  'Test samples:', len(X)*0.3

        gs = GridSearchCV(
                          estimator=SVC(kernel='rbf', random_state=1, probability=True),
                          param_grid=[{ 'gamma': [1, 0.1, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}],
                          scoring='accuracy',
                          cv=5)
        gs.fit(X_train, y_train)

        clf=gs.best_estimator_

        print 'Accuracy: %.3f' % clf.score(X_test, y_test)
        print 'Precision: %.3f' % precision_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'Recall: %.3f' % recall_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'F1: %.3f' % f1_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print '\n'

        print classification_report(y_true=y_test, y_pred=clf.predict(X_test))
        self.confusionMatrix(clf, X_test, y_test)
        self.rocCurve(clf, X_test, y_test, class_names)

    def knn(self, X, y):
        print  '---KNN---'

        feature_names = X.columns.values
        class_names   = np.unique(y)
        print  'Feature names:', feature_names
        print  'Class names:', class_names

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        X_combined = np.vstack((X_train, X_test))
        y_combined = np.hstack((y_train, y_test))
        print  'Train samples:', len(X)*0.7
        print  'Test samples:', len(X)*0.3

        gs = GridSearchCV(
                          estimator=KNeighborsClassifier(p=2, metric='minkowski'),
                          param_grid=[{'n_neighbors':[1, 2, 3, 4, 5, 6, 7]}],
                          scoring='accuracy',
                          cv=5)
        gs.fit(X_train, y_train)

        clf=gs.best_estimator_
        print 'Accuracy: %.3f' % clf.score(X_test, y_test)
        print 'Precision: %.3f' % precision_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'Recall: %.3f' % recall_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'F1: %.3f' % f1_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print '\n'

        print classification_report(y_true=y_test, y_pred=clf.predict(X_test))
        self.confusionMatrix(clf, X_test, y_test)
        self.rocCurve(clf, X_test, y_test, class_names)

    def randomForest(self, X, y):
        print  '---RF---'

        feature_names = X.columns.values
        class_names   = np.unique(y)
        print  'Feature names:', feature_names
        print  'Class names:', class_names

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        X_combined = np.vstack((X_train, X_test))
        y_combined = np.hstack((y_train, y_test))
        print  'Train samples:', len(X)*0.7
        print  'Test samples:', len(X)*0.3

        gs = GridSearchCV(
                          estimator=RandomForestClassifier(criterion='entropy', n_estimators=10,  random_state=1, n_jobs=2),
                          param_grid=[{'max_depth': [1, 2, 3, 4, 5, 6, 7]}],
                          scoring='accuracy',
                          cv=5)
        gs.fit(X_train, y_train)

        clf=gs.best_estimator_
        print 'Accuracy: %.3f' % clf.score(X_test, y_test)
        print 'Precision: %.3f' % precision_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'Recall: %.3f' % recall_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print 'F1: %.3f' % f1_score(y_true=y_test, y_pred=clf.predict(X_test), average='micro')
        print '\n'

        print classification_report(y_true=y_test, y_pred=clf.predict(X_test))
        self.confusionMatrix(clf, X_test, y_test)
        self.rocCurve(clf, X_test, y_test, class_names)

    def confusionMatrix(self, clf, X_test, y_test):
        confmat = confusion_matrix(y_true=y_test, y_pred=clf.predict(X_test))
        fig, ax = plt.subplots(figsize=(2.5, 2.5))
        ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
        for i in range(confmat.shape[0]):
            for j in range(confmat.shape[1]):
                ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
        plt.xlabel('predicted label')
        plt.ylabel('true label')
        plt.tight_layout()
        #plt.savefig('./figures/confusion.png', dpi=300)
        plt.show()

    def rocCurve(self, clf, X_test, y_test, class_names):
        n_classes = len(class_names)

        y_test  = label_binarize(y_test, classes=class_names)
        y_proba = clf.predict_proba(X_test)

        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_test[:,i], y_proba[:,i], pos_label=1)
            roc_auc[i] = auc(fpr[i], tpr[i])

        fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_proba.ravel(), pos_label=1)
        roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

        all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

        mean_tpr = np.zeros_like(all_fpr)
        for i in range(n_classes):
            mean_tpr += interp(all_fpr, fpr[i], tpr[i])

        mean_tpr /= n_classes

        fpr["macro"] = all_fpr
        tpr["macro"] = mean_tpr
        roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

        fig = plt.figure(figsize=(7, 5))

        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], lw=1, label='ROC curve of class {0} (area = {1:0.2f})'''.format(i, roc_auc[i]))

        plt.plot(fpr["micro"], tpr["micro"], 'k--', lw=2, label='micro-average ROC curve (area = {0:0.2f})'''.format(roc_auc["micro"]))
        plt.plot(fpr["macro"], tpr["macro"], 'k--', lw=2, label='macro-average ROC curve (area = {0:0.2f})'''.format(roc_auc["macro"]))
        plt.plot([0, 1], [0, 1], lw=2, linestyle=':', color='black', label='perfect performance')

        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.0])
        plt.xlabel('false positive rate')
        plt.ylabel('true positive rate')
        plt.title('Receiver Operator Characteristic')
        plt.legend(loc="lower right")
        plt.tight_layout()
        # plt.savefig('./figures/roc.png', dpi=300)
        plt.show()


if __name__ == '__main__':

    #======テスト用データセット1=====
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    X = df.drop('target',axis=1)
    y = df['target']
    #=============================

    #======テスト用データセット2=====
    wine = datasets.load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target_names[wine.target]
    X = df.drop('target',axis=1)
    y = df['target']
    #=============================

    ml = ML()
    ml.svm(X,y)
    ml.knn(X,y)
    ml.randomForest(X,y)
