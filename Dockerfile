FROM apache/airflow:2.9.1                                                                                                                                                                     
                                                                                                                                                                                            
USER airflow                                                                                                                                                                                     
                                                                                                                                                                                            
RUN pip install uv                                                                                                                                                                            

COPY pyproject.toml uv.lock* /opt/airflow/

# install your project deps (scipy, pandas, etc.)
RUN uv pip install --system /opt/airflow
                                                                                                                                                                      
   
