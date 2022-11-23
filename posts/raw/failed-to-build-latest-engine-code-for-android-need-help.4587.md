att | 2018-10-10 16:35:49 UTC | #1

I want to build the latest Urho3D for android, run following command,

> ./gradlew build

and failed,

> Build 45_InverseKinematics armeabi-v7a
> 
> [1/2] Building CXX object Samples/45_InverseKinematics/CMakeFiles/45_InverseKinematics.dir/InverseKinematics.cpp.o
> 
> [2/2] Linking CXX shared library ../../../../build/intermediates/cmake/debug/obj/armeabi-v7a/lib45_InverseKinematics.so
> 
> &gt; Task :android:launcher-app:packageDebug FAILED
> 
> FAILURE: Build failed with an exception.
> 
> * What went wrong:
> 
> Execution failed for task ':android:launcher-app:packageDebug'.
> 
> &gt; org.gradle.tooling.BuildException (no error message)
> 
> * Try:
> 
> Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
> 
> * Get more help at https://help.gradle.org
> 
> BUILD FAILED in 42m 36s
> 
> 52 actionable tasks: 48 executed, 4 up-to-date

-------------------------

weitjong | 2018-10-10 19:23:28 UTC | #2

Are you using Windows 10 as your host system? If yes then try to shorten your project and Android SDK directory name. There is a known issue on Windows host system caused by cmd.exe having limited command line length.

-------------------------

att | 2018-10-10 23:47:49 UTC | #3

No, I used macos 10.14 to build the engine code.

-------------------------

weitjong | 2018-10-11 02:03:30 UTC | #4

In that case you have to share more of the relevant build log. Use the stacktrace option as suggested.

-------------------------

att | 2018-10-12 00:40:48 UTC | #5

Here is the build log by setting stacktrace:

[details="Log"]

./gradlew build --refresh-dependencies --stacktrace
Starting a Gradle Daemon, 2 stopped Daemons could not be reused, use --status for details

FAILURE: Build failed with an exception.

* Where:
Build file '/Users/att/Work/SDK/Urho3D/buildSrc/build.gradle.kts' line: 23

* What went wrong:
Error resolving plugin [id: 'org.gradle.kotlin.kotlin-dsl', version: '0.18.1']
> Could not resolve all dependencies for configuration 'detachedConfiguration1'.
   > Could not determine artifacts for org.gradle.kotlin.kotlin-dsl:org.gradle.kotlin.kotlin-dsl.gradle.plugin:0.18.1
      > Could not get resource 'https://plugins.gradle.org/m2/org/gradle/kotlin/kotlin-dsl/org.gradle.kotlin.kotlin-dsl.gradle.plugin/0.18.1/org.gradle.kotlin.kotlin-dsl.gradle.plugin-0.18.1.jar'.
         > Could not HEAD 'https://plugins.gradle.org/m2/org/gradle/kotlin/kotlin-dsl/org.gradle.kotlin.kotlin-dsl.gradle.plugin/0.18.1/org.gradle.kotlin.kotlin-dsl.gradle.plugin-0.18.1.jar'.
            > Read timed out

