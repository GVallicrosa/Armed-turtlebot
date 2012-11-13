/****************************************************************************
 *
 * $Id: vpFeatureThetaU.h 3530 2012-01-03 10:52:12Z fspindle $
 *
 * This file is part of the ViSP software.
 * Copyright (C) 2005 - 2012 by INRIA. All rights reserved.
 * 
 * This software is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * ("GPL") version 2 as published by the Free Software Foundation.
 * See the file LICENSE.txt at the root directory of this source
 * distribution for additional information about the GNU GPL.
 *
 * For using ViSP with software that can not be combined with the GNU
 * GPL, please contact INRIA about acquiring a ViSP Professional 
 * Edition License.
 *
 * See http://www.irisa.fr/lagadic/visp/visp.html for more information.
 * 
 * This software was developed at:
 * INRIA Rennes - Bretagne Atlantique
 * Campus Universitaire de Beaulieu
 * 35042 Rennes Cedex
 * France
 * http://www.irisa.fr/lagadic
 *
 * If you have questions regarding the use of this file, please contact
 * INRIA at visp@inria.fr
 * 
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 *
 *
 * Description:
 * Segment visual feature.
 *
 * Authors:
 * Filip Novotny
 * Fabien Spindler
 *
 *****************************************************************************/


#ifndef vpFeatureSegment_H
#define vpFeatureSegment_H

/*!
  \file vpFeatureSegment.h
  \brief class that defines the Segment visual feature
*/

#include <visp/vpMatrix.h>
#include <visp/vpPoint.h>
#include <visp/vpBasicFeature.h>
#include <visp/vpRGBa.h>
#include <visp/vpFeatureException.h>

/*!
  \class vpFeatureSegment
  \ingroup VsFeature2

  \brief Class that defines a 2D segment visual features.
  This class allow to consider two sets of visual features:
  - the non normalised features \f${\bf s} = (x_c, y_c, l, \alpha)\f$ where \f$(x_c,y_c)\f$
    are the coordinates of the segment center, \f$ l \f$ the segment length
    and \f$ \alpha \f$ the orientation of the segment with respect to the \f$ x \f$ axis.
  - or the normalized features \f${\bf s} = (x_n, y_n, l_n, \alpha)\f$ with \f$x_n = x_c/l\f$,
    \f$y_n = y_c/l\f$ and \f$l_n = 1/l\f$.



  The selection of the feature set is done either during construction using vpFeatureSegment(bool),
  or by setNormalized(bool).

*/
class VISP_EXPORT vpFeatureSegment : public vpBasicFeature
{
public:
  //empty constructor
  vpFeatureSegment(bool normalized=false);

  //! Destructor. Does nothing.
  ~vpFeatureSegment() { if (flags != NULL) delete [] flags; }
  // change values of the segment
  void buildFrom(const double x1, const double y1, const double Z1, const double x2, const double y2, const double Z2);

  void display(const vpCameraParameters &cam,
               const vpImage<unsigned char> &I,
               const vpColor &color=vpColor::green,
               unsigned int thickness=1) const ;
  void display(const vpCameraParameters &cam,
               const vpImage<vpRGBa> &I,
               const vpColor &color=vpColor::green,
               unsigned int thickness=1) const ;
  //! Feature duplication.
  vpFeatureSegment *duplicate() const ;
  // compute the error between two visual features from a subset
  // a the possible features
  vpColVector error(const vpBasicFeature &s_star,
                    const unsigned int select = FEATURE_ALL)  ;

  /*!
      Get the x coordinate of the segment center in the image plane.

      \return If normalized features are used, return \f$ x_n = x_c / l \f$. Otherwise return \f$ x_c \f$.
   */
  inline double getXc() const { return s[0] ; }

  /*!
      Get the y coordinate of the segment center in the image plane.

      \return If normalized features are used, return \f$ y_n = y_c / l \f$. Otherwise return \f$ y_c \f$.
    */
  inline double getYc() const { return s[1] ; }

  /*!
      Get the length of the segment.

      \return If normalized features are used, return \f$ l_n = 1 / l \f$. Otherwise return \f$ l \f$.

    */
  inline double getL() const { return s[2] ; }

