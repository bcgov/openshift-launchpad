/*
 * Create an admin user with admin/admin
 */
import jenkins.model.*
import hudson.security.*

println "--> creating admin user"

def adminUsername = System.getenv("ADMIN_USERNAME") ?: "admin"
def adminPassword = System.getenv("ADMIN_PASSWORD") ?: "admin"

def hudsonRealm = new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount(adminUsername, adminPassword)
Jenkins.instance.setSecurityRealm(hudsonRealm)
def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
strategy.setAllowAnonymousRead(false)
Jenkins.instance.setAuthorizationStrategy(strategy)

Jenkins.instance.save()