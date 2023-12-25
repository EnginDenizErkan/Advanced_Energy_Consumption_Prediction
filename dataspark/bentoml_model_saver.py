import bentoml
import xgboost
from xgboost import XGBRegressor

# To load the model later using XGBoost
trained_xgb_model = XGBRegressor()
trained_xgb_model.load_model('xgboost_trained_model.model')

# Save model to the BentoML local Model Store
saved_model = bentoml.xgboost.save_model("xgboost_trained_regressor", trained_xgb_model)