  /*!
        Get the value of \f$ \alpha \f$ which represents the orientation of the segment.

        \return The value of \f$ \alpha \f$.
    */
  inline double getAlpha() const { return s[3] ;}

  /*!
      Get the value of \f$ Z_1 \f$ which represents the Z coordinate in the camera frame
      of the 3D point that corresponds to the segment first point.

      \return The value of the depth \f$ Z_1 \f$.
    */
  inline double getZ1() const { return Z1_ ;}

  /*!
      Get the value of \f$ Z_2 \f$ which represents the Z coordinate in the camera frame
      of the 3D point that corresponds to the segment second point.

      \return The value of the depth \f$ Z_2 \f$.
    */
  inline double getZ2() const { return Z2_ ;}

  // Basic construction.
  void init() ;

  // compute the interaction matrix from a subset a the possible features
  vpMatrix  interaction(const unsigned int select = FEATURE_ALL);

  void print(const unsigned int select= FEATURE_ALL) const ;

  /*!
    Indicates if the normalized features are considered.
    */
  bool isNormalized() { return normalized_; };

  /*!

    Function used to select the \f$x_c\f$ or \f$x_n\f$ subfeature.

    This function is to use in conjunction with interaction() in order
    to compute the interaction matrix associated to \f$x_c\f$ or \f$x_n\f$ feature.

    See the interaction() method for an usage example.

    This function is also useful in the vpServo class to indicate that
    a subset of the visual feature is to use in the control law:

    \code
  vpFeatureSegment s, s_star; // Current and desired visual feature
  vpServo task;
  ...
  // Add only the xc subset feature from a segment to the task
  task.addFeature(s, s_star, vpFeatureSegment::selectXc());
    \endcode

    \sa selectYc(), selectL(), selectAlpha()
  */
  inline static unsigned int selectXc()  { return FEATURE_LINE[0] ; }

  /*!

    Function used to select the \f$y_c\f$ or \f$y_n\f$ subfeature.

    This function is to use in conjunction with interaction() in order
    to compute the interaction matrix associated to \f$y_c\f$ or \f$y_n\f$ feature.

    See the interaction() method for an usage example.

    This function is also useful in the vpServo class to indicate that
    a subset of the visual feature is to use in the control law:

    \code
  vpFeatureSegment s, s_star; // Current and desired visual feature
  vpServo task;
  ...
  // Add only the yc subset feature from a segment to the task
  task.addFeature(s, s_star, vpFeatureSegment::selectYc());
    \endcode

    \sa selectXc(), selectL(), selectAlpha()
  */

  inline static unsigned int selectYc()  { return FEATURE_LINE[1] ; }

  /*!

    Function used to select the \f$l\f$ or \f$l_n\f$ subfeature.

    This function is to use in conjunction with interaction() in order
    to compute the interaction matrix associated to \f$l\f$ or \f$l_n\f$ feature.

    See the interaction() method for an usage example.

    This function is also useful in the vpServo class to indicate that
    a subset of the visual feature is to use in the control law:

    \code
  vpFeatureSegment s, s_star; // Current and desired visual feature
  vpServo task;
  ...
  // Add only the l subset feature from a segment to the task
  task.addFeature(s, s_star, vpFeatureSegment::selectL());
    \endcode

    \sa selectXc(), selectYc(), selectAlpha()
  */

  inline static unsigned int selectL()  { return FEATURE_LINE[2] ; }

  /*!

    Function used to select the \f$\alpha\f$ subfeature.

    This function is to use in conjunction with interaction() in order
    to compute the interaction matrix associated to \f$\alpha\f$ feature.

    See the interaction() method for an usage example.

    This function is also useful in the vpServo class to indicate that
    a subset of the visual feature is to use in the control law:

    \code
  vpFeatureSegment s, s_star; // Current and desired visual feature
  vpServo task;
  ...
  // Add only the alpha subset feature from a segment to the task
  task.addFeature(s, s_star, vpFeatureSegment::selectAlpha());
    \endcode

    \sa selectXc(), selectYc(), selectL()
  */

  inline static unsigned int selectAlpha() { return FEATURE_LINE[3] ; }
  