* Try:
Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Exception is:
org.gradle.api.GradleException: Error resolving plugin [id: 'org.gradle.kotlin.kotlin-dsl', version: '0.18.1']
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator.resolveToFoundResult(DefaultPluginRequestApplicator.java:255)
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator.access$100(DefaultPluginRequestApplicator.java:63)
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator$1.transform(DefaultPluginRequestApplicator.java:91)
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator$1.transform(DefaultPluginRequestApplicator.java:88)
        at org.gradle.util.CollectionUtils.collect(CollectionUtils.java:204)
        at org.gradle.util.CollectionUtils.collect(CollectionUtils.java:199)
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator.applyPlugins(DefaultPluginRequestApplicator.java:88)
        at org.gradle.kotlin.dsl.provider.PluginRequestsHandler.handle(PluginRequestsHandler.kt:49)
        at org.gradle.kotlin.dsl.provider.StandardKotlinScriptEvaluator$InterpreterHost.applyPluginsTo(KotlinScriptEvaluator.kt:155)
        at org.gradle.kotlin.dsl.execution.Interpreter$ProgramHost.applyPluginsTo(Interpreter.kt:348)
        at Program.execute(Unknown Source)
        at org.gradle.kotlin.dsl.execution.Interpreter$ProgramHost.eval(Interpreter.kt:481)
        at org.gradle.kotlin.dsl.execution.Interpreter.eval(Interpreter.kt:180)
        at org.gradle.kotlin.dsl.provider.StandardKotlinScriptEvaluator.evaluate(KotlinScriptEvaluator.kt:101)
        at org.gradle.kotlin.dsl.provider.KotlinScriptPluginFactory$create$1.invoke(KotlinScriptPluginFactory.kt:51)
        at org.gradle.kotlin.dsl.provider.KotlinScriptPluginFactory$create$1.invoke(KotlinScriptPluginFactory.kt:36)
        at org.gradle.kotlin.dsl.provider.KotlinScriptPlugin.apply(KotlinScriptPlugin.kt:34)
        at org.gradle.configuration.BuildOperationScriptPlugin$1.run(BuildOperationScriptPlugin.java:61)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.configuration.BuildOperationScriptPlugin.apply(BuildOperationScriptPlugin.java:58)
        at org.gradle.configuration.project.BuildScriptProcessor.execute(BuildScriptProcessor.java:41)
        at org.gradle.configuration.project.BuildScriptProcessor.execute(BuildScriptProcessor.java:26)
        at org.gradle.configuration.project.ConfigureActionsProjectEvaluator.evaluate(ConfigureActionsProjectEvaluator.java:34)
        at org.gradle.configuration.project.LifecycleProjectEvaluator$EvaluateProject.run(LifecycleProjectEvaluator.java:105)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.configuration.project.LifecycleProjectEvaluator.evaluate(LifecycleProjectEvaluator.java:68)
        at org.gradle.api.internal.project.DefaultProject.evaluate(DefaultProject.java:682)
        at org.gradle.api.internal.project.DefaultProject.evaluate(DefaultProject.java:138)
        at org.gradle.execution.TaskPathProjectEvaluator.configure(TaskPathProjectEvaluator.java:35)
        at org.gradle.execution.TaskPathProjectEvaluator.configureHierarchy(TaskPathProjectEvaluator.java:60)
        at org.gradle.configuration.DefaultBuildConfigurer.configure(DefaultBuildConfigurer.java:41)
        at org.gradle.initialization.DefaultGradleLauncher$ConfigureBuild.run(DefaultGradleLauncher.java:266)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.initialization.DefaultGradleLauncher.configureBuild(DefaultGradleLauncher.java:179)
        at org.gradle.initialization.DefaultGradleLauncher.doBuildStages(DefaultGradleLauncher.java:138)
        at org.gradle.initialization.DefaultGradleLauncher.executeTasks(DefaultGradleLauncher.java:121)
        at org.gradle.internal.invocation.GradleBuildController$1.call(GradleBuildController.java:77)
        at org.gradle.internal.invocation.GradleBuildController$1.call(GradleBuildController.java:74)
        at org.gradle.internal.work.DefaultWorkerLeaseService.withLocks(DefaultWorkerLeaseService.java:152)
        at org.gradle.internal.work.StopShieldingWorkerLeaseService.withLocks(StopShieldingWorkerLeaseService.java:38)
        at org.gradle.internal.invocation.GradleBuildController.doBuild(GradleBuildController.java:96)
        at org.gradle.internal.invocation.GradleBuildController.run(GradleBuildController.java:74)
        at org.gradle.initialization.buildsrc.BuildSrcUpdateFactory.build(BuildSrcUpdateFactory.java:55)
        at org.gradle.initialization.buildsrc.BuildSrcUpdateFactory.create(BuildSrcUpdateFactory.java:45)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder$3.transform(BuildSourceBuilder.java:122)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder$3.transform(BuildSourceBuilder.java:116)
        at org.gradle.composite.internal.DefaultNestedBuild.run(DefaultNestedBuild.java:87)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder.buildBuildSrc(BuildSourceBuilder.java:116)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder.access$000(BuildSourceBuilder.java:45)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder$2.call(BuildSourceBuilder.java:94)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder$2.call(BuildSourceBuilder.java:91)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$CallableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:314)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$CallableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:304)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:100)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.call(DelegatingBuildOperationExecutor.java:36)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder.createBuildSourceClasspath(BuildSourceBuilder.java:91)
        at org.gradle.initialization.buildsrc.BuildSourceBuilder.buildAndCreateClassLoader(BuildSourceBuilder.java:71)
        at org.gradle.initialization.DefaultSettingsLoader.findSettingsAndLoadIfAppropriate(DefaultSettingsLoader.java:107)
        at org.gradle.initialization.DefaultSettingsLoader.findAndLoadSettings(DefaultSettingsLoader.java:48)
        at org.gradle.initialization.DefaultSettingsLoaderFactory$1.findAndLoadSettings(DefaultSettingsLoaderFactory.java:63)
        at org.gradle.internal.composite.CompositeBuildSettingsLoader.findAndLoadSettings(CompositeBuildSettingsLoader.java:42)
        at org.gradle.initialization.DefaultGradleLauncher$LoadBuild.run(DefaultGradleLauncher.java:246)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.initialization.DefaultGradleLauncher.loadSettings(DefaultGradleLauncher.java:171)
        at org.gradle.initialization.DefaultGradleLauncher.doBuildStages(DefaultGradleLauncher.java:134)
        at org.gradle.initialization.DefaultGradleLauncher.executeTasks(DefaultGradleLauncher.java:121)
        at org.gradle.internal.invocation.GradleBuildController$1.call(GradleBuildController.java:77)
        at org.gradle.internal.invocation.GradleBuildController$1.call(GradleBuildController.java:74)
        at org.gradle.internal.work.DefaultWorkerLeaseService.withLocks(DefaultWorkerLeaseService.java:152)
        at org.gradle.internal.work.StopShieldingWorkerLeaseService.withLocks(StopShieldingWorkerLeaseService.java:38)
        at org.gradle.internal.invocation.GradleBuildController.doBuild(GradleBuildController.java:96)
        at org.gradle.internal.invocation.GradleBuildController.run(GradleBuildController.java:74)
        at org.gradle.tooling.internal.provider.ExecuteBuildActionRunner.run(ExecuteBuildActionRunner.java:28)
        at org.gradle.launcher.exec.ChainingBuildActionRunner.run(ChainingBuildActionRunner.java:35)
        at org.gradle.tooling.internal.provider.ValidatingBuildActionRunner.run(ValidatingBuildActionRunner.java:32)
        at org.gradle.launcher.exec.RunAsBuildOperationBuildActionRunner$3.run(RunAsBuildOperationBuildActionRunner.java:47)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.launcher.exec.RunAsBuildOperationBuildActionRunner.run(RunAsBuildOperationBuildActionRunner.java:43)
        at org.gradle.tooling.internal.provider.SubscribableBuildActionRunner.run(SubscribableBuildActionRunner.java:51)
        at org.gradle.launcher.exec.InProcessBuildActionExecuter$1.transform(InProcessBuildActionExecuter.java:50)
        at org.gradle.launcher.exec.InProcessBuildActionExecuter$1.transform(InProcessBuildActionExecuter.java:46)
        at org.gradle.composite.internal.DefaultRootBuildState.run(DefaultRootBuildState.java:74)
        at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:46)
        at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:32)
        at org.gradle.launcher.exec.BuildTreeScopeBuildActionExecuter.execute(BuildTreeScopeBuildActionExecuter.java:39)
        at org.gradle.launcher.exec.BuildTreeScopeBuildActionExecuter.execute(BuildTreeScopeBuildActionExecuter.java:25)
        at org.gradle.tooling.internal.provider.ContinuousBuildActionExecuter.execute(ContinuousBuildActionExecuter.java:80)
        at org.gradle.tooling.internal.provider.ContinuousBuildActionExecuter.execute(ContinuousBuildActionExecuter.java:53)
        at org.gradle.tooling.internal.provider.ServicesSetupBuildActionExecuter.execute(ServicesSetupBuildActionExecuter.java:62)
        at org.gradle.tooling.internal.provider.ServicesSetupBuildActionExecuter.execute(ServicesSetupBuildActionExecuter.java:34)
        at org.gradle.tooling.internal.provider.GradleThreadBuildActionExecuter.execute(GradleThreadBuildActionExecuter.java:36)
        at org.gradle.tooling.internal.provider.GradleThreadBuildActionExecuter.execute(GradleThreadBuildActionExecuter.java:25)
        at org.gradle.tooling.internal.provider.ParallelismConfigurationBuildActionExecuter.execute(ParallelismConfigurationBuildActionExecuter.java:43)
        at org.gradle.tooling.internal.provider.ParallelismConfigurationBuildActionExecuter.execute(ParallelismConfigurationBuildActionExecuter.java:29)
        at org.gradle.tooling.internal.provider.StartParamsValidatingActionExecuter.execute(StartParamsValidatingActionExecuter.java:59)
        at org.gradle.tooling.internal.provider.StartParamsValidatingActionExecuter.execute(StartParamsValidatingActionExecuter.java:31)
        at org.gradle.tooling.internal.provider.SessionFailureReportingActionExecuter.execute(SessionFailureReportingActionExecuter.java:59)
        at org.gradle.tooling.internal.provider.SessionFailureReportingActionExecuter.execute(SessionFailureReportingActionExecuter.java:44)
        at org.gradle.tooling.internal.provider.SetupLoggingActionExecuter.execute(SetupLoggingActionExecuter.java:46)
        at org.gradle.tooling.internal.provider.SetupLoggingActionExecuter.execute(SetupLoggingActionExecuter.java:30)
        at org.gradle.launcher.daemon.server.exec.ExecuteBuild.doBuild(ExecuteBuild.java:67)
        at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.WatchForDisconnection.execute(WatchForDisconnection.java:37)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.ResetDeprecationLogger.execute(ResetDeprecationLogger.java:26)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.RequestStopIfSingleUsedDaemon.execute(RequestStopIfSingleUsedDaemon.java:34)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.ForwardClientInput$2.call(ForwardClientInput.java:74)
        at org.gradle.launcher.daemon.server.exec.ForwardClientInput$2.call(ForwardClientInput.java:72)
        at org.gradle.util.Swapper.swap(Swapper.java:38)
        at org.gradle.launcher.daemon.server.exec.ForwardClientInput.execute(ForwardClientInput.java:72)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.LogAndCheckHealth.execute(LogAndCheckHealth.java:55)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.LogToClient.doBuild(LogToClient.java:62)
        at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.EstablishBuildEnvironment.doBuild(EstablishBuildEnvironment.java:82)
        at org.gradle.launcher.daemon.server.exec.BuildCommandOnly.execute(BuildCommandOnly.java:36)
        at org.gradle.launcher.daemon.server.api.DaemonCommandExecution.proceed(DaemonCommandExecution.java:122)
        at org.gradle.launcher.daemon.server.exec.StartBuildOrRespondWithBusy$1.run(StartBuildOrRespondWithBusy.java:50)
        at org.gradle.launcher.daemon.server.DaemonStateCoordinator$1.run(DaemonStateCoordinator.java:295)
        at org.gradle.internal.concurrent.ExecutorPolicy$CatchAndRecordFailures.onExecute(ExecutorPolicy.java:63)
        at org.gradle.internal.concurrent.ManagedExecutorImpl$1.run(ManagedExecutorImpl.java:46)
        at org.gradle.internal.concurrent.ThreadFactoryImpl$ManagedThreadRunnable.run(ThreadFactoryImpl.java:55)
