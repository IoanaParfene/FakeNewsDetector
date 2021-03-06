import preprocessing
import testing
import corpus
import classifiers as c
import data_models

if __name__ == "__main__":
    # Gather news from websites and separate in json files
    # scraper.scrape_data()

    # Get fake news and data news corpus
    true_news_corpus, fake_news_corpus = corpus.get_corpus()
    data_models.get_corpus_word_count(true_news_corpus, fake_news_corpus)

    # Preprocess data and add to json files
    # preprocessing.preprocess_data(true_news_corpus, fake_news_corpus)

    # Get preprocessed data
    true_pre_data, fake_pre_data = preprocessing.get_preprocessed_data()
    data_models.get_processed_data_word_count(true_pre_data, fake_pre_data)

    # Merge labeled data
    merged_labeled_data = preprocessing.merge_news(true_pre_data, fake_pre_data)

    # Get word_frequency
    word_frequency = preprocessing.get_word_frequency(merged_labeled_data)

    # Get vocabulary
    vocabulary = preprocessing.get_vocabulary(merged_labeled_data, word_frequency)

    # Test something
    testing.test_classifier("Voting Classifier", "LogisticRegression(),RandomForestClassifier(),KNeighborsClassifier()",
                            vocabulary, merged_labeled_data, "c.voting_classifier")