  /*!
    Set the king of feature to consider.
    \param normalized : If true, use normalized features \f${\bf s} = (x_n, y_n, l_n, \alpha)\f$.
    If false, use non normalized features \f${\bf s} = (x_c, y_c, l_c, \alpha)\f$.
    */
  void setNormalized(bool normalized) { normalized_ = normalized; };
  /*!

    Set the value of the x coordinate of the segment center
    in the image plane.  It is one parameter of the visual feature \f$ s \f$.

    \param val : Value to set, that is either equal to \f$ x_n = x_c/l \f$ when normalized features
    are considered, or equal to \f$ x_c \f$ otherwise.
  */
  inline void setXc(const double val){
    s[0] = xc_ = val;
    flags[0] = true;
  }
  /*!

    Set the value of the y coordinate of the segment center
    in the image plane.  It is one parameter of the visual feature \f$ s \f$.

    \param val : Value to set, that is either equal to \f$ y_n = y_c/l \f$ when normalized features
    are considered, or equal to \f$ y_c \f$ otherwise.
  */
  inline void setYc(const double val){
    s[1] = yc_ = val;
    flags[1] = true;
  }
  /*!

    Set the value of the segment length in the image plane. It is one parameter of the visual feature \f$ s \f$.

    \param val : Value to set, that is either equal to \f$l_n= 1/l \f$ when normalized features
    are considered, or equal to \f$ l \f$ otherwise.
  */
  inline void setL(const double val){
    s[2] = l_ = val;
    flags[2] = true;
  }
  /*!

    Set the value of \f$ \alpha \f$ which represents the orientation of the segment
    in the image plane. It is one parameter of the visual feature \f$ s \f$.

    \param val : \f$ \alpha \f$ value to set.
  */
  inline void setAlpha(const double val){
    s[3] = alpha_ = val;
    cos_a_ = cos(val);
    sin_a_ = sin(val);
    flags[3] = true;
  }

  /*!

    Set the value of \f$ Z_1 \f$ which represents the Z coordinate in the camera frame
    of the 3D point that corresponds to the segment first point.

    This value is requested to compute the interaction matrix.

    \param val : \f$ Z_1 \f$ value to set.

    \exception vpFeatureException::badInitializationError : If Z1 is behind the camera or equal to zero.
  */
  inline void setZ1(const double val)
  {
    Z1_ = val;

    if (Z1_ < 0)
    {
      vpERROR_TRACE("Point is behind the camera ") ;
      std::cout <<"Z1 = " << Z1_ << std::endl ;

      throw(vpFeatureException(vpFeatureException::badInitializationError,
             "Point Z1 is behind the camera ")) ;
    }

    if (fabs(Z1_) < 1e-6)
    {
      vpERROR_TRACE("Point Z1 coordinates is null ") ;
      std::cout <<"Z1 = " << Z1_ << std::endl ;

      throw(vpFeatureException(vpFeatureException::badInitializationError,
             "Point Z1 coordinates is null")) ;
    }

    flags[4] = true;
  }

  /*!

    Set the value of \f$ Z_2 \f$ which represents the Z coordinate in the camera frame
    of the 3D point that corresponds to the segment second point.

    This value is requested to compute the interaction matrix.

    \param val : \f$ Z_2 \f$ value to set.

    \exception vpFeatureException::badInitializationError : If Z2 is behind the camera or equal to zero.
  */
  inline void setZ2(const double val)
  {
    Z2_ = val;

    if (Z2_ < 0)
    {
      vpERROR_TRACE("Point Z2 is behind the camera ") ;
      std::cout <<"Z2 = " << Z2_ << std::endl ;

      throw(vpFeatureException(vpFeatureException::badInitializationError,
             "Point Z2 is behind the camera ")) ;
    }

    if (fabs(Z2_) < 1e-6)
    {
      vpERROR_TRACE("Point Z2 coordinates is null ") ;
      std::cout <<"Z2 = " << Z2_ << std::endl ;

      throw(vpFeatureException(vpFeatureException::badInitializationError,
             "Point Z2 coordinates is null")) ;
    }

    flags[5] = true;
  }


private:
  double xc_;
  double yc_;
  double l_;
  double alpha_;
  double Z1_;
  double Z2_;
  double cos_a_;
  double sin_a_;
  bool normalized_;
} ;

#endif