Caused by: org.gradle.api.artifacts.ResolveException: Could not resolve all dependencies for configuration 'detachedConfiguration1'.
        at org.gradle.api.internal.artifacts.ivyservice.ErrorHandlingConfigurationResolver.wrapException(ErrorHandlingConfigurationResolver.java:96)
        at org.gradle.api.internal.artifacts.ivyservice.ErrorHandlingConfigurationResolver.resolveGraph(ErrorHandlingConfigurationResolver.java:68)
        at org.gradle.api.internal.artifacts.configurations.DefaultConfiguration$5.run(DefaultConfiguration.java:534)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:300)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$RunnableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:292)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:90)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.run(DelegatingBuildOperationExecutor.java:31)
        at org.gradle.api.internal.artifacts.configurations.DefaultConfiguration.resolveGraphIfRequired(DefaultConfiguration.java:525)
        at org.gradle.api.internal.artifacts.configurations.DefaultConfiguration.resolveToStateOrLater(DefaultConfiguration.java:510)
        at org.gradle.api.internal.artifacts.configurations.DefaultConfiguration.getResolvedConfiguration(DefaultConfiguration.java:502)
        at org.gradle.api.internal.artifacts.configurations.DefaultConfiguration_Decorated.getResolvedConfiguration(Unknown Source)
        at org.gradle.plugin.use.resolve.internal.ArtifactRepositoriesPluginResolver.exists(ArtifactRepositoriesPluginResolver.java:120)
        at org.gradle.plugin.use.resolve.internal.ArtifactRepositoriesPluginResolver.resolve(ArtifactRepositoriesPluginResolver.java:82)
        at org.gradle.plugin.use.resolve.internal.CompositePluginResolver.resolve(CompositePluginResolver.java:33)
        at org.gradle.plugin.use.resolve.internal.AlreadyOnClasspathPluginResolver.resolve(AlreadyOnClasspathPluginResolver.java:51)
        at org.gradle.plugin.use.internal.DefaultPluginRequestApplicator.resolveToFoundResult(DefaultPluginRequestApplicator.java:253)
        ... 147 more
