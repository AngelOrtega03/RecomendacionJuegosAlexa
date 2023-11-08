# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import mysql.connector

mydb = mysql.connector.connect(
  host="146.190.218.21",
  user="agustin",
  password="dalkoeslaonda",
  database="alexaskill_sql"
)

mycursor = mydb.cursor()


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Llegó la hora de recomendar juegos! Para que te recomiende uno, puedes decir, por ejemplo: Recomiendame un juego de estrategia. O puedes checar los comandos existentes, diciendo, ayuda o ayuda con los comandos."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class GenreSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomGenreIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        genero = slots["genero"].value
        if(genero):
            mycursor.execute("SELECT nombre, plataforma, desarrollador FROM juegos WHERE genero = %s ORDER BY RAND() LIMIT 1",(genero,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego del genero "+genero+" que te recomiendo es "+respuesta[0]+", para la plataforma "+respuesta[1]+", desarrollado por "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que estuviera en dicho genero. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PlatformSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomPlatformIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        plataforma = slots["plataforma"].value
        if(plataforma):
            mycursor.execute("SELECT nombre, genero, desarrollador FROM juegos WHERE plataforma = %s ORDER BY RAND() LIMIT 1",(plataforma,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego de la plataforma "+plataforma+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", desarrollado por "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que estuviera en dicha plataforma. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    

class DeveloperSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomDeveloperIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        desarrollador = slots["desarrollador"].value
        if(desarrollador):
            mycursor.execute("SELECT nombre, genero, plataforma FROM juegos WHERE desarrollador = %s ORDER BY RAND() LIMIT 1",(desarrollador,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego del desarrollador "+desarrollador+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", para la plataforma "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que haya sido hecho por ese desarrollador. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
    
class RandomSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomCustomIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        mycursor.execute("SELECT nombre, genero, plataforma, clasificacion FROM juegos ORDER BY RAND() LIMIT 1")
        respuesta = mycursor.fetchone()
        speak_output = "Un juego que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", para la plataforma "+respuesta[2]+", con clasificación para "+respuesta[3]

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RatingSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomRatingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        clasificacion = slots["clasificacion"].value
        if(clasificacion):
            mycursor.execute("SELECT nombre, genero, plataforma, desarrollador FROM juegos WHERE clasificacion = %s ORDER BY RAND() LIMIT 1",(clasificacion,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego para "+clasificacion+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", para la plataforma "+respuesta[2]+", desarrollado por "+respuesta[3]
        else:
            speak_output = "Vaya. No pude encontrar un juego que tenga esa clasificacion. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class GenrePlatformSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomGenrePlatformIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        genero = slots["genero"].value
        plataforma = slots["plataforma"].value
        if(genero and plataforma):
            mycursor.execute("SELECT nombre, desarrollador, clasificacion FROM juegos WHERE genero = %s AND plataforma = %s ORDER BY RAND() LIMIT 1",(genero,plataforma,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego del genero "+genero+" para la plataforma "+plataforma+" que te recomiendo es "+respuesta[0]+", del desarrollador "+respuesta[1]+", con clasificacion para "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de ese genero como de esa plataforma. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
class GenreRatingSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomGenreRatingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        genero = slots["genero"].value
        clasificacion = slots["clasificacion"].value
        if(genero and clasificacion):
            mycursor.execute("SELECT nombre, desarrollador, plataforma FROM juegos WHERE genero = %s AND clasificacion = %s ORDER BY RAND() LIMIT 1",(genero,clasificacion,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego del genero "+genero+" de clasificacion "+clasificacion+" que te recomiendo es "+respuesta[0]+", del desarrollador "+respuesta[1]+", para la plataforma "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de ese genero como de esa clasificacion. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class GenreDeveloperSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomGenreDeveloperIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        genero = slots["genero"].value
        desarrollador = slots["desarrollador"].value
        if(genero and desarrollador):
            mycursor.execute("SELECT nombre, plataforma, clasificacion FROM juegos WHERE genero = %s AND desarrollador = %s ORDER BY RAND() LIMIT 1",(genero,desarrollador,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego del genero "+genero+" desarrollado por "+desarrollador+" que te recomiendo es "+respuesta[0]+", de la plataforma "+respuesta[1]+", con clasificacion para "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de ese genero como de ese desarrollador. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PlatformRatingSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomPlatformRatingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        plataforma = slots["plataforma"].value
        clasificacion = slots["clasificacion"].value
        if(plataforma and clasificacion):
            mycursor.execute("SELECT nombre, genero, desarrollador FROM juegos WHERE plataforma = %s AND clasificacion = %s ORDER BY RAND() LIMIT 1",(plataforma,clasificacion,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego de la plataforma "+plataforma+" de clasificacion para "+clasificacion+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", desarrollado por "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de esa plataforma como de esa clasificacion. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class PlatformDeveloperSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomPlatformDeveloperIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        plataforma = slots["plataforma"].value
        desarrollador = slots["desarrollador"].value
        if(plataforma and desarrollador):
            mycursor.execute("SELECT nombre, genero, clasificacion FROM juegos WHERE plataforma = %s AND clasificacion = %s ORDER BY RAND() LIMIT 1",(plataforma,clasificacion,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego de la plataforma "+plataforma+" desarrollado por "+desarrollador+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", de clasificacion para "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de esa plataforma como de ese desarrollador. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RatingDeveloperSearchIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CustomRatingDeveloperIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        desarrollador = slots["desarrollador"].value
        clasificacion = slots["clasificacion"].value
        if(plataforma and clasificacion):
            mycursor.execute("SELECT nombre, genero, plataforma FROM juegos WHERE desarrollador = %s AND clasificacion = %s ORDER BY RAND() LIMIT 1",(desarrollador,clasificacion,))
            respuesta = mycursor.fetchone()
            speak_output = "El juego de clasificacion para "+clasificacion+", desarrollado por "+desarrollador+" que te recomiendo es "+respuesta[0]+", del genero "+respuesta[1]+", para la plataforma "+respuesta[2]
        else:
            speak_output = "Vaya. No pude encontrar un juego que sea tanto de esa clasificacion como de ese desarrollador. Por favor, intenta de nuevo."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_genero = "Para recomendar juegos por genero, di: recomiendame un juego de, y el nombre del genero. "
        speak_plataforma = "Para recomendar juegos por plataforma, di: recomiendame un juego para, y el nombre de la plataforma. "
        speak_clasificacion = "Para recomendar juegos por clasificacion, di: recomiendame un juego hecho para, y el publico destinado. "
        speak_desarrollador = "Para recomendar juegos por desarrollador, di: recomiendame un juego hecho por, y el nombre del desarrollador."
        speak_output = speak_genero+speak_plataforma+speak_clasificacion+speak_desarrollador
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "OK. Si quieres volver a escuchar recomendaciones, no te olvides de decir: Alexa, recomendacion de juegos!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm. No he logrado entenderte. Si tienes problemas con los comandos, puedes decir: ayuda, o, ayuda con los comandos"
        reprompt = "No logro entender del todo. ¿En que te puedo ayudar?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Lo siento. No logro entender tu peticion. Por favor, intenta de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GenreSearchIntentHandler())
sb.add_request_handler(PlatformSearchIntentHandler())
sb.add_request_handler(DeveloperSearchIntentHandler())
sb.add_request_handler(RandomSearchIntentHandler())
sb.add_request_handler(RatingSearchIntentHandler())
sb.add_request_handler(GenrePlatformSearchIntentHandler())
sb.add_request_handler(GenreRatingSearchIntentHandler())
sb.add_request_handler(GenreDeveloperSearchIntentHandler())
sb.add_request_handler(PlatformRatingSearchIntentHandler())
sb.add_request_handler(PlatformDeveloperSearchIntentHandler())
sb.add_request_handler(RatingDeveloperSearchIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()