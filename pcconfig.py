import pynecone as pc

class GalnailingConfig(pc.Config):
    pass

config = GalnailingConfig(
    app_name="galnailing",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)

#config = pc.Config(
#    app_name="galnailing",
#    api_url="http://174.115.119.13:8000",
#    bun_path="$HOME/.bun/bin/bun",
#    db_url="sqlite:///pynecone.db",
#)