Caused by: org.gradle.internal.resolve.ArtifactResolveException: Could not determine artifacts for org.gradle.kotlin.kotlin-dsl:org.gradle.kotlin.kotlin-dsl.gradle.plugin:0.18.1
        at org.gradle.api.internal.artifacts.ivyservice.ivyresolve.ErrorHandlingModuleComponentRepository$ErrorHandlingModuleComponentRepositoryAccess.resolveArtifacts(ErrorHandlingModuleComponentRepository.java:171)
        at org.gradle.api.internal.artifacts.ivyservice.ivyresolve.RepositoryChainArtifactResolver.resolveArtifacts(RepositoryChainArtifactResolver.java:65)
        at org.gradle.internal.resolve.resolver.DefaultArtifactSelector.resolveArtifacts(DefaultArtifactSelector.java:60)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.artifact.ResolvedArtifactsGraphVisitor.getArtifacts(ResolvedArtifactsGraphVisitor.java:100)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.artifact.ResolvedArtifactsGraphVisitor.visitEdges(ResolvedArtifactsGraphVisitor.java:69)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.graph.CompositeDependencyGraphVisitor.visitEdges(CompositeDependencyGraphVisitor.java:53)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.graph.builder.DependencyGraphBuilder.assembleResult(DependencyGraphBuilder.java:384)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.graph.builder.DependencyGraphBuilder.resolve(DependencyGraphBuilder.java:121)
        at org.gradle.api.internal.artifacts.ivyservice.resolveengine.DefaultArtifactDependencyResolver.resolve(DefaultArtifactDependencyResolver.java:119)
        at org.gradle.api.internal.artifacts.ivyservice.DefaultConfigurationResolver.resolveGraph(DefaultConfigurationResolver.java:167)
        at org.gradle.api.internal.artifacts.ivyservice.ShortCircuitEmptyConfigurationResolver.resolveGraph(ShortCircuitEmptyConfigurationResolver.java:82)
        at org.gradle.api.internal.artifacts.ivyservice.ErrorHandlingConfigurationResolver.resolveGraph(ErrorHandlingConfigurationResolver.java:66)
        ... 162 more
