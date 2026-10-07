GOLDEN_BASIC = [
    # Config Errors
    (
        "DNS configuration change caused container services to lose DNS resolution",
        "72d4feb2b782"   # PagerDuty
    ),
    (
        "database configuration rollout broke routing health checks and marked read endpoint unhealthy",
        "a54d7767497a"   # GitHub
    ),

    # Hardware / Power
    (
        "backup generators failed to start after transformer failure because phase alignment check failed",
        "67178eb044ee"   # Amazon
    ),
    (
        "cooling control system became unresponsive causing servers to overheat and power off",
        "6e9363e9c8d5"   # Amazon
    ),

    # Conflicts
    (
        "network partition during maintenance caused MySQL master failover before writes replicated",
        "ec4ce24fd285"   # GitHub
    ),
    (
        "conflicting deployed versions and reused flag caused massive trading loss",
        "6b198b63f3d7"   # Knight Capital
    ),

    # Time
    (
        "leap second caused DNS resolver weighted round robin logic to panic",
        "f2e763da04f0"   # Cloudflare
    ),
    (
        "expired certificate disabled thousands of browser add-ons",
        "e12d00a83dfc"   # Mozilla
    ),

    # Database
    (
        "foreign key scoped token table reached INT32 maximum and required migration to INT64",
        "1d6c07a2aa98"   # GitHub
    ),
    (
        "MySQL replicas entered semaphore deadlock and crash recovery during schema migration",
        "8e10f4cc0977"   # GitHub
    ),
    (
        "foreign key had smaller datatype than referenced primary key causing overflow",
        "b190d020ff51"   # Heroku
    ),
    (
        "signed integer primary key limit caused uploads to fail",
        "882584558446"   # Strava
    ),

    # Security
    (
        "parser bug returned private memory containing cookies authentication tokens and request bodies",
        "bd22739494b0"   # Cloudflare
    ),
    (
        "attacker gained access through third party support engineer laptop",
        "447beb0fbf95"   # Okta
    ),

    # Networking
    (
        "Kubernetes cluster upgrade changed node metadata and broke workload networking",
        "2e2955aab2c5"   # Reddit
    ),
    (
        "network partition in Redis billing cluster caused resynchronization and duplicate customer charges",
        "e07352c30eab"   # Twilio
    ),

    # Capacity / Overload
    (
        "merchant authentication service overloaded because of cascading errors from adjacent service",
        "34bd9baedde2"   # Square
    ),

    # Operational / Human Error
    (
        "debugging command typo removed too many servers supporting critical storage systems",
        "e49eb2bce070"   # Amazon
    ),
    (
        "operator forgot command flag and rebooted every server in datacenter",
        "16c9accc0b12"   # Joyent
    ),
    (
        "bad regular expression in firewall rule exhausted CPU and caused global outage",
        "55c51e75f787"   # Cloudflare
    ),
]
