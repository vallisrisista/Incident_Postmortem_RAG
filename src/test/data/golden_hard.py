GOLDEN_HARD = [

    # Config / deployment / service discovery
    (
        "things looked fine after deploy but internal name resolution started failing",
        "72d4feb2b782"
    ),
    (
        "read traffic cannot reach the database anymore even though the hosts are still up",
        "a54d7767497a"
    ),
    (
        "traffic went up and the platform did not spin up more instances",
        "eaa38fc3c0f8"
    ),
    (
        "jobs are sitting there and not getting picked up after a database-related deploy",
        "b51464122ab4"
    ),
    (
        "one bad dependency seems to have taken down service discovery everywhere",
        "74590d8645b8"
    ),
    (
        "new application instances stopped coming up after some remote settings were changed",
        "95138d5bb651"
    ),

    # Power / hardware / datacenter
    (
        "we lost utility power and the backup systems were supposed to take over but did not",
        "67178eb044ee"
    ),
    (
        "machines started shutting themselves down after temperatures went high",
        "6e9363e9c8d5"
    ),
    (
        "multiple cloud services disappeared at once and it looks related to datacenter cooling",
        "e0070fdc39b8"
    ),
    (
        "API and dashboard were unavailable for hours after some strange switch behaviour",
        "061f2e369996"
    ),

    # Failover / race / split state
    (
        "after a short network problem the database switched primary and we seem to be missing recent data",
        "ec4ce24fd285"
    ),
    (
        "during network maintenance both sides of a redundant storage pair ended up offline",
        "d36b669cdbe6"
    ),
    (
        "regional services failed because DNS ended up with no endpoint record",
        "a7441bf5e72f"
    ),
    (
        "IDs started skipping values after database HA failover, but data itself is still there",
        "af5721579948"
    ),

    # Time / certificate
    (
        "DNS crashes only started around a clock correction event",
        "f2e763da04f0"
    ),
    (
        "browser add-ons suddenly stopped being accepted even though nothing was deployed",
        "e12d00a83dfc"
    ),
    (
        "certificate creation worked normally except on a leap-year date",
        "3ac74c8b957a"
    ),

    # Integer / schema / DB limits
    (
        "Git operations and some related services are failing because an ID column may have run out of range",
        "1d6c07a2aa98"
    ),
    (
        "new authorizations and deploys stopped working and we suspect a key column size mismatch",
        "b190d020ff51"
    ),
    (
        "uploads fail only when creating newer records, older data still works",
        "882584558446"
    ),
    (
        "service suddenly became read only and the database is near some numeric limit",
        "c2a97eaa5321"
    ),
    (
        "database upgrade completed but replicas started dying right at the final schema step",
        "8e10f4cc0977"
    ),

    # DB load / capacity / migration
    (
        "the primary database keeps falling behind because work is piling up faster than it can process",
        "9240643d2aeb"
    ),
    (
        "mongo becomes unstable under traffic and memory keeps disappearing",
        "c9de62517f87"
    ),
    (
        "we lowered DB capacity to save money and now everything falls over during busy hours",
        "098f611fc474"
    ),
    (
        "an extension or audit component seems to be holding database locks forever after an upgrade",
        "5693dd48d1df"
    ),
    (
        "secondary database load was moved to primary during troubleshooting and made the outage worse",
        "fc0e44a6434b"
    ),
    (
        "replicas are no longer consistent with the primary and the issue only became visible when a query failed",
        "24407078a602"
    ),

    # Security / leakage
    (
        "responses sometimes contain data that clearly belongs to somebody else's request",
        "bd22739494b0"
    ),
    (
        "the compromise may have entered through a third-party support person's machine",
        "447beb0fbf95"
    ),
    (
        "users cannot log in after a security controls change that was supposed to tighten access",
        "ba6234a5f30a"
    ),
    (
        "the site is reachable but traffic volume looks malicious and extremely high",
        "da690e34e5ea"
    ),

    # Networking
    (
        "after upgrading the cluster, applications are alive but pods cannot communicate properly",
        "2e2955aab2c5"
    ),
    (
        "billing started charging some customers repeatedly after a brief connectivity problem",
        "e07352c30eab"
    ),
    (
        "we are seeing packet loss and the provider gateway looks saturated",
        "6ecf86458221"
    ),

    # Capacity / cascading overload
    (
        "login service slowed down badly because failures in another component started cascading into it",
        "34bd9baedde2"
    ),
    (
        "after users reconnected together, the database could not handle the sudden burst",
        "78e6ca0bf459"
    ),

    # Human / operational mistakes
    (
        "during troubleshooting someone removed far more production machines than intended",
        "e49eb2bce070"
    ),
    (
        "an operator meant to restart a small group of servers but ended up restarting the entire site",
        "16c9accc0b12"
    ),
    (
        "a security rule change caused CPU to max out almost immediately",
        "55c51e75f787"
    ),
]