Caused by: org.gradle.api.resources.ResourceException: Could not get resource 'https://plugins.gradle.org/m2/org/gradle/kotlin/kotlin-dsl/org.gradle.kotlin.kotlin-dsl.gradle.plugin/0.18.1/org.gradle.kotlin.kotlin-dsl.gradle.plugin-0.18.1.jar'.
        at org.gradle.internal.resource.ResourceExceptions.failure(ResourceExceptions.java:74)
        at org.gradle.internal.resource.ResourceExceptions.getFailed(ResourceExceptions.java:57)
        at org.gradle.api.internal.artifacts.repositories.resolver.DefaultExternalResourceArtifactResolver.staticResourceExists(DefaultExternalResourceArtifactResolver.java:87)
        at org.gradle.api.internal.artifacts.repositories.resolver.DefaultExternalResourceArtifactResolver.artifactExists(DefaultExternalResourceArtifactResolver.java:71)
        at org.gradle.api.internal.artifacts.repositories.resolver.ExternalResourceResolver.findOptionalArtifacts(ExternalResourceResolver.java:260)
        at org.gradle.api.internal.artifacts.repositories.resolver.MavenResolver$MavenRemoteRepositoryAccess.resolveModuleArtifacts(MavenResolver.java:244)
        at org.gradle.api.internal.artifacts.repositories.resolver.MavenResolver$MavenRemoteRepositoryAccess.resolveModuleArtifacts(MavenResolver.java:240)
        at org.gradle.api.internal.artifacts.repositories.resolver.ExternalResourceResolver$AbstractRepositoryAccess.resolveArtifacts(ExternalResourceResolver.java:389)
        at org.gradle.api.internal.artifacts.repositories.resolver.ExternalResourceResolver$RemoteRepositoryAccess.resolveArtifacts(ExternalResourceResolver.java:456)
        at org.gradle.api.internal.artifacts.ivyservice.ivyresolve.CachingModuleComponentRepository$ResolveAndCacheRepositoryAccess.resolveArtifacts(CachingModuleComponentRepository.java:412)
        at org.gradle.api.internal.artifacts.ivyservice.ivyresolve.ErrorHandlingModuleComponentRepository$ErrorHandlingModuleComponentRepositoryAccess.resolveArtifacts(ErrorHandlingModuleComponentRepository.java:168)
        ... 173 more
