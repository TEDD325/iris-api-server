import mlflow

def load_model():
    print('Loading Model...')
    return mlflow.sklearn.load_model('models:/iris_model/production') # mlflow를 통해 확인 할 수 있는 모델 정보. 즉, 앞선 실습에서 이미 돌린 모델의 경로임