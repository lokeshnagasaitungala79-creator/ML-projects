import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifats' , "train_csv")
    test_data_path  : str = os.path.join('artifats' , "test_csv")
    raw_data_path : str = os.path.join('artifats' , "data_csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component or method")
        try:
            df = pd.read_csv(r'C:\Users\tunga\OneDrive\Documents\ML Projects\Note book\data\stud.csv')
            logging.info("read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path , header=True ,index=False)
            logging.info("train test split intitated")
            train_set , test_set = train_test_split(df , test_size=0.2 , random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path , header = True , index = False)
            test_set.to_csv(self.ingestion_config.test_data_path , header = True , index = False)

            logging.info("Inmgestion is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(sys , e)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


    

