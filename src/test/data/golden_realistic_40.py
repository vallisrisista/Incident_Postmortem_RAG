GOLDEN_REALISTIC_40 =  [

    # Config Errors
    (
        "after a config rollout, some internal services stopped resolving DNS",
        "72d4feb2b782"
    ),
    (
        "database routing health checks suddenly started failing after a change",
        "a54d7767497a"
    ),
    (
        "our deployment looks healthy but new instances are not starting even though capacity is available",
        "eaa38fc3c0f8"
    ),
    (
        "remote configuration did not reach all servers and new application instances cannot start",
        "95138d5bb651"
    ),
    (
        "a valid customer configuration change unexpectedly triggered a global outage",
        "6d10b857eb07"
    ),

    # Hardware / Power
    (
        "power failed at the datacenter and the backup generators did not take over",
        "67178eb044ee"
    ),
    (
        "servers overheated after the cooling control system stopped responding",
        "6e9363e9c8d5"
    ),
    (
        "multiple cooling systems failed at the same time and cloud services became unavailable",
        "e0070fdc39b8"
    ),
    (
        "datacenter power interruption caused the main service to go offline",
        "897903de2ce7"
    ),

    # Conflicts / distributed system issues
    (
        "database failover happened during a network problem and some recent writes disappeared",
        "ec4ce24fd285"
    ),
    (
        "two nodes ended up shutting each other down during a network switch maintenance event",
        "d36b669cdbe6"
    ),
    (
        "different application versions were active together and caused incorrect processing",
        "6b198b63f3d7"
    ),
    (
        "database IDs started jumping after we promoted a replica to primary",
        "af5721579948"
    ),

    # Time related
    (
        "DNS requests started crashing around a leap second event",
        "f2e763da04f0"
    ),
    (
        "users suddenly lost browser extensions because a signing certificate was no longer valid",
        "e12d00a83dfc"
    ),
    (
        "certificate generation broke because the date calculation did not handle leap year correctly",
        "3ac74c8b957a"
    ),

    # Database
    (
        "new records stopped being created because an integer ID reached its maximum value",
        "1d6c07a2aa98"
    ),
    (
        "database replicas started crashing near the end of a schema migration",
        "8e10f4cc0977"
    ),
    (
        "a foreign key column could no longer hold the values coming from the primary key",
        "b190d020ff51"
    ),
    (
        "file uploads suddenly stopped because the database identifier became too large",
        "882584558446"
    ),
    (
        "postgres stopped working because transaction IDs wrapped around",
        "a0aa73d201de"
    ),
    (
        "database became read only after an integer field reached its limit",
        "c2a97eaa5321"
    ),
    (
        "mongo started failing badly under load because memory usage kept increasing",
        "c9de62517f87"
    ),
    (
        "after reducing database capacity to save cost, production collapsed during peak traffic",
        "098f611fc474"
    ),
    (
        "database requests kept queueing until the primary could no longer catch up",
        "9240643d2aeb"
    ),
    (
        "a routine postgres migration hung and started blocking most application operations",
        "5693dd48d1df"
    ),

    # Security
    (
        "some users are receiving pieces of data that belong to other requests",
        "bd22739494b0"
    ),
    (
        "security breach appears to have started from a support engineer's computer",
        "447beb0fbf95"
    ),
    (
        "website is being flooded with huge amounts of malicious traffic",
        "da690e34e5ea"
    ),
    (
        "a security policy update unexpectedly blocked legitimate users from accessing resources",
        "ba6234a5f30a"
    ),

    # Networking
    (
        "pods stopped communicating after the Kubernetes cluster was upgraded",
        "2e2955aab2c5"
    ),
    (
        "temporary Redis network split resulted in customers getting charged more than once",
        "e07352c30eab"
    ),
    (
        "packet loss started after cloud network gateways became saturated",
        "6ecf86458221"
    ),

    # Capacity / overload
    (
        "authentication service became overloaded after another service started failing repeatedly",
        "34bd9baedde2"
    ),
    (
        "users reconnecting at the same time overwhelmed the database after an outage",
        "78e6ca0bf459"
    ),

    # Operational / Human Error
    (
        "someone ran the wrong admin command and accidentally removed too many production servers",
        "e49eb2bce070"
    ),
    (
        "maintenance command restarted the whole datacenter instead of only a few machines",
        "16c9accc0b12"
    ),
    (
        "a bad regex in a security rule caused CPU usage to spike and the service went down",
        "55c51e75f787"
    ),
    (
        "a bad update passed validation and caused millions of Windows machines to crash",
        "ae544c4fec19"
    ),
    (
        "database replication was already unhealthy and an admin accidentally deleted the wrong data directory",
        "f962a1878a6c"
    ),
]