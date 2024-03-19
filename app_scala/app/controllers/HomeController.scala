package controllers

import logic.Factorial
import play.api.Logger
import play.api.i18n.Lang.logger
import play.api.mvc._

import javax.inject._

/** This controller creates an `Action` to handle HTTP requests to the application's home page.
  */
@Singleton
class HomeController @Inject() (val controllerComponents: ControllerComponents) extends BaseController {

//  private val logger = Logger("time")

  /** Create an Action to render an HTML page.
    *
    * The configuration in the `routes` file means that this method will be called when the application receives a `GET`
    * request with a path of `/`.
    */
  def index(): Action[AnyContent] = Action { implicit request: Request[AnyContent] =>
    logger.info(s"called ${request.host} endpoint")
    Ok(Factorial(5).get.toString)
  }
}