Caused by: org.gradle.internal.resource.transport.http.HttpRequestException: Could not HEAD 'https://plugins.gradle.org/m2/org/gradle/kotlin/kotlin-dsl/org.gradle.kotlin.kotlin-dsl.gradle.plugin/0.18.1/org.gradle.kotlin.kotlin-dsl.gradle.plugin-0.18.1.jar'.
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performRequest(HttpClientHelper.java:96)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performRawHead(HttpClientHelper.java:72)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performHead(HttpClientHelper.java:76)
        at org.gradle.internal.resource.transport.http.HttpResourceAccessor.getMetaData(HttpResourceAccessor.java:65)
        at org.gradle.internal.resource.transfer.DefaultExternalResourceConnector.getMetaData(DefaultExternalResourceConnector.java:63)
        at org.gradle.internal.resource.transfer.AccessorBackedExternalResource.getMetaData(AccessorBackedExternalResource.java:201)
        at org.gradle.internal.resource.BuildOperationFiringExternalResourceDecorator$1.call(BuildOperationFiringExternalResourceDecorator.java:61)
        at org.gradle.internal.resource.BuildOperationFiringExternalResourceDecorator$1.call(BuildOperationFiringExternalResourceDecorator.java:58)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$CallableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:314)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor$CallableBuildOperationWorker.execute(DefaultBuildOperationExecutor.java:304)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.execute(DefaultBuildOperationExecutor.java:174)
        at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:100)
        at org.gradle.internal.operations.DelegatingBuildOperationExecutor.call(DelegatingBuildOperationExecutor.java:36)
        at org.gradle.internal.resource.BuildOperationFiringExternalResourceDecorator.getMetaData(BuildOperationFiringExternalResourceDecorator.java:58)
        at org.gradle.api.internal.artifacts.repositories.resolver.DefaultExternalResourceArtifactResolver.staticResourceExists(DefaultExternalResourceArtifactResolver.java:83)
        ... 181 more
Caused by: javax.net.ssl.SSLProtocolException: Read timed out
        at org.apache.http.conn.ssl.SSLConnectionSocketFactory.createLayeredSocket(SSLConnectionSocketFactory.java:396)
        at org.apache.http.conn.ssl.SSLConnectionSocketFactory.connectSocket(SSLConnectionSocketFactory.java:355)
        at org.apache.http.impl.conn.DefaultHttpClientConnectionOperator.connect(DefaultHttpClientConnectionOperator.java:142)
        at org.apache.http.impl.conn.PoolingHttpClientConnectionManager.connect(PoolingHttpClientConnectionManager.java:373)
        at org.apache.http.impl.execchain.MainClientExec.establishRoute(MainClientExec.java:381)
        at org.apache.http.impl.execchain.MainClientExec.execute(MainClientExec.java:237)
        at org.apache.http.impl.execchain.ProtocolExec.execute(ProtocolExec.java:185)
        at org.apache.http.impl.execchain.RetryExec.execute(RetryExec.java:89)
        at org.apache.http.impl.execchain.RedirectExec.execute(RedirectExec.java:111)
        at org.apache.http.impl.client.InternalHttpClient.doExecute(InternalHttpClient.java:185)
        at org.apache.http.impl.client.CloseableHttpClient.execute(CloseableHttpClient.java:83)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performHttpRequest(HttpClientHelper.java:148)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performHttpRequest(HttpClientHelper.java:126)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.executeGetOrHead(HttpClientHelper.java:103)
        at org.gradle.internal.resource.transport.http.HttpClientHelper.performRequest(HttpClientHelper.java:94)
        ... 195 more
