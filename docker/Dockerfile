FROM continuumio/miniconda3
RUN conda update -n base -c defaults conda
RUN groupadd -g 10027 seafood && useradd --no-log-init -m -s /bin/bash -g seafood seafood
RUN chown seafood:seafood /opt/conda
USER seafood
WORKDIR /home/seafood
RUN conda init 
# Create the environment:
COPY environment/environment.yml .
RUN conda env create --name imaging-env -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "imaging-env", "/bin/bash", "-c"]

COPY ./src /home/seafood
EXPOSE 8080

# The code to run when container is started:
# ENTRYPOINT ["conda", "run", "-n", "imaging-env", "python3", "src/main.py"]


