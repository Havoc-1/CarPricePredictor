from PIL import Image
import pytesseract
import io
import fitz
import numpy as np
import pandas as pd
from langchain.docstore.document import Document
import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import OllamaEmbeddings, ChatOllama
from typing import List, Union, Dict
import os
from concurrent.futures import ThreadPoolExecutor
import gc

from multiprocessing import Pool, cpu_count
from langchain_community.vectorstores import FAISS
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
import shap
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
from typing import Dict, List, Any
from joblib import Parallel, delayed

import hashlib
import pickle
import os
import numpy as np
from typing import Dict, Any, Optional
import logging
from datetime import datetime, timedelta
import json
import shap
import warnings
warnings.filterwarnings('ignore')


# Configure logging with a more efficient format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


class PreCalculationPipeline:
    def __init__(self, cache_dir=".cache"):
        self.cache_dir = cache_dir
        self.shap_cache = SHAPCache(cache_dir=cache_dir)