Caused by: java.net.SocketTimeoutException: Read timed out
        ... 210 more


* Get more help at https://help.gradle.org

BUILD FAILED in 44s
[/details]

-------------------------

weitjong | 2018-10-12 02:04:47 UTC | #6

Thanks for bringing this up. I will try to reproduce it in my Android dockerized build environment container over the weekend. We are using a pre-release kotlin-dsl Gradle plugin and things are moving quite fast there. Most probably have to bump up some dependency’s version number.

-------------------------

weitjong | 2018-10-14 03:44:13 UTC | #7

Unfortunately I was not able to reproduce your issue in my newly minted container. The corresponding jar could be successfully downloaded from somewhere to my local Gradle caches. If you have Docker-CE for Mac then you may want to try the Android build using the `urho3d/dockerized-android` docker image.

EDIT: to try it, check out the latest master version of Urho3D project and then type something like this at the project root.
```
script/dockerized.sh android ./gradlew -P ANDROID_ABI=armeabi-v7a build
```

I will wait until Gradle kotlin-dsl releases version 1.0 before bumping our dependency version. They have reached 1.0 RC now, so it should be soon.

-------------------------

att | 2018-10-14 08:32:31 UTC | #8

Thank you, weitjong, I will try it.

-------------------------

weitjong | 2018-10-14 15:00:27 UTC | #9

Keep in mind the `dockerized.sh` and the associated docker images are pre-release software in itself. :P 
Any feedback, bug report, PR are welcome.

You will need the latest version (18.09.x) of Docker-CE from "Edge Release" and not the usual "Stable Release" for Mac. For my Fedora host system, I can only find that latest version in the `docker-ce-test` repo and not even in the `docker-ce-edge` repo. Other readers reading this and want to try, YMMV depends on your host system.

If you are lucky and the script run and completed as per designed then the build artifacts can be found in the usual Android output directories in the project root of your host system, as if you have run the build directly in your host!

-------------------------

Sinoid | 2018-10-16 05:30:15 UTC | #10

Slight tangent, is it even possible to get past Ninja if the path is too deep on windows? The Ninja command-lines CMake spits out are massive. I had to tweak the Cmake scripts just for a `C:\Urho3D` target because those command-lines were so long the last time I did a non-premake android build it refused to do anything.

-------------------------

weitjong | 2018-10-16 13:32:23 UTC | #11

I don’t have many Windows host system to play around. I don’t have first hand experience with the new Gradle Android build on Win10 but based on some user reports it failed due to cmd.exe line buffer limit. However, I have a success on my Win7 VM where CMake/Ninja generator automatically uses response files whenever it is required in order to shorten the command line. I don’t know why it does not work for others though. So, the answer SHOULD BE yes, if someone could figure out how to get the response files work for Win10.

Using Docker on Windows is another workaround to this issue. It basically runs a thin (Linux) container with all the pre-requisite software already installed and build the project for you. Having said that, again I have not tested those docker images on any Windows system yet.

-------------------------

weitjong | 2018-10-19 15:05:15 UTC | #12

The latest commit in the Urho3D master branch has a fallback workaround implemented in the `script/dockerized.sh` so that it should work on any stable repo version of Docker-CE, in case you want to try this for Android build and was blocked by bleeding edge version requirement previously.

-------------------------

weiyuemin | 2018-11-09 04:21:26 UTC | #13

I encountered exactly the same problem with you.
try ./gradlew build --stacktrace, I found the following words in stack trace:
...
Caused by: java.lang.OutOfMemoryError: Java heap space
...

start a taskmgr when building, I found the java.exe occupies more than 3g during the build, then the build fails.

modify gradle.properties fix the problem for me:
org.gradle.jvmargs=-Xmx6G

actually it took 4.7G mem on my machine (win7)

-------------